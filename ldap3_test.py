from ldap3 import Server, Connection, ALL, MODIFY_REPLACE
import ldap
import logging
from ldap3.utils.log import set_library_log_activation_level
from ldap3.utils.log import set_library_log_detail_level, get_detail_level_name, set_library_log_hide_sensitive_data, EXTENDED
import os
from datetime import date

def ldap3t():
    server = Server('ldap://localhost:389', get_info=ALL)
    conn = Connection(server, 'cn=novusclient,cn=users,ou=novusaws,o=westgroup.com', 'r4raEasdoutTn0', auto_bind=True)
    conn.search('cn=client,ou=novusaws,o=westgroup.com', '(objectClass=wgAccessibleDatastore)')

    conn.entriesserver = Server('ldap://localhost:389', get_info=ALL)
    conn = Connection(server, 'cn=novusclient,cn=users,ou=novusaws,o=westgroup.com', 'r4raEasdoutTn0', auto_bind=True)
    conn.search('cn=client,ou=novusaws,o=westgroup.com', '(objectClass=wgAccessibleDatastore)')

    print(conn.entries)

'''
# update_datastore_ptrs_oneoff(ldap_py, ldap_conn, log, commit)
'''
def update_datastore_ptrs_oneoff(ldap_py, ldap_conn, log, commit):
   print('update_datastore_ptrs_oneoff(): BEGIN')
   print('update_datastore_ptrs_oneoff(): BEGIN', file=log)

   out_log = open('client_upd_dsp_0122.log', 'w')
   print('output log:', out_log)

   #commit = False
   count = 0
   
   #baseDN = "cn=dev,ou=novusaws,o=westgroup.com"
   #baseDN = "cn=client,ou=novusaws,o=westgroup.com"
   baseDN = "cn=client,ou=novusaws,o=westgroup.com"
   searchScope = ldap.SCOPE_SUBTREE
   ## retrieve all attributes - again adjust to your needs - see documentation for more options
   retrieveAttributes = None
   searchFilter = "(objectClass=wgAccessibleDatastore)"

   #resource_dict = util.get_resource_dict()

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

      count = 0
      op_count = 0

      for entry in result_set:

         dn = entry[0][0]
         entry_dict = entry[0][1]
         cn = entry_dict.get('cn')[0].decode('utf-8')
         dsp = entry_dict.get('wgDataStorePtr')[0].decode('utf-8')
         rsc = entry_dict.get('wgResourceName')[0].decode('utf-8')
         
         rsc = rsc.lower()
         #cn = cn.lower()

         #if dsp.find('cn=resources') or dsp.find('cn=Resources'):

         #"wwlkccitingrefss":  "norm.intl.01",

         if 'wwlkcciterefss' in cn:

            #print(rsc, dn, dsp)
            op_count = op_count + 1

            #if dsp.find('wkrnims') >= 0:
            #   print('BREAK')

            aws_rsc = 'norm.intl.01'
            dsp_split = dsp.split('cn=') 
            base_rsc =  dsp_split[len(dsp_split) - 2]
            base_rsc = base_rsc[:len(base_rsc) - 1]
            base_rsc = base_rsc.lower()

            infra_rsc = False

            print('    dsp:', dsp, file=log)
            print('     cn:', cn, file=log)
            print('aws_rsc:', aws_rsc, file=log)
            print('    rsc:', rsc, file=log)
            print(" ", file=log)

            '''
            print('    dsp:', dsp)
            print('     cn:', cn)
            print('aws_rsc:', aws_rsc)
            print('    rsc:', rsc)
            print(" ")
            '''

            rsc_typ = cn[cn.find('.'):]

            aws_rsc_b = aws_rsc
            bucket = aws_rsc + rsc[len(base_rsc):]

            is_bucket = True
            skip = False


            if is_bucket and not skip:
               if rsc_typ.find('master.u') >= 0:
                  new_dsp = 'cn=' + aws_rsc_b + 'a.update,cn=' + bucket + ',cn=' + aws_rsc + ',cn=Resources'
                  aws_rsc = bucket

               elif rsc_typ.find('masterA.u') >= 0:
                  new_dsp = 'cn=' + aws_rsc_b + 'a.update,cn=' + bucket + ',cn=' + aws_rsc + ',cn=Resources'
                  aws_rsc = bucket

               elif rsc_typ.find('.Site-A.u') >= 0:
                  new_dsp = 'cn=' + aws_rsc_b + 'a.update,cn=' + bucket + ',cn=' + aws_rsc + ',cn=Resources'
                  aws_rsc = bucket

               elif rsc_typ.find('.Site-A.r') >= 0:
                  new_dsp = 'cn=' + aws_rsc_b + 'a.read,cn=' + bucket + ',cn=' + aws_rsc + ',cn=Resources'
                  aws_rsc = bucket

               elif rsc_typ.find('.Site-B.u') >= 0:
                  new_dsp = 'cn=' + aws_rsc_b + 'b.update,cn=' + bucket + ',cn=' + aws_rsc + ',cn=Resources'
                  aws_rsc = bucket
               
               elif rsc_typ.find('.Site-B.r') >= 0:
                  new_dsp = 'cn=' + aws_rsc_b + 'b.read,cn=' + bucket + ',cn=' + aws_rsc + ',cn=Resources'
                  aws_rsc = bucket

               elif rsc_typ.find('master.r') >= 0:
                  new_dsp = 'cn=' + aws_rsc_b + 'a.read,cn=' + bucket + ',cn=' + aws_rsc + ',cn=Resources'
                  aws_rsc = bucket
                  
               elif rsc_typ.find('ret-masterA.r') >= 0:
                  new_dsp = 'cn=' + aws_rsc_b + 'a.read,cn=' + bucket + ',cn=' + aws_rsc + ',cn=Resources'
                  aws_rsc = bucket
               elif rsc_typ.find('slave.slave.r') >= 0:
                  new_dsp = 'cn=' + aws_rsc_b + 'a.read,cn=' + bucket + ',cn=' + aws_rsc + ',cn=Resources'
                  aws_rsc = bucket
                  aws_cn = rsc + 's.read'
               elif rsc_typ.find('slave.r') >= 0:
                  new_dsp = 'cn=' + aws_rsc_b + 'a.read,cn=' + bucket + ',cn=' + aws_rsc + ',cn=Resources'
                  aws_rsc = bucket
                  aws_cn = rsc + 's.read'
               
               else:
                  print('rsc_typ NOT FOUND:', rsc_typ)
                  continue

            elif not skip:
               if rsc_typ.find('master.u') >= 0:
                  if infra_rsc:
                     new_dsp = 'cn=' + aws_rsc + '.01a.update,cn=' + aws_rsc + ',cn=Resources'   
                  else: 
                     new_dsp = 'cn=' + aws_rsc + 'a.update,cn=' + aws_rsc + ',cn=Resources'

                  aws_rsc = bucket

               elif rsc_typ.find('master.1.u') >= 0 and infra_rsc:
                  if infra_rsc:
                     new_dsp = 'cn=' + aws_rsc + '.01a.update,cn=' + aws_rsc + ',cn=Resources'   
                  else: 
                     new_dsp = 'cn=' + aws_rsc + 'a.update,cn=' + aws_rsc + ',cn=Resources'
                  
                  aws_rsc = bucket
               
               elif rsc_typ.find('master.2.u') >= 0:
                  if infra_rsc:
                     new_dsp = 'cn=' + aws_rsc + '.01b.update,cn=' + aws_rsc + ',cn=Resources'   
                  else: 
                     new_dsp = 'cn=' + aws_rsc + 'b.update,cn=' + aws_rsc + ',cn=Resources'
                  
                  aws_rsc = bucket

               elif rsc_typ.find('masterA.u') >= 0:
                  if infra_rsc:
                     new_dsp = 'cn=' + aws_rsc + '.01a.update,cn=' + aws_rsc + ',cn=Resources'   
                  else: 
                     new_dsp = 'cn=' + aws_rsc + 'a.update,cn=' + aws_rsc + ',cn=Resources'

                  aws_rsc = bucket

               elif rsc_typ.find('.Site-A.u') >= 0:

                  if infra_rsc:
                     new_dsp = 'cn=' + aws_rsc + '.01a.update,cn=' + aws_rsc + ',cn=Resources'   
                  else: 
                     new_dsp = 'cn=' + aws_rsc + 'a.update,cn=' + aws_rsc + ',cn=Resources'

                  aws_rsc = bucket

               elif rsc_typ.find('.Site-A.r') >= 0:

                  if infra_rsc:
                     new_dsp = 'cn=' + aws_rsc + '.01a.read,cn=' + aws_rsc + ',cn=Resources'   
                  else: 
                     new_dsp = 'cn=' + aws_rsc + 'a.read,cn=' + aws_rsc + ',cn=Resources'
                  
                  aws_rsc = bucket

               elif rsc_typ.find('.Site-B.u') >= 0:

                  if infra_rsc:
                     new_dsp = 'cn=' + aws_rsc + '.01b.update,cn=' + aws_rsc + ',cn=Resources'   
                  else: 
                     new_dsp = 'cn=' + aws_rsc + 'b.update,cn=' + aws_rsc + ',cn=Resources'
                  
                  aws_rsc = bucket
               
               elif rsc_typ.find('.Site-B.r') >= 0:
               
                  if infra_rsc:
                     new_dsp = 'cn=' + aws_rsc + '.01b.read,cn=' + aws_rsc + ',cn=Resources'   
                  else: 
                     new_dsp = 'cn=' + aws_rsc + 'b.read,cn=' + aws_rsc + ',cn=Resources'
                  
                  aws_rsc = bucket

               elif rsc_typ.find('master.r') >= 0:

                  if infra_rsc:
                     new_dsp = 'cn=' + aws_rsc + '.01a.read,cn=' + aws_rsc + ',cn=Resources'   
                  else: 
                     new_dsp = 'cn=' + aws_rsc + 'a.read,cn=' + aws_rsc + ',cn=Resources'
                  
                  aws_rsc = bucket
                  
               elif rsc_typ.find('ret-masterA.r') >= 0:

                  if infra_rsc:
                     new_dsp = 'cn=' + aws_rsc + '.01a.read,cn=' + aws_rsc + ',cn=Resources'   
                  else: 
                     new_dsp = 'cn=' + aws_rsc + 'a.read,cn=' + aws_rsc + ',cn=Resources'
                  
                  aws_rsc = bucket
               
               elif rsc_typ.find('slave.r') >= 0:
                  
                  if infra_rsc:
                     new_dsp = 'cn=' + aws_rsc + '.01b.read,cn=' + aws_rsc + ',cn=Resources'   
                  else: 
                     new_dsp = 'cn=' + aws_rsc + 'z.read,cn=' + aws_rsc + ',cn=Resources'
                  
                  aws_rsc = bucket
               
               elif rsc_typ.find('slave.u') >= 0:
                  
                  if infra_rsc:
                     new_dsp = 'cn=' + aws_rsc + '.01b.update,cn=' + aws_rsc + ',cn=Resources'   
                  else: 
                     new_dsp = 'cn=' + aws_rsc + 'z.read,cn=' + aws_rsc + ',cn=Resources'
                  
                  aws_rsc = bucket

               else:
                  print('rsc_typ NOT FOUND:', rsc_typ)
                  continue   
            else:
               print('SKIP DOUBLE SLAVE OR DLC')

            if not skip:

                # perform the Modify operation
                if commit:

                    print('dn:', dn)
                    print('dsp:', new_dsp)
                    print('rsc', aws_rsc)

                    ldap_conn.modify(dn,
                                    {'wgDataStorePtr': [(MODIFY_REPLACE, [new_dsp])],
                                     'wgResourceName': [(MODIFY_REPLACE, [aws_rsc])]
                                    })

                    print(ldap_conn.result)
               
                '''
                dsp_ldif = modlist.modifyModlist({'wgDataStorePtr': dsp.encode('utf-8')}, {'wgDataStorePtr': [new_dsp.encode('utf-8')]})

                print('\t', dn)
                print('\t\t', dsp_ldif)
                print(dn, file=out_log)
                print('\t\t', dsp_ldif, file=out_log)

                if(commit):
                    ldap_py.modify_s(dn, dsp_ldif)
                
                count = count + 1

                res_ldif = modlist.modifyModlist({'wgResourceName': rsc.encode('utf-8')}, {'wgResourceName': [(aws_rsc).encode('utf-8')]})
                print('\t\t',res_ldif)
                print('\t\t', res_ldif, file=out_log)

                if(commit):
                    ldap_py.modify_s(dn, res_ldif)
                
                
                cn_ldif = modlist.modifyModlist({'cn': cn.encode('utf-8')}, {'cn': [(aws_cn).encode('utf-8')]})
                print(cn_ldif)
                print('\t', cn_ldif, file=out_log)
                
                if commit:
                    ldap_py.modify_s(dn, cn_ldif)
                '''
         else:
            ph = 'place holder'

            #if dn.find('wwlkc') >= 0:
            #   print('skipping rsc, \'resources\' not matched:', rsc,'dn:', dn, 'dsp:', dsp)

   except(ldap.LDAPError) as e:
      print(e)
   finally:
      print('update_datastore_ptrs_oneoff(): END')
      print('update_datastore_ptrs_oneoff(): END', file=log)

###
# "Mainline"
###
log_file = os.getcwd() + "\\log\\prod_adsp_audit." + str(date.today()) + ".log"
log = open(log_file, 'w')
print(log)


ldap_py = ldap.initialize('ldap://localhost:389')
ldap_py.simple_bind_s("cn=novusclient,cn=users,ou=novusaws,o=westgroup.com", "r4raEasdoutTn0")

logging.basicConfig(filename='client_application.' + str(date.today()) + '.log', level=logging.DEBUG)
set_library_log_activation_level(EXTENDED)
set_library_log_detail_level(EXTENDED)
set_library_log_hide_sensitive_data(True)

# define the server
#server = Server('a207947-novus-client-use1ldap.1667.aws-int.thomsonreuters.com:636', get_info=ALL) # define an unsecure LDAP server, requesting info on DSE and schema
server = Server('ldap://localhost:389', get_info=ALL) # define an unsecure LDAP server, requesting info on DSE and schema

# define the connection
conn = Connection(server, 'cn=novusclient,cn=users,ou=novusaws,o=westgroup.com', 'r4raEasdoutTn0', auto_bind=True)
conn.bind()

update_datastore_ptrs_oneoff(ldap_py, conn, log, True)

'''
dn = 'cn=wwlkcciterefss1.master.u,cn=CleanupServ,cn=client,ou=novusaws,o=westgroup.com'
dsp = 'cn=norm.intl.01a.update,cn=norm.intl.011,cn=norm.intl.01,cn=Resources'
rsc = 'norm.intl.011'

# perform the Modify operation
conn.modify(dn,
            {'wgDataStorePtr': [(MODIFY_REPLACE, [dsp])],
            'wgResourceName': [(MODIFY_REPLACE, [rsc])]
            })

print(conn.result)
'''