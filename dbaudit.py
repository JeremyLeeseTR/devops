import pg
import secrets
import base64
import boto3
import psycopg
import json
import os
import subprocess

##
#   BEGIN DEF audit_dbs(log)
##
def audit_dbs(db_match, db_user, log_name):
    
    log = open(log_name, 'w')

    region='us-east-1'
    cur = None
    conn = None
    tunnel_open = False

    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region)

    secrets_response = secrets.get_secrets_list(client)

    for secret in secrets_response:

        secret_name = secret['Name']

        # skip if db not in subset being validated
        if db_match not in secret_name:
            continue

        if secret_name.find('qa-us-east-1-pg-sm') >= 0:

            response = client.get_secret_value(SecretId=secret_name)

            # Decrypts secret using the associated KMS CMK.
            # Depending on whether the secret is a string or binary, one of these fields will be populated.
            if 'SecretString' in response:
                secret_s = response['SecretString']
                #print('\tsecret_s:', secret_s)

            elif 'SecretBinary' in response:
                secret_b = base64.b64decode(response['SecretBinary'])
                #print('\tsecret_b:', secret_b)
            else:
                print('\tSecret String NOT FOUND')
                
                print(file=log)
                print('Secret String NOT FOUND', file=log)
                print(file=log)

            secret_dict = json.loads(secret_s) 

            cluster_id = secret_dict['dbClusterIdentifier'] 
            host = secret_dict['host']
            db_name = secret_dict['dbname']
            user = secret_dict['username']
            password = secret_dict['password']
            #port = secret_dict['port']
            port = '8898'

            # ssh tunnel to aws pg db
            tunnel_cmd = pg.OPEN_SSH_TUNNEL + host

            #print()
            print("Exec CMD: " + tunnel_cmd)
            os.system(tunnel_cmd)
            tunnel_open = True

            #print()
            #print('Connecting to the PostgreSQL database ', db_name, user, password, 'localhost', port, '...')

            try:
                conn = psycopg.connect(dbname=db_name, user=user, password=password, host="localhost", port=port)
            except(psycopg.DatabaseError) as error:
                print(error)
                
                print(file=log)
                print(error, file=log)
                print(file=log)

                if tunnel_open:
                    tunnel_cmd = pg.CLOSE_SSH_TUNNEL + host
                    os.system(tunnel_cmd)
                    print('Database tunnel closed.')
                    tunnel_open = False

                continue

            try: 
                cur = conn.cursor()
                cur.execute("SELECT schema_name FROM information_schema.schemata WHERE schema_name LIKE \'%pub%\'")

                rows = cur.fetchall() 

                print()
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")              
                print('FOUND:', db_name, '|', rows[0])
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                print()

                print(file=log)
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!", file=log)              
                print('FOUND:', db_name, '|', rows[0], file=log)
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!', file=log)
                print(file=log)

                #for row in rows:
                    #print(db_name + '|' + row[0])
                    #print(db_name + '|' + row[0],file=log)

            except (Exception, psycopg.DatabaseError) as error:
                print(error)
                print(error, file=log)

                if tunnel_open:
                    tunnel_cmd = pg.CLOSE_SSH_TUNNEL + host
                    os.system(tunnel_cmd)
                    print('Database tunnel closed.')
                    tunnel_open = False

                continue
            finally:
                if cur is not None:
                    cur.close()
                    cur = None
                    print('Database cursor closed.')
                if conn is not None:
                    conn.close()
                    conn = None
                    print('Database connection closed.')
                if tunnel_open:
                    tunnel_cmd = pg.CLOSE_SSH_TUNNEL + host
                    os.system(tunnel_cmd)
                    print('Database tunnel closed.')
                    tunnel_open = False

#   END DEF audit_dbs(log)