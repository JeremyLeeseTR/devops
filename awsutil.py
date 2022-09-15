__author__ = "Jeremy Leese | jeremy.leese@thomsonreuters.com | Technology - Product Eng - Content Platforms"
__copyright__ = "Copyright© (C) 2022 Thomson Reuters. All Rights Reserved."
__version__ = "ALPHA 0.1"

import sys
import os
from pickle import TRUE
from datetime import date
import ldap

import dbaudit
import pg
import util
import ldaputil

US_EAST_1 = "us-east-1"
RDS_SERVICE = "rds"
RG6_X2L_CLASS = 'db.r6g.2xlarge'

# supported functions
DBAUDIT = 'dbaudit'
TRGAUDIT = 'trgaudit'
TRGADD = 'trgadd'
SCHAUDIT = 'schaudit'

COMMIT = True
NO_COMMIT = False

##
#  BEGIN DEF resize_db_audit()
##
def resize_db_audit():

    #rds_client = util.get_client(US_EAST_1, RDS_SERVICE)
    rds_client = "this is broken"
    #db_instances = rds.get_db_instances(rds_client)
    db_instances = "this is also broken"

    if db_instances is not None:

        for instance in db_instances:

            cluster_id = instance['DBClusterIdentifier']
            instance_id = instance['']
            instance_class = instance['DBInstanceClass']
            
            if '-qa-' in cluster_id and 'auth' in cluster_id:

                print('    Cluster ID:', cluster_id)
                print('Instance Class:', instance_class)
                print()

                if RG6_X2L_CLASS in instance_class:
                    print('x2l')
                    #rds.modify_instance_class(rds_client, 'instance_id', instance_class)

# END DEF resize_db_audit()

##
#  BEGIN DEF aws_test
##
def aws_test(func, db_filter, port, commit, log):

    print()
    util.get_client(util.USE_REGION, util.SM_SERVICE)

    if DBAUDIT in func:
        dbaudit.audit_dbs('nims', 'novusr1', 'dbaudit_nims_0330.log')
    elif TRGAUDIT in func:
        pg.audit_trigger_functions(db_filter, commit)
    elif TRGADD in func:
        pg.add_trigger_functions(db_filter, port, NO_COMMIT)
    elif SCHAUDIT in func:
        pg.map_schema_locations(db_filter, log)
    else:
        print('Function', func, ' not supported. Exit.')
        return

# END DEF aws_test

###
# aws "mainline"
###

args = sys.argv

if len(args) > 1:
    print('Using argv.')
    db_filter = args[1]
    port = args[2]
    
else:
    print('Using hard code.')
    db_filter = 'nims'

log_file = os.getcwd() + "\\log\\prod_adsp_audit." + str(date.today()) + ".log"
log = open(log_file, 'w')
print(log)

ldap_py = ldap.initialize('ldap://localhost:389')
#ldap_py.simple_bind_s("cn=novusclient,cn=users,ou=novusaws,o=westgroup.com", "r4raEasdoutTn0")
ldap_py.simple_bind_s("cn=novusprod,cn=users,ou=novusaws,o=westgroup.com", "SrF7330ngErf$tdm3rdeel9")

#pg.update_trigger_functions('nims', True)
pg.grant_user_access('metadoc-ha')

#pg.create_doc_admin_user(False)

#pg.print_db_tables('nims')

#pg.populate_migration_table(True)

#ldaputil.update_datastore_ptrs(ldap_py, log, True)
#ldaputil.update_datastore_ptrs_oneoff(ldap_py, log, True)

#pg.map_schema_locations("doc-w", log)
#pg.grant_user_access("doc-shared-01")

#aws_test(SCHAUDIT, 'doc-load', '', True, log)
#aws_test(DBAUDIT)
#aws_test(TRGAUDIT, db_filter, '8891', False)
#aws_test(TRGADD, db_filter, 4103)

#pg.populate_migration_table(False)
#pg.grant_user_access('loadqueue')



