__author__ = "Jeremy Leese | jeremy.leese@thomsonreuters.com | Technology - Product Eng - Content Platforms"
__copyright__ = "Copyright© (C) 2022 Thomson Reuters. All Rights Reserved."
__version__ = "0.3"

import boto3
from botocore.exceptions import ClientError
import base64
import os
import json
import psycopg
import util

##
# constants
##
RDS_SERVICE="rds"
SECRETS_MANAGER_SERVICE = "secretsmanager"

REGION_NAME = 'us-east-1'
POSTGRES = "postgres"

DEVELOPMENT = "DEVELOPMENT"
DEV = "DEV"
TEST = "TEST"
QC = "QC"
QA = "QA"
CLIENT = "CLIENT"
PROD = "PROD"

METADOC = "metadoc"
ECPQUEUE = "ecpqueue"
LOADQUEUE = "loadqueue"
LAGER = "lager"
CCI = "cci"
PERSIST = "persist"
STATUS = "status"

ROTATION_INTERVAL = 90 # int days

RESOURCE_OWNER = "AMS-Novus.thomsonreuters.com"
FINANCIAL_ID = "23310"
ASSET_ID = "207947"

CREATE_COUNT = 0

## END constants

##
#  BEGIN DEF get_db_instances(REGION_NAME)
#  return the list of db instances in the account region
##
def get_db_instances(REGION_NAME):

    client = util.get_client(REGION_NAME, RDS_SERVICE)

    try:

        describe_db_response = client.describe_db_instances()

    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print("The requested secret was not found")
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            print("The request was invalid due to:", e)
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            print("The request had invalid params:", e)
        elif e.response['Error']['Code'] == 'DecryptionFailure':
            print("The requested secret can't be decrypted using the provided KMS key:", e)
        elif e.response['Error']['Code'] == 'InternalServiceError':
            print("An error occurred on service side:", e)
        else: 
            print("An error occurred on service side:", e)
    else:

        return describe_db_response.get("DBInstances")

# END DEF get_db_instances

##
#   BEGIN DEF get_secret_string(secret_name)
#   return the secret string for AWS region and friendly secret name
##
def get_secret_value(secret_name):

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager')

    '''
    client = session.client(
        service_name='secretsmanager',
        REGION_NAME=REGION_NAME
    )
    '''

    try:
        
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)

    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            # An error occurred on the server side.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            # You provided an invalid value for a parameter.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            # You provided a parameter value that is not valid for the current state of the resource.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            # We can't find the resource that you asked for.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        else: print(e)
    else:
        # Decrypts secret using the associated KMS CMK.
        # Depending on whether the secret is a string or binary, one of these fields will be populated.
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            return secret
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
            return decoded_binary_secret
            

    return None

##   END DEF get_secret_string(secret_name)

##
#   BEGIN DEF update_secret(REGION_NAME, secret_name, secret_string)
##
def update_secret(REGION_NAME, secret_name, secret_string):

    client = util.get_client(REGION_NAME, SECRETS_MANAGER_SERVICE)

    try:
        response = client.update_secret(SecretId=secret_name, SecretString=secret_string)
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print("The requested secret " + secret_name + " was not found")
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            print("The request was invalid due to:", e)
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            print("The request had invalid params:", e)
        elif e.response['Error']['Code'] == 'DecryptionFailure':
            print("The requested secret can't be decrypted using the provided KMS key:", e)
        elif e.response['Error']['Code'] == 'InternalServiceError':
            print("An error occurred on service side:", e)
        else: 
            print("An error occurred on service side:", e)
    else:

        return response

##   END DEF update_secret(REGION_NAME, secret_name, secret_string)


##
#   BEGIN DEF get_secrets_list()
##
def get_secrets_list(region):
    client = util.get_client(region, SECRETS_MANAGER_SERVICE)

    secrets_list = None
    next_token = None

    try:
        response = client.list_secrets(MaxResults=100)
        secrets_list = response.get('SecretList')
        next_token = response.get('NextToken')

        while(next_token):
            response = client.list_secrets(MaxResults=100, NextToken=next_token)
            secrets_list.extend(response.get('SecretList'))
            next_token = response.get('NextToken')

        return secrets_list
    
    except ClientError as e:
        raise Exception("boto3 client error in get_secrets: " + e.__str__())
    except Exception as e:
        raise Exception("Unexpected error in get_secrets: " + e.__str__()) 

##   END DEF get_secrets_list()

##
# BEGIN DEF disable_auto_rotation()    
##            
def disable_auto_rotation():
    
    dev_pattern =  'dev-us-east-1' 
    test_pattern = 'test-us-east-1'
    qa_pattern = 'qa-us-east-1'

    client = util.get_client(REGION_NAME, SECRETS_MANAGER_SERVICE)

    secrets_list = get_secrets_list(REGION_NAME)

    print()

    count1 = 0
    count2 = 1

    for secrets in secrets_list:
        secret_name = secrets['Name']
        count1 = count1 + 1
        #only execute for novus test/qc - so cheesy, need a tag or something
        #if secret_name.find(dev_pattern) >= 0 or  secret_name.find(test_pattern) >= 0:
        if secret_name.find(qa_pattern) >= 0:
            count2 = count2 + 1
            print('   update:', secret_name)
            response = client.cancel_rotate_secret(SecretId=secret_name)
            print(response)
            print()
        else:
            print('no update:', secret_name)

    print(count2)
    print(count1)
    print('DAR END')

def log_print(msg, log, to_sys):
    
    print(msg, file=log)

    if(to_sys):
        print(msg)

'''
# BEGIN def audit_secrets()
'''
def audit_secrets():
    try:
        LOG = open('client_secrets_audit.log', 'w')
        schema_log = open('aws_client_schemas.txt', 'w')

        print('BEGIN', file=LOG)
        
        OPEN_SSH_TUNNEL="cloud-tool ssh-tunnel -r 8893 -I -c "
        CLOSE_SSH_TUNNEL="cloud-tool ssh-tunnel --close -r 8893 -I -c "

        tunnel_open = False
        cur = None
        conn = None

        client = util.get_client(REGION_NAME, SECRETS_MANAGER_SERVICE)

        secrets_list = get_secrets_list(REGION_NAME)
        
        for secrets in secrets_list:

            secret_name = secrets['Name']
            print('Secret Name: ', secret_name)
        
            if ("qa-us-east-1" in secret_name or "prod-us-east-1" in secret_name) & ("-pg-sm2" in secret_name):

                #secret = get_secret('us-east-1', secret_name)
                secret = client.get_secret_value(SecretId=secret_name)
                secret_string = secret.get('SecretString')
                print(type(secret_string), secret_string)
                secret_dict = json.loads(secret_string)   
                #print("\tSecret Dictionary: ", secret_dict)

                host =  secret_dict.get('host')
                db_name = secret_dict.get('dbname')
                db_user = secret_dict.get('username')
                db_password = secret_dict.get('password')

                tunnel_cmd = OPEN_SSH_TUNNEL + host
                os.system(tunnel_cmd)
                tunnel_open = True

                try:
                    
                    print('Connecting to the PostgreSQL database ' + db_name + '...')
                    conn = psycopg.connect(dbname=db_name, user='postgres', password='postgres', host="localhost", port="5432")
                    cur = conn.cursor()
                    cur.execute("SELECT schema_name FROM information_schema.schemata")
                    rows = cur.fetchall()

                    print(file=LOG)
                    print('SUCCESS:', secret_name, file=LOG)
                    print()
                    print('SUCCESS:', secret_name)
                    
                    #print(db_name, file=schema_log)
                    print(db_name)

                    for row in rows:
                        print('\t', row[0], file=schema_log)
                        print('\t', row[0])

                except (Exception, psycopg.DatabaseError) as error:
                    
                    print('Secret Name:', secret_name, file=LOG)
                    print('\tERROR:', error, file=LOG)
                    print('\t\t  DB:', db_name, file=LOG)
                    print('\t\tUser:', db_user, file=LOG)
                    print('\t\t  PW:', db_password, file=LOG)
                    print(file=LOG)

                    print('Secret Name:', secret_name)
                    print('\tERROR:', error)
                    print('\t\t  DB:', db_name)
                    print('\t\tUser:', db_user)
                    print('\t\t  PW:', db_password)
                    print()

                finally:
                    LOG.close
                    if cur is not None:
                        cur.close()
                        cur = None
                        print('Database cursor closed.')
                    if conn is not None:
                        conn.close()
                        conn = None
                        print('Database connection closed.')
                    if tunnel_open:
                        tunnel_cmd = CLOSE_SSH_TUNNEL + host
                        os.system(tunnel_cmd)
                        tunnel_open = False
                        print('SSH tunnel closed.')
                
                if tunnel_open:
                    tunnel_cmd = CLOSE_SSH_TUNNEL + host
                    os.system(tunnel_cmd)
                    tunnel_open = False
                    print('SSH tunnel closed.')
    finally:
            LOG.close
            if cur is not None:
                cur.close()
                cur = None
                print('Database cursor closed.')
            if conn is not None:
                conn.close()
                conn = None
                print('Database connection closed.')
            if tunnel_open:
                tunnel_cmd = CLOSE_SSH_TUNNEL + host
                os.system(tunnel_cmd)
                tunnel_open = False
                print('SSH tunnel closed.')

'''
# manual_secret_create(secret_name, secret_string, db_resource, lambda_rotation, description)
'''
def manual_secret_create(secret_name, secret_string, db_resource, lambda_rotation, description, rotate):
    

    if 'loadqueue' in db_resource:
        db_resource = 'loadqueue'

    print()
    print('secret_name:', secret_name)
    print('secret_string:', secret_string)
    print('db_resource:', db_resource)
    print('lambda_rotation:', lambda_rotation)
    print('description:', description)
    print()

    secrets_client = util.get_client(REGION_NAME, SECRETS_MANAGER_SERVICE)

    try:
        secrets_client.create_secret(Name=secret_name,
                                    Description=description,
                                    SecretString=secret_string,
                                    Tags=[
                                        {
                                            'Key': 'tr:resource-owner',
                                            'Value': 'ams-novus@thomsonreuters.com'
                                        },
                                        {
                                            'Key': 'tr:environment-type',
                                            'Value': 'qa'
                                        },
                                        {
                                            'Key': 'tr:environment-name',
                                            'Value': 'client'
                                        },
                                        {
                                            'Key': 'tr:financial-identifier',
                                            'Value': FINANCIAL_ID
                                        },
                                        {
                                            'Key': 'tr:application-asset-insight-id',
                                            'Value': ASSET_ID
                                        },
                                        {
                                            'Key': 'tr:db-resource',
                                            'Value': db_resource
                                        },
                                        {
                                            'Key': 'Name',
                                            'Value': secret_name
                                        },
                                    ],

                                    ForceOverwriteReplicaSecret = True)

        if rotate:
            secrets_client.rotate_secret(RotationLambdaARN=lambda_rotation,
                                        RotationRules={
                                            'AutomaticallyAfterDays': ROTATION_INTERVAL,
                                        },
                                        SecretId=secret_name)
    except Exception as e:
        print("An error occurred on service side:", e)

'''
##
# build_secret_string: build a secret string for use in aws api method calls
##
'''
def build_secret_string(user_name, password, host, port, db_name, cluster_id):

    secret_string = "{"
    secret_string += "\"username\":"
    secret_string += "\"" + user_name + "\","
    secret_string += "\"password\":"
    secret_string += "\"" + password + "\","
    secret_string += "\"engine\":"
    secret_string += "\"" + POSTGRES + "\","
    secret_string += "\"host\":"
    secret_string += "\"" + host + "\","
    secret_string += "\"port\":"
    secret_string += "\"" + port + "\","
    secret_string += "\"dbname\":"
    secret_string += "\"" + db_name + "\","
    secret_string += "\"dbClusterIdentifier\":"
    secret_string += "\"" + cluster_id + "\""
    secret_string += "}"

    return secret_string

'''
### END build_secret_string
'''

'''
# create_secrets()
'''
def create_secrets_hvr(rotate):
    primary = 'a-prod'
    secondary_b = 'b-prod'
    region = 'us-east-1'
    read_user = 'novusr1'
    update_user = 'novusu1'
    read_pw = 'novusr1'
    update_pw = 'novusu1'
    port = ''

    secrets_client = util.get_client(REGION_NAME, SECRETS_MANAGER_SERVICE)

    secrets = get_secrets_list(region)

    for secret in secrets:

        secret_name = secret['Name']

        print(secret_name)

        db_resource = secret_name[8:]

        #if secret_name.find('cci') >= 0:
        #    print(secret_name)
        #    print('\t', db_resource)

        if '-pg-sm' in secret_name and 'prod' in secret_name and 'docloc-ha' in secret_name:
        #if pos >= 0 and secret_name.find('-qa-prod') >= 0:
            print('secret_name', secret_name, 'db_resource:', db_resource)

            description = secret['Description']
            rotation_lambda = secret['RotationLambdaARN']

            app_secret_name = secret_name[:8]
            app_secret_name = app_secret_name + 'novus-'
            
            pos = secret_name.find('-prod-us')
            app_secret_name = app_secret_name + secret_name[8:pos]

            db_resource = secret_name[8:]
            pos = db_resource.find('-prod-')
            db_resource = db_resource[:pos - 1]
            db_resource = db_resource.replace('-','.')

            #print('secret_name', secret_name)
            secret = secrets_client.get_secret_value(SecretId=secret_name)
            secret_string = secret.get('SecretString')
            secret_dict = json.loads(secret_string)  

            host =  secret_dict.get('host')
            db_name = secret_dict.get('dbname')
            port = secret_dict.get('port')
            cluster_id = secret_dict.get('dbClusterIdentifier')

            if secret_name.find(primary) >= 0:
                print("PRIMARY:", secret_name)
                
                user_name = update_user
                password = update_pw
                temp_name = app_secret_name + '-db-update-prod-us-east-1'

                description = 'Novus application UPDATE access for ' + db_resource.replace('.','-') + 'a PROD DB.'
                secret_string = build_secret_string(user_name, password, host, port, db_name, cluster_id)
                
                manual_secret_create(temp_name, secret_string, db_resource, rotation_lambda, description, rotate)

                user_name = read_user
                password = read_pw
                temp_name = app_secret_name + '-db-read-prod-us-east-1'
                description = 'Novus application READ access for ' + db_resource.replace('.','-') + 'a PROD DB.'
                secret_string = build_secret_string(user_name, password, host, port, db_name, cluster_id)

                manual_secret_create(temp_name, secret_string, db_resource, rotation_lambda, description, rotate)

            elif secret_name.find(secondary_b) >= 0:
                print('SECONDARY B:', secret_name)
                
                user_name = update_user
                password = update_pw
                temp_name = app_secret_name + '-db-update-prod-us-east-1'

                secret_string = build_secret_string(user_name, password, host, port, db_name, cluster_id)
                description = 'Novus application UPDATE access for ' + db_resource.replace('.','-') + 'b PROD DB.'

                manual_secret_create(temp_name, secret_string, db_resource, rotation_lambda, description, rotate)

                user_name = read_user
                password = read_pw
                temp_name = app_secret_name + '-db-read-prod-us-east-1'
                secret_string = build_secret_string(user_name, password, host, port, db_name, cluster_id)
                description = 'Novus application READ access for ' + db_resource.replace('.','-') + 'b PROD DB.'

                manual_secret_create(temp_name, secret_string, db_resource, rotation_lambda, description, rotate)


            else:
                print("NOT FOUND:", secret_name)
'''
# EDD create_secrets()
'''

'''
##
# build_secret_string: build a secret string for use in aws api method calls
##
'''
def build_secret_string(user_name, password, host, port, db_name, cluster_id):

    secret_string = "{"
    secret_string += "\"username\":"
    secret_string += "\"" + user_name + "\","
    secret_string += "\"password\":"
    secret_string += "\"" + password + "\","
    secret_string += "\"engine\":"
    secret_string += "\"" + POSTGRES + "\","
    secret_string += "\"host\":"
    secret_string += "\"" + host + "\","
    secret_string += "\"port\":"
    secret_string += "\"" + port + "\","
    secret_string += "\"dbname\":"
    secret_string += "\"" + db_name + "\","
    secret_string += "\"dbClusterIdentifier\":"
    secret_string += "\"" + cluster_id + "\""
    secret_string += "}"

    return secret_string

'''
# update_secret
'''
def update_secret(REGION_NAME, secret_name, secret_string):

    client = util.get_client(REGION_NAME, SECRETS_MANAGER_SERVICE)

    try:

        response = client.update_secret(SecretId=secret_name, SecretString=secret_string)
    
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print("The requested secret " + secret_name + " was not found")
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            print("The request was invalid due to:", e)
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            print("The request had invalid params:", e)
        elif e.response['Error']['Code'] == 'DecryptionFailure':
            print("The requested secret can't be decrypted using the provided KMS key:", e)
        elif e.response['Error']['Code'] == 'InternalServiceError':
            print("An error occurred on service side:", e)
        else: 
            print("An error occurred on service side:", e)
    else:

        return response

    ## END else

'''
### END update_secret
'''

'''
##
# build_secret_string: build a secret string for use in aws api method calls
##
'''
def build_secret_string(user_name, password, host, port, db_name, cluster_id):

    secret_string = "{"
    secret_string += "\"username\":"
    secret_string += "\"" + user_name + "\","
    secret_string += "\"password\":"
    secret_string += "\"" + password + "\","
    secret_string += "\"engine\":"
    secret_string += "\"" + POSTGRES + "\","
    secret_string += "\"host\":"
    secret_string += "\"" + host + "\","
    secret_string += "\"port\":"
    secret_string += "\"" + port + "\","
    secret_string += "\"dbname\":"
    secret_string += "\"" + db_name + "\","
    secret_string += "\"dbClusterIdentifier\":"
    secret_string += "\"" + cluster_id + "\""
    secret_string += "}"

    return secret_string

'''
### END build_secret_string
'''

'''
'''
def update_secrets():
    secrets_list = get_secrets_list(REGION_NAME)

    for secret in secrets_list:
        secret_name = secret['Name']
        #print(secret_name)

        if 'z-db' not in secret_name and ('update-qa' in secret_name or 'read-qa' in secret_name):
            secret_string = get_secret_value(secret_name)
            secret_dict = json.loads(secret_string)

            host =  secret_dict.get('host')
            db_name = secret_dict.get('dbname')
            db_user = secret_dict.get('username')
            db_password = secret_dict.get('password')
            port = secret_dict.get('port')
            cluster_id = secret_dict.get('dbClusterIdentifier')

            new_secret_string = build_secret_string(db_user, db_user, host, port, db_name, cluster_id)

            print(new_secret_string)

            update_secret(REGION_NAME, secret_name, new_secret_string)
'''
'''

'''
# create_secrets()
'''
def create_secrets(rotate):
    primary = 'a-dev'
    secondary_b = 'b-dev'
    region = 'us-east-1'
    read_user = 'novusr1'
    update_user = 'novusu1'
    read_pw = 'novusr1'
    update_pw = 'novusu1'
    port = ''

    secrets_client = util.get_client(REGION_NAME, SECRETS_MANAGER_SERVICE)

    secrets = get_secrets_list(region)

    for secret in secrets:

        secret_name = secret['Name']

        db_resource = secret_name[8:]
 
        pos = db_resource.find('-dev-')

        if pos >= 0 and 'perfmart-01a-dev' in secret_name and 'z-db' not in secret_name :
            print('secret_name', secret_name, 'db_resource:', db_resource)

            description = secret['Description']
            rotation_lambda = secret['RotationLambdaARN']

            app_secret_name = secret_name[:8]
            app_secret_name = app_secret_name + 'novus-'
            
            pos = secret_name.find('-dev-us')
            app_secret_name = app_secret_name + secret_name[8:pos]

            db_resource = secret_name[8:]
            pos = db_resource.find('-dev-')
            db_resource = db_resource[:pos - 1]
            db_resource = db_resource.replace('-','.')

            #print('secret_name', secret_name)
            secret = secrets_client.get_secret_value(SecretId=secret_name)
            secret_string = secret.get('SecretString')
            secret_dict = json.loads(secret_string)  

            host =  secret_dict.get('host')
            db_name = secret_dict.get('dbname')
            port = secret_dict.get('port')
            cluster_id = secret_dict.get('dbClusterIdentifier')


            if secret_name.find(primary) >= 0:
                print("PRIMARY:", secret_name)
                
                user_name = update_user
                password = update_pw
                temp_name = app_secret_name + '-db-update-dev-us-east-1'
                description = 'Novus application UPDATE access for ' + db_resource.replace('.','-') + ' DEV DB.'
                secret_string = build_secret_string(user_name, password, host, port, db_name, cluster_id)
                
                manual_secret_create(temp_name, secret_string, db_resource, rotation_lambda, description, rotate)

                user_name = read_user
                password = read_pw
                temp_name = app_secret_name + '-db-read-qa-us-east-1'
                description = 'Novus application READ access for ' + db_resource.replace('.','-') + ' DEV DB.'
                secret_string = build_secret_string(user_name, password, host, port, db_name, cluster_id)

                manual_secret_create(temp_name, secret_string, db_resource, rotation_lambda, description, rotate)

            elif secret_name.find(secondary_b) >= 0:
                print('SECONDARY B:', secret_name)
                
                user_name = update_user
                password = update_pw
                temp_name = app_secret_name + '-db-update-qa-us-east-1'
                secret_string = build_secret_string(user_name, password, host, port, db_name, cluster_id)
                description = 'Novus application UPDATE access for ' + db_resource.replace('.','-') + 'b Quality Assurance DB.'

                manual_secret_create(temp_name, secret_string, db_resource, rotation_lambda, description, rotate)

                user_name = read_user
                password = read_pw
                temp_name = app_secret_name + '-db-read-qa-us-east-1'
                secret_string = build_secret_string(user_name, password, host, port, db_name, cluster_id)
                description = 'Novus application READ access for ' + db_resource.replace('.','-') + 'b Quality Assurance DB.'

                manual_secret_create(temp_name, secret_string, db_resource, rotation_lambda, description, rotate)

            else:
                print("NOT FOUND:", secret_name)
'''
# EDD create_secrets()
'''


'''
# manual_secret_create(secret_name, secret_string, db_resource, lambda_rotation, description)
'''
def manual_secret_create(secret_name, secret_string, db_resource, lambda_rotation, description, rotate):

    print()
    print('secret_name:', secret_name)
    print('db_resource:', db_resource)
    print('lambda_rotation:', lambda_rotation)
    print('description:', description)
    print()

    secrets_client = util.get_client(REGION_NAME, SECRETS_MANAGER_SERVICE)

    try:
        secrets_client.create_secret(Name=secret_name,
                                    Description=description,
                                    SecretString=secret_string,
                                    Tags=[
                                        {
                                            'Key': 'tr:resource-owner',
                                            'Value': 'ams-novus@thomsonreuters.com'
                                        },
                                        {
                                            'Key': 'tr:environment-type',
                                            'Value': 'PRODUCTION'
                                        },
                                        {
                                            'Key': 'tr:environment-name',
                                            'Value': 'prod'
                                        },
                                        {
                                            'Key': 'tr:financial-identifier',
                                            'Value': FINANCIAL_ID
                                        },
                                        {
                                            'Key': 'tr:application-asset-insight-id',
                                            'Value': ASSET_ID
                                        },
                                        {
                                            'Key': 'tr:db-resource-name',
                                            'Value': db_resource
                                        },
                                        {
                                            'Key': 'Name',
                                            'Value': secret_name
                                        }
                                    ],

                                    ForceOverwriteReplicaSecret = True)

        if rotate:
            secrets_client.rotate_secret(RotationLambdaARN=lambda_rotation,
                                        RotationRules={
                                            'AutomaticallyAfterDays': ROTATION_INTERVAL,
                                        },
                                        SecretId=secret_name)
    except Exception as e:
        print("An error occurred on service side:", e)



'''
# BEGIN def audit_secrets()
'''
def grep_secrets():

    client = util.get_client(REGION_NAME, SECRETS_MANAGER_SERVICE)

    secrets_list = get_secrets_list(REGION_NAME)
    secret_name = ''
    
    for secrets in secrets_list:

        secret_name = secrets['Name']
    
        if ("qa-us-east-1" in secret_name or "prod-us-east-1" in secret_name) and ("-pg-sm2" in secret_name):

            print(secret_name)

            try:
                secret = client.get_secret_value(SecretId=secret_name)

                response = client.delete_secret(
                                                SecretId=secret_name,
                                                RecoveryWindowInDays=123,
                                                ForceDeleteWithoutRecovery=True|False
)

                secret_string = secret.get('SecretString')

                secret_dict = json.loads(secret_string) 
                
                secret_desc = client.describe_secret(SecretId=secret_name)
                
                description = secret_desc.get('Description')
                tags = secret_desc.get('Tags')
                print(type(tags), tags)

                for tag in tags:
                    if 'tr:db-resource-name' in tag.get('Key'):
                        db_resource = tag.get('Value')
                        print()
                        print(db_resource)
                        break

                lambda_rotation = secret_desc.get('RotationLambdaARN')
                rotate = False

                host =  secret_dict.get('host')
                db_name = secret_dict.get('dbname')
                db_user = secret_dict.get('username')
                db_password = secret_dict.get('password')

                end_pos = len(secret_name) - 1
                secret_name = secret_name[:end_pos]

                manual_secret_create(secret_name, secret_string, db_resource, lambda_rotation, description, rotate)

            except (Exception) as error:
                print()
                # skip deleted secrets
                #print()
                #print(error) 


'''
# BEGIN def delete_secrets()
'''
def delete_secrets(pattern):

    client = util.get_client(REGION_NAME, SECRETS_MANAGER_SERVICE)

    secrets_list = get_secrets_list(REGION_NAME)
    
    for secrets in secrets_list:

        secret_name = secrets['Name']
    
        if ("qa-us-east-1" in secret_name or "prod-us-east-1" in secret_name) and (pattern in secret_name):

            print()
            print(secret_name)

            try:

                response = client.delete_secret(SecretId=secret_name,
                                                RecoveryWindowInDays=30,
                                                ForceDeleteWithoutRecovery=False)
                
                print(response)
            
            except (Exception) as error:
                print()
                # skip deleted secrets
                #print()
                #print(error) 

'''
##
# get_secrets_list()
##
'''
def get_secrets_list(client):

    secrets_list = None
    next_token = None

    try:
        response = client.list_secrets(MaxResults=100)
        secrets_list = response.get('SecretList')
        next_token = response.get('NextToken')

        while(next_token):
            response = client.list_secrets(MaxResults=100, NextToken=next_token)
            secrets_list.extend(response.get('SecretList'))
            next_token = response.get('NextToken')

        return secrets_list
    
    except ClientError as e:
        raise Exception("boto3 client error in get_secrets: " + e.__str__())
    except Exception as e:
        raise Exception("Unexpected error in get_secrets: " + e.__str__()) 

##
# secrets.py MAINLINE
##

print("secrets.py 'main': Oh. Hai!")

#create_secrets(False)
#grep_secrets()
#delete_secrets('z-')
#create_secrets_hvr(False)
#disable_auto_rotation()

'''
secrets_client = util.get_client(REGION_NAME, SECRETS_MANAGER_SERVICE)

secrets = get_secrets_list(REGION_NAME)
description = "Novus Doc Admin RDS Role Secret"

for secret in secrets:

    secret_name = secret['Name']
    lambda_rotation = None
    rotate = False

    if 'prod-us-east-1-pg-sm' in secret_name and \
        'doc-g' in secret_name and \
        'docloc' not in secret_name and \
        'dlc' not in secret_name:

        print(secret_name)
        
        db_resource = secret_name[8:]
        pos = db_resource.find('-prod-')
        db_resource = db_resource[:pos-1]
        new_secret_name = 'a207947-' + db_resource + '-prod-doc-admin-use1'
        db_resource = db_resource.replace('-', '.')
        
        print('secret_name', secret_name, 'db_resource:', db_resource)
        print(secret)

        secret_info = get_secret_value(secret_name)

        secret_dict = json.loads(secret_info)

        host =  secret_dict.get('host')
        db_name = secret_dict.get('dbname')
        db_user = secret_dict.get('username')
        db_password = secret_dict.get('password')
        port = secret_dict.get('port')
        cluster_id = secret_dict.get('dbClusterIdentifier')

        secret_string = build_secret_string('novusdocadmin', 
                                            'asadmin', 
                                            host, 
                                            port, 
                                            db_name,
                                            cluster_id     
                                        )

        manual_secret_create(new_secret_name, secret_string, db_resource, lambda_rotation, description, rotate)

    else:
        #print('\tdb_resource:', db_resource)
        continue
'''

print("secrets.py 'main': Bai!")
