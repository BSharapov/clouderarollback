#!/home/playtika/miniconda3/bin/python

import cm_client
from cm_client.rest import ApiException
from pprint import pprint
import time

def wait(cmd, timeout=None):
    SYNCHRONOUS_COMMAND_ID = -1
    if cmd.id == SYNCHRONOUS_COMMAND_ID:
        return cmd
    SLEEP_SECS = 5
    if timeout is None:
        deadline = None
    else:
        deadline = time.time() + timeout
    try:
        cmd_api_instance = cm_client.CommandsResourceApi(api_client)
        while True:
            cmd = cmd_api_instance.read_command(int(cmd.id))
            #pprint(cmd)
            if not cmd.active:
                return cmd
            if deadline is not None:
                now = time.time()
                if deadline < now:
                    return cmd
                else:
                    time.sleep(min(SLEEP_SECS, deadline - now))
            else:
                time.sleep(SLEEP_SECS)
    except ApiException as e:
        val=1
        #print ("Exception reading and waiting for command %s\n" %e)

# Parameter value
paramVal = 128
paramName = 'mapreduce.map.memory.mb'

# Configure HTTP basic authorization: basic
cm_client.configuration.username = 'admin'
cm_client.configuration.password = 'admin'

# Create an instance of the API class
api_host = 'http://localhost'
port = '7180'
api_version = 'v33'
api_url = api_host + ':' + port + '/api/' + api_version
api_client = cm_client.ApiClient(api_url)
cluster_api_instance = cm_client.ClustersResourceApi(api_client)

# This lists all clusters, so if you have more than one, set "cluster_name" to it.  Otherwise, last one wins
api_response = cluster_api_instance.read_clusters(view='SUMMARY')
for cluster in api_response.items:
    cluster_name = cluster.name

# Get a list of all services and set myserive if the service type is "YARN"
services_api_instance = cm_client.ServicesResourceApi(api_client)
services = services_api_instance.read_services(cluster.name, view='FULL')
for service in services.items:
    if service.type == 'YARN':
        myservice = service

# Get a list of roles and get the GATEWAY type
roles_api_instance = cm_client.RolesResourceApi(api_client)
roles = roles_api_instance.read_roles(cluster_name, myservice.name)
for role in roles.items:
    if role.type == 'GATEWAY':
        myrole = role
# default is summary... this is only relevant if printing out information since full shows all values
# regardless if they have a non-default value or not
view = 'full'

# Uses RoleConfigGroupsResourceApi to retrieve all YARN role config groups
# Sets yarnGatewayBase to be the name of the role config group we want to update
rcg_api_instance = cm_client.RoleConfigGroupsResourceApi(api_client)
rcg_api_response = rcg_api_instance.read_role_config_groups(cluster_name, myservice.name)
#pprint(rcg_api_response)
for cfg in rcg_api_response.items:
  if cfg.name == "yarn-GATEWAY-BASE":
       yarnGatewayBase = cfg.name

# read the config and iterate over each config till we find the one we want
# print out the config before update
yarn_gateway_base = rcg_api_instance.read_config(cluster_name, yarnGatewayBase, myservice.name, view=view)
for config in yarn_gateway_base.items:
    if config.related_name == paramName:
       config_to_update = config.name

# Set message and new config values where "value" is what we want the new value to be
# use update_config() to update the value
message = 'update of ' + paramName
new_config = cm_client.ApiConfig(name=config_to_update, value=paramVal)
new_config_list = cm_client.ApiConfigList([new_config])
try:
    # Updates the config for the given role config group.
    res = rcg_api_instance.update_config(cluster_name, yarnGatewayBase, myservice.name, message=message, body=new_config_list)
    #pprint(res)
except ApiException as e:
    print("Exception when calling RoleConfigGroupsResourceApi->update_config: %s\n" % e)

clusters_api_instance = cm_client.ClustersResourceApi(api_client)
restart_args = cm_client.ApiRestartClusterArgs(restart_only_stale_services=True, redeploy_client_configuration=True)
restart_command = clusters_api_instance.restart_command(cluster_name, body=restart_args)
wait(restart_command)
