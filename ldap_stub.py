__author__ = "Jeremy Leese | jeremy.leese@thomsonreuters.com | Technology - Product Eng - Content Platforms"
__copyright__ = "Copyright© (C) 2022 Thomson Reuters. All Rights Reserved."
__version__ = "0.01"

import ldap 
from ldif import LDIFParser,LDIFWriter
import ldap.modlist as modlist
import json
import boto3
from botocore.exceptions import ClientError

ldap_py = ldap.initialize('ldap://localhost:389')
ldap_py.simple_bind_s("cn=novusprod,cn=users,ou=novusaws,o=westgroup.com", "SrF7330ngErf$tdm3rdeel9")

baseDN = "cn=Resources,cn=novusprod,ou=novusaws,o=westgroup.com"
searchScope = ldap.SCOPE_SUBTREE
retrieveAttributes = None  ## ironicaly, retrieve all attributes
searchFilter = "(objectClass=wgResource)"

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

'''
#################
"M A I N L I N E"
#################
'''

try:
    secrets_client = util.get_client(REGION_NAME, SECRETS_MANAGER_SERVICE)

    secrets = get_secrets_list(REGION_NAME)
    description = "Novus Doc Admin RDS Role Secret"

    for secret in secrets:

        secret_name = secret['Name']
        lambda_rotation = None
        rotate = False

        if 'prod-us-east-1-pg-sm' in secret_name:
            print('FOUND:', secret_name)

except(Exception) as e:
    print(e)
finally:
    print('EXIT')
try:
      
    ldap_result_id = ldap_py.search(baseDN, searchScope, searchFilter, retrieveAttributes)
    result_set = []

    while 1:
        
        result_type, result_data = ldap_py.result(ldap_result_id, 0)

        if (result_data == []):
            break
        else:
            if result_type == ldap.RES_SEARCH_ENTRY:
                result_set.append(result_data)

    for entry in result_set:
        count1 = count1 + 1

        dn = entry[0][0]
        entry_dict = entry[0][1]
        cn = entry_dict.get('cn')[0].decode('utf-8')
        print(entry_dict)

        # do work here
        print()
        print('cn:', cn)
    
        if 'read' in cn >= 0 and '-ro-' in db_host:

            print('\tdn:', dn)
            print('\twgDatabaseHost:', db_host)

            db_host = db_host.replace('-ro', '')

            ldif = modlist.modifyModlist({'wgDatabaseHost': entry_dict['wgDatabaseHost'][0]},{'wgDatabaseHost': [db_host.encode()]})
            ldap_py.modify_s(dn,ldif)
        
except(ldap.LDAPError) as e:
    print(e)
finally:
    print('EXIT')