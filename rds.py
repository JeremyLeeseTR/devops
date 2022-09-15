__author__ = "Jeremy Leese | jeremy.leese@thomsonreuters.com | Technology - Product Eng - Content Platforms"
__copyright__ = "Copyright© (C) 2022 Thomson Reuters. All Rights Reserved."
__version__ = "1.0"

import boto3
from botocore.exceptions import ClientError
import util
import builtins

US_EAST_1 = "us-east-1"
RDS_SERVICE = "rds"
PROD = "PROD"
CLIENT = "CLIENT"

##
#   BEGIN DEF enableEnhancedLogging(int monitoring_interval)
#
#   turn on enhanced logging for novus dbs
#   Valid Values: 0, 1, 5, 10, 15, 30, 60
##
def enableEnhancedLogging(client, monitoring_interval):

    describe_instances_response = client.describe_db_instances()
    
    db_instances_dict = describe_instances_response.get("DBInstances") 
    
    for k in db_instances_dict:
        db_dict = db_instances_dict[k]

        print("")
        print(db_dict.get("DBName"))
        print(db_dict.get("DBInstanceIdentifier"))
        
        db_inst_id = db_dict.get("DBInstanceIdentifier")
        
        if monitoring_interval > 0:
            try:
                modify_response = client.modify_db_instance(
                        DBInstanceIdentifier=db_inst_id,
                        ApplyImmediately=True,
                        MonitoringInterval=monitoring_interval,
                        MonitoringRoleArn="arn:aws:iam::255679434152:role/a207947-novus-enhanced-rds-enhanced-monitoring-role"
                )
            except ClientError as e:
                util.handle_aws_error(e)
            else:
                print(modify_response)

        else:
            # if monitor interval is 0 we are turning enh log off. do not include role arn
            try:
                modify_response = client.modify_db_instance(
                        DBInstanceIdentifier=db_inst_id,
                        ApplyImmediately=True,
                        MonitoringInterval=monitoring_interval
                )
            except ClientError as e:
                util.handle_aws_error(e)
            else:
                print(modify_response)

# END DEF enableEnhancedLogging(int monitoring_interval)

##
#   BEGIN DEF get_db_parameters()
##
def get_db_cluster_parameters(client, db_parameter_group_name):

    try:
        
        response = client.describe_db_cluster_parameters(DBParameterGroupName=db_parameter_group_name, MaxRecords=100)
        
        db_parms = response.get('Parameters')
        marker = response.get('Marker')

        while(marker):

            response = client.describe_db_cluster_parameters(DBParameterGroupName=db_parameter_group_name, MaxRecords=100, Marker=marker)

            marker = response.get('Marker')
            temp_parms = response.get('Parmeters')

            if temp_parms:

                db_parms.extend()

    except ClientError as e:
        util.handle_client_error(e)
    else:
        return db_parms

# END DEF get_db_parameters()

##
#   BEGIN DEF get_db_cluster_parameter_groups(client  - AWS RDS Client) 
##
def get_db_cluster_parameter_groups(client):

    try:
        
        response = client.describe_db_cluster_parameter_groups(MaxRecords=100)
        
        db_parm_groups = response.get('DBClusterParameterGroups')
        marker = response.get('Marker')
        
        while(marker):

            response = client.describe_db_cluster_parameter_groups(MaxRecords=100, Marker=marker)

            marker = response.get('Marker')
            db_parm_groups.extend(response.get('DBClusterParameterGroups'))

    except ClientError as e:
        util.handle_client_error(e)
    else:
        return db_parm_groups

# END DEF get_db_cluster_parameter_groups(client  - AWS RDS Client) 

##
#   BEGIN DEF modify_db_cluster_parameter(parm_group_name, parm_key, parm_value, client)
##
def modify_db_cluster_parameter(client, parm_group_name, parm_key, parm_value):
    print()
    print('parm_group_name:', parm_group_name)
    print('parm_key', parm_key)
    print('parm_value:', parm_value)

    response = client.modify_db_cluster_parameter_group(DBClusterParameterGroupName=parm_group_name,
                                                        Parameters=[
                                                            {
                                                                'ApplyMethod': 'immediate',
                                                                'ParameterName': parm_key,
                                                                'ParameterValue': parm_value
                                                            }
                                                        ])

    print(response)

# END DEF modify_db_cluster_parameter(parm_group_name, parm_key, parm_value, client)

##
#   BEGIN DEF list get_db_instances(client)
#   client: boto rds service client  
##
def get_db_instances(client):

    db_instances = []
    next_token = None

    try:
        
        response = client.describe_db_instances() 
        db_instances = response.get('DBInstances')
        next_token = response.get('NextToken')

        while next_token:
            
            response = client.describe_db_instances(NextToken=next_token)
            
            db_instances.extend(response.get('DBInstances'))
            next_token = response.get('NextToken')

        return db_instances
    
    except ClientError as e:
        raise Exception("boto3 client error in rds.get_db_instances: " + e.__str__())
    except Exception as e:
        raise Exception("Unexpected error in rds.get_db_instances: " + e.__str__()) 

# END DEF list get_db_instances(client)

##
#   BEGIN DEF modify_instance_class(client, instance_id, commit)
##
def modify_instance_class(client, instance_id, instance_class, commit):
    
    if commit:
        response = client.modify_db_instance(DBInstanceIdentifier=instance_id,
                                             DBInstanceClass=instance_class)

    print(response)

#   END DEF modify_instance_class(client, instance_id, commit)