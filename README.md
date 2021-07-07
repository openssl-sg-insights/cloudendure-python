# cloudendure
© 2021 CloudEndure All rights reserved

# General
Request authentication in CloudEndure's API is done using session cookies.
A session cookie is returned upon successful execution of the \"login\" method.
This value must then be provided within the request headers of all subsequent API requests.

## Errors
Some errors are not specifically written in every method since they may always return.
Those are:
1) 401 (Unauthorized) - for unauthenticated requests.
2) 405 (Method Not Allowed) - for using a method that is not supported (POST instead of GET).
3) 403 (Forbidden) - request is authenticated, but the user is not allowed to access.
4) 422 (Unprocessable Entity) - for invalid input.

## Formats
All strings with date-time format are according to RFC3339.

All strings with \"duration\" format are according to ISO8601.
For example, a full day duration can be specified with \"PNNNND\".


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 5
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://bit.ly/2T54hSc](https://bit.ly/2T54hSc)

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/craigmonson/2ndWatch/python-cloudendure.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/craigmonson/2ndWatch/python-cloudendure.git`)

Then import the package:
```python
import cloudendure
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cloudendure
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import cloudendure
from cloudendure.api import authentication_api
from cloudendure.api import project_api
# since the api def doesn't have this defined, we'll rename it.
from cloudendure.models import InlineObject1 as LoginModel

# bare, base api client
api_client = cloudendure.ApiClient()

# we need to auth before anything else... if we don't have a session...
auth_client = authentication_api.AuthenticationApi(api_client)
# your token can be found in the 'Setup & Info' page, in the 'OTHER SETTINGS' tab under the 'API Token' section.
login_model = LoginModel(user_api_token="xxxx-yyyy-zzzz...")
auth_client.login_post(login_model)
# In order to set the proper session cookie and headers:
api_client.set_auth_from_last_response()

# you can get both parts of the auth to store for later use (so you don't have to log in again)
# stored in the header as 'X-XSRF-TOKEN'
xsrf_token = api_client.xsrf_token

# the session cookie
cookie = api_client.cookie

# no need to log back in if you've got valid token and session cookie
new_api_client = cloudendure.ApiClient()
new_api_client.set_session_auth(xsrf_token, cookie)

# now... do something useful
project_client = project_api.ProjectApi(new_api_client) # or api_client
response = project_client.projects_get()
print(response.items)
project_id = response.items[0].id

machine_client = machines_api.MachinesApi(api_client) # or new_api_client
response = machine_client.projects_project_id_machinies_get(project_id)
print(response.items)
```

## Documentation for API Endpoints



All URIs are relative to *https://console.cloudendure.com/api/latest*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**accounts_account_id_get**](docs/AccountApi.md#accounts_account_id_get) | **GET** /accounts/{accountId} | Get Account information
*ActionsApi* | [**projects_project_id_jobs_get**](docs/ActionsApi.md#projects_project_id_jobs_get) | **GET** /projects/{projectId}/jobs | List Jobs
*ActionsApi* | [**projects_project_id_jobs_job_id_get**](docs/ActionsApi.md#projects_project_id_jobs_job_id_get) | **GET** /projects/{projectId}/jobs/{jobId} | Get Job
*ActionsApi* | [**projects_project_id_launch_machines_post**](docs/ActionsApi.md#projects_project_id_launch_machines_post) | **POST** /projects/{projectId}/launchMachines | Launch target machines
*ActionsApi* | [**projects_project_id_move_machines_post**](docs/ActionsApi.md#projects_project_id_move_machines_post) | **POST** /projects/{projectId}/moveMachines | Moves machines to another project
*ActionsApi* | [**projects_project_id_pause_replication_post**](docs/ActionsApi.md#projects_project_id_pause_replication_post) | **POST** /projects/{projectId}/pauseReplication | Pause replication
*ActionsApi* | [**projects_project_id_replicas_delete**](docs/ActionsApi.md#projects_project_id_replicas_delete) | **DELETE** /projects/{projectId}/replicas | Perform Cleanup
*ActionsApi* | [**projects_project_id_reverse_replication_post**](docs/ActionsApi.md#projects_project_id_reverse_replication_post) | **POST** /projects/{projectId}/reverseReplication | Reverse replication direction
*ActionsApi* | [**projects_project_id_start_replication_post**](docs/ActionsApi.md#projects_project_id_start_replication_post) | **POST** /projects/{projectId}/startReplication | Start replication
*ActionsApi* | [**projects_project_id_stop_replication_post**](docs/ActionsApi.md#projects_project_id_stop_replication_post) | **POST** /projects/{projectId}/stopReplication | Stop replication
*AuthenticationApi* | [**login_post**](docs/AuthenticationApi.md#login_post) | **POST** /login | Login
*AuthenticationApi* | [**logout_post**](docs/AuthenticationApi.md#logout_post) | **POST** /logout | Logout
*BlueprintApi* | [**projects_project_id_blueprints_blueprint_id_get**](docs/BlueprintApi.md#projects_project_id_blueprints_blueprint_id_get) | **GET** /projects/{projectId}/blueprints/{blueprintId} | Get Blueprint
*BlueprintApi* | [**projects_project_id_blueprints_blueprint_id_patch**](docs/BlueprintApi.md#projects_project_id_blueprints_blueprint_id_patch) | **PATCH** /projects/{projectId}/blueprints/{blueprintId} | Configure Blueprint
*BlueprintApi* | [**projects_project_id_blueprints_get**](docs/BlueprintApi.md#projects_project_id_blueprints_get) | **GET** /projects/{projectId}/blueprints | List Blueprints
*BlueprintApi* | [**projects_project_id_blueprints_post**](docs/BlueprintApi.md#projects_project_id_blueprints_post) | **POST** /projects/{projectId}/blueprints | Create Blueprint
*CloudApi* | [**cloud_credentials_creds_id_regions_get**](docs/CloudApi.md#cloud_credentials_creds_id_regions_get) | **GET** /cloudCredentials/{credsId}/regions | List Regions
*CloudApi* | [**cloud_credentials_creds_id_regions_region_id_delete**](docs/CloudApi.md#cloud_credentials_creds_id_regions_region_id_delete) | **DELETE** /cloudCredentials/{credsId}/regions/{regionId} | Delete region (VCenter)
*CloudApi* | [**cloud_credentials_creds_id_regions_region_id_get**](docs/CloudApi.md#cloud_credentials_creds_id_regions_region_id_get) | **GET** /cloudCredentials/{credsId}/regions/{regionId} | Get Region
*CloudApi* | [**cloud_credentials_creds_id_regions_region_id_patch**](docs/CloudApi.md#cloud_credentials_creds_id_regions_region_id_patch) | **PATCH** /cloudCredentials/{credsId}/regions/{regionId} | Patch region (rename)
*CloudApi* | [**clouds_get**](docs/CloudApi.md#clouds_get) | **GET** /clouds | List Clouds
*CloudCredentialsApi* | [**cloud_credentials_creds_id_get**](docs/CloudCredentialsApi.md#cloud_credentials_creds_id_get) | **GET** /cloudCredentials/{credsId} | Get Credentials
*CloudCredentialsApi* | [**cloud_credentials_creds_id_patch**](docs/CloudCredentialsApi.md#cloud_credentials_creds_id_patch) | **PATCH** /cloudCredentials/{credsId} | Change Credentials
*CloudCredentialsApi* | [**cloud_credentials_get**](docs/CloudCredentialsApi.md#cloud_credentials_get) | **GET** /cloudCredentials | List Credentials
*CloudCredentialsApi* | [**cloud_credentials_post**](docs/CloudCredentialsApi.md#cloud_credentials_post) | **POST** /cloudCredentials | Create Credentials
*DefaultApi* | [**accounts_account_id_access_get**](docs/DefaultApi.md#accounts_account_id_access_get) | **GET** /accounts/{accountId}/access | get a temporary token by email
*DefaultApi* | [**extended_account_info_get**](docs/DefaultApi.md#extended_account_info_get) | **GET** /extendedAccountInfo | Returns the extended current account information.
*DefaultApi* | [**projects_assign_users_post**](docs/DefaultApi.md#projects_assign_users_post) | **POST** /projects/assignUsers | Assign User
*DefaultApi* | [**projects_project_id_audit_log_get**](docs/DefaultApi.md#projects_project_id_audit_log_get) | **GET** /projects/{projectId}/auditLog | Get audit log
*DefaultApi* | [**projects_project_id_machines_machine_id_force_rescan_post**](docs/DefaultApi.md#projects_project_id_machines_machine_id_force_rescan_post) | **POST** /projects/{projectId}/machines/{machineId}/forceRescan | Force rescan of machine volumes.
*DefaultApi* | [**projects_project_id_storage_get**](docs/DefaultApi.md#projects_project_id_storage_get) | **GET** /projects/{projectId}/storage | project&#39;s storage
*DefaultApi* | [**projects_remove_users_post**](docs/DefaultApi.md#projects_remove_users_post) | **POST** /projects/removeUsers | Remove User
*DefaultApi* | [**replace_api_token_post**](docs/DefaultApi.md#replace_api_token_post) | **POST** /replaceApiToken | Replaces API token
*DefaultApi* | [**set_password_post**](docs/DefaultApi.md#set_password_post) | **POST** /setPassword | Set password for invited user
*DefaultApi* | [**users_assign_roles_post**](docs/DefaultApi.md#users_assign_roles_post) | **POST** /users/assignRoles | Add roles to users
*DefaultApi* | [**users_post**](docs/DefaultApi.md#users_post) | **POST** /users | Create a new User
*DefaultApi* | [**users_revoke_roles_post**](docs/DefaultApi.md#users_revoke_roles_post) | **POST** /users/revokeRoles | Revoke roles from users
*LicensingApi* | [**licenses_get**](docs/LicensingApi.md#licenses_get) | **GET** /licenses | List Licenses
*LicensingApi* | [**licenses_license_id_get**](docs/LicensingApi.md#licenses_license_id_get) | **GET** /licenses/{licenseId} | Get License
*MachinesApi* | [**projects_project_id_machines_delete**](docs/MachinesApi.md#projects_project_id_machines_delete) | **DELETE** /projects/{projectId}/machines | Uninstall multiple agents
*MachinesApi* | [**projects_project_id_machines_get**](docs/MachinesApi.md#projects_project_id_machines_get) | **GET** /projects/{projectId}/machines | List Machines
*MachinesApi* | [**projects_project_id_machines_machine_id_delete**](docs/MachinesApi.md#projects_project_id_machines_machine_id_delete) | **DELETE** /projects/{projectId}/machines/{machineId} | Uninstall agent
*MachinesApi* | [**projects_project_id_machines_machine_id_get**](docs/MachinesApi.md#projects_project_id_machines_machine_id_get) | **GET** /projects/{projectId}/machines/{machineId} | Get a specific machine.
*MachinesApi* | [**projects_project_id_machines_machine_id_patch**](docs/MachinesApi.md#projects_project_id_machines_machine_id_patch) | **PATCH** /projects/{projectId}/machines/{machineId} | Update a machine. Accepts only Launch time updates.
*MachinesApi* | [**projects_project_id_machines_patch**](docs/MachinesApi.md#projects_project_id_machines_patch) | **PATCH** /projects/{projectId}/machines | Batch-update multiple machines
*MachinesApi* | [**projects_project_id_replicas_replica_id_get**](docs/MachinesApi.md#projects_project_id_replicas_replica_id_get) | **GET** /projects/{projectId}/replicas/{replicaId} | Get Target Machine
*ProjectApi* | [**projects_get**](docs/ProjectApi.md#projects_get) | **GET** /projects | List Projects
*ProjectApi* | [**projects_post**](docs/ProjectApi.md#projects_post) | **POST** /projects | Create Project
*ProjectApi* | [**projects_project_id_delete**](docs/ProjectApi.md#projects_project_id_delete) | **DELETE** /projects/{projectId} | Delete Project and all sub-resources including cloud assets other than launched target machines
*ProjectApi* | [**projects_project_id_get**](docs/ProjectApi.md#projects_project_id_get) | **GET** /projects/{projectId} | Get Project
*ProjectApi* | [**projects_project_id_patch**](docs/ProjectApi.md#projects_project_id_patch) | **PATCH** /projects/{projectId} | Update Project (including partial update)
*ProjectApi* | [**projects_project_id_tags_get**](docs/ProjectApi.md#projects_project_id_tags_get) | **GET** /projects/{projectId}/tags | Gets all instance tags of all machines in the project.
*ProjectApi* | [**projects_project_id_target_cloud_credentials_post**](docs/ProjectApi.md#projects_project_id_target_cloud_credentials_post) | **POST** /projects/{projectId}/targetCloudCredentials | Set target cloud credentials
*RecoveryPlansApi* | [**projects_project_id_recovery_plans_get**](docs/RecoveryPlansApi.md#projects_project_id_recovery_plans_get) | **GET** /projects/{projectId}/recoveryPlans | Gets all recovery plans for the project.
*RecoveryPlansApi* | [**projects_project_id_recovery_plans_post**](docs/RecoveryPlansApi.md#projects_project_id_recovery_plans_post) | **POST** /projects/{projectId}/recoveryPlans | Creates a new recovery plan.
*RecoveryPlansApi* | [**projects_project_id_recovery_plans_recovery_plan_id_delete**](docs/RecoveryPlansApi.md#projects_project_id_recovery_plans_recovery_plan_id_delete) | **DELETE** /projects/{projectId}/recoveryPlans/{recoveryPlanId} | Deletes a recovery plan.
*RecoveryPlansApi* | [**projects_project_id_recovery_plans_recovery_plan_id_get**](docs/RecoveryPlansApi.md#projects_project_id_recovery_plans_recovery_plan_id_get) | **GET** /projects/{projectId}/recoveryPlans/{recoveryPlanId} | Gets a recovery plan.
*RecoveryPlansApi* | [**projects_project_id_recovery_plans_recovery_plan_id_patch**](docs/RecoveryPlansApi.md#projects_project_id_recovery_plans_recovery_plan_id_patch) | **PATCH** /projects/{projectId}/recoveryPlans/{recoveryPlanId} | Updates a new recovery plan.
*RecoveryPlansApi* | [**projects_project_id_run_recovery_plan_post**](docs/RecoveryPlansApi.md#projects_project_id_run_recovery_plan_post) | **POST** /projects/{projectId}/runRecoveryPlan | Launch a recovery plan.
*ReplicationApi* | [**projects_project_id_machines_machine_id_bandwidth_throttling_get**](docs/ReplicationApi.md#projects_project_id_machines_machine_id_bandwidth_throttling_get) | **GET** /projects/{projectId}/machines/{machineId}/bandwidthThrottling | Get value of network bandwidth throttling setting for Machine
*ReplicationApi* | [**projects_project_id_machines_machine_id_bandwidth_throttling_patch**](docs/ReplicationApi.md#projects_project_id_machines_machine_id_bandwidth_throttling_patch) | **PATCH** /projects/{projectId}/machines/{machineId}/bandwidthThrottling | Set value of network bandwidth throttling setting for Machine
*ReplicationApi* | [**projects_project_id_machines_machine_id_delete**](docs/ReplicationApi.md#projects_project_id_machines_machine_id_delete) | **DELETE** /projects/{projectId}/machines/{machineId} | Uninstall agent
*ReplicationApi* | [**projects_project_id_machines_machine_id_pointsintime_get**](docs/ReplicationApi.md#projects_project_id_machines_machine_id_pointsintime_get) | **GET** /projects/{projectId}/machines/{machineId}/pointsintime | List Available Points-in-time
*ReplicationApi* | [**projects_project_id_replication_configurations_get**](docs/ReplicationApi.md#projects_project_id_replication_configurations_get) | **GET** /projects/{projectId}/replicationConfigurations | List Replication Configurations
*ReplicationApi* | [**projects_project_id_replication_configurations_post**](docs/ReplicationApi.md#projects_project_id_replication_configurations_post) | **POST** /projects/{projectId}/replicationConfigurations | Create Replication Configuration
*ReplicationApi* | [**projects_project_id_replication_configurations_replication_configuration_id_patch**](docs/ReplicationApi.md#projects_project_id_replication_configurations_replication_configuration_id_patch) | **PATCH** /projects/{projectId}/replicationConfigurations/{replicationConfigurationId} | Modify Replication Configuration
*UserApi* | [**change_password_post**](docs/UserApi.md#change_password_post) | **POST** /changePassword | Change Password
*UserApi* | [**me_get**](docs/UserApi.md#me_get) | **GET** /me | Me
*UserApi* | [**users_user_id_delete**](docs/UserApi.md#users_user_id_delete) | **DELETE** /users/{userId} | Delete a User
*UserApi* | [**users_user_id_patch**](docs/UserApi.md#users_user_id_patch) | **PATCH** /users/{userId} | Modify user settings


## Documentation For Models

 - [Account](docs/Account.md)
 - [AccountCeAdminProperties](docs/AccountCeAdminProperties.md)
 - [AccountLink](docs/AccountLink.md)
 - [AccountLinkList](docs/AccountLinkList.md)
 - [AccountRequest](docs/AccountRequest.md)
 - [AccountRequestList](docs/AccountRequestList.md)
 - [AccountsList](docs/AccountsList.md)
 - [AgentNextReplicationInitRequest](docs/AgentNextReplicationInitRequest.md)
 - [AllProjectFeatures](docs/AllProjectFeatures.md)
 - [AuditLog](docs/AuditLog.md)
 - [AuditLogChangedField](docs/AuditLogChangedField.md)
 - [AuditLogEntry](docs/AuditLogEntry.md)
 - [AuditLogEntryParticipatingMachines](docs/AuditLogEntryParticipatingMachines.md)
 - [BandwidthThrottling](docs/BandwidthThrottling.md)
 - [Blueprint](docs/Blueprint.md)
 - [BlueprintDisks](docs/BlueprintDisks.md)
 - [BlueprintList](docs/BlueprintList.md)
 - [CSLPItem](docs/CSLPItem.md)
 - [CSLPRequest](docs/CSLPRequest.md)
 - [CSLPResult](docs/CSLPResult.md)
 - [Cloud](docs/Cloud.md)
 - [CloudCredentials](docs/CloudCredentials.md)
 - [CloudCredentialsList](docs/CloudCredentialsList.md)
 - [CloudCredentialsRequest](docs/CloudCredentialsRequest.md)
 - [CloudsList](docs/CloudsList.md)
 - [ComputeLocation](docs/ComputeLocation.md)
 - [Configurations](docs/Configurations.md)
 - [ConfigurationsList](docs/ConfigurationsList.md)
 - [DiskConfig](docs/DiskConfig.md)
 - [DynamicConfiguration](docs/DynamicConfiguration.md)
 - [Error](docs/Error.md)
 - [ExtendedAccountInfo](docs/ExtendedAccountInfo.md)
 - [GcpMachinesFinanceData](docs/GcpMachinesFinanceData.md)
 - [IdentityProviderRedirectResponse](docs/IdentityProviderRedirectResponse.md)
 - [InitializationStep](docs/InitializationStep.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InlineObject10](docs/InlineObject10.md)
 - [InlineObject2](docs/InlineObject2.md)
 - [InlineObject3](docs/InlineObject3.md)
 - [InlineObject4](docs/InlineObject4.md)
 - [InlineObject5](docs/InlineObject5.md)
 - [InlineObject6](docs/InlineObject6.md)
 - [InlineObject7](docs/InlineObject7.md)
 - [InlineObject8](docs/InlineObject8.md)
 - [InlineObject9](docs/InlineObject9.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [Job](docs/Job.md)
 - [JobLog](docs/JobLog.md)
 - [JobTargetMachine](docs/JobTargetMachine.md)
 - [JobsList](docs/JobsList.md)
 - [KeyValueList](docs/KeyValueList.md)
 - [LaunchMachinesParameters](docs/LaunchMachinesParameters.md)
 - [LaunchMachinesParametersDebugScripts](docs/LaunchMachinesParametersDebugScripts.md)
 - [License](docs/License.md)
 - [LicenseCeAdminProperties](docs/LicenseCeAdminProperties.md)
 - [LicenseFeatures](docs/LicenseFeatures.md)
 - [LicenseList](docs/LicenseList.md)
 - [ListUsersResult](docs/ListUsersResult.md)
 - [ListUsersResults](docs/ListUsersResults.md)
 - [LogicalLocation](docs/LogicalLocation.md)
 - [Machine](docs/Machine.md)
 - [MachineAndPathAndPointInTime](docs/MachineAndPathAndPointInTime.md)
 - [MachineAndPointInTime](docs/MachineAndPointInTime.md)
 - [MachineLicense](docs/MachineLicense.md)
 - [MachineLifeCycle](docs/MachineLifeCycle.md)
 - [MachineReplicationConfiguration](docs/MachineReplicationConfiguration.md)
 - [MachineReplicationInfo](docs/MachineReplicationInfo.md)
 - [MachineReplicationInfoInitiationStates](docs/MachineReplicationInfoInitiationStates.md)
 - [MachineReplicationInfoInitiationStatesItems](docs/MachineReplicationInfoInitiationStatesItems.md)
 - [MachineSnapshotCredits](docs/MachineSnapshotCredits.md)
 - [MachineSourceProperties](docs/MachineSourceProperties.md)
 - [MachineSourcePropertiesCpu](docs/MachineSourcePropertiesCpu.md)
 - [MachineSourcePropertiesDisks](docs/MachineSourcePropertiesDisks.md)
 - [MachineSourcePropertiesInstalledApplications](docs/MachineSourcePropertiesInstalledApplications.md)
 - [MachineSourcePropertiesInstalledApplicationsItems](docs/MachineSourcePropertiesInstalledApplicationsItems.md)
 - [MachineSourcePropertiesRunningServices](docs/MachineSourcePropertiesRunningServices.md)
 - [MachineSourcePropertiesRunningServicesItems](docs/MachineSourcePropertiesRunningServicesItems.md)
 - [MachineThrottleTimeSeconds](docs/MachineThrottleTimeSeconds.md)
 - [MachinesList](docs/MachinesList.md)
 - [MachinesListInvalidIDsAndJob](docs/MachinesListInvalidIDsAndJob.md)
 - [NetworkInterface](docs/NetworkInterface.md)
 - [Outpost](docs/Outpost.md)
 - [PointInTime](docs/PointInTime.md)
 - [PointInTimeList](docs/PointInTimeList.md)
 - [PopulateJobNames](docs/PopulateJobNames.md)
 - [PopulateJobParams](docs/PopulateJobParams.md)
 - [Project](docs/Project.md)
 - [ProjectCeAdminProperties](docs/ProjectCeAdminProperties.md)
 - [ProjectFeatures](docs/ProjectFeatures.md)
 - [ProjectStorage](docs/ProjectStorage.md)
 - [ProjectStorageWorkingStorage](docs/ProjectStorageWorkingStorage.md)
 - [ProjectsAndUsers](docs/ProjectsAndUsers.md)
 - [ProjectsAndUsersItems](docs/ProjectsAndUsersItems.md)
 - [ProjectsList](docs/ProjectsList.md)
 - [RecoveryPlan](docs/RecoveryPlan.md)
 - [RecoveryPlanList](docs/RecoveryPlanList.md)
 - [RecoveryPlanStep](docs/RecoveryPlanStep.md)
 - [RecoveryPlanSteps](docs/RecoveryPlanSteps.md)
 - [Region](docs/Region.md)
 - [RegionsList](docs/RegionsList.md)
 - [Replica](docs/Replica.md)
 - [ReplicationConfiguration](docs/ReplicationConfiguration.md)
 - [ReplicationConfigurationList](docs/ReplicationConfigurationList.md)
 - [ReplicationConfigurationReplicationTags](docs/ReplicationConfigurationReplicationTags.md)
 - [SamlSettings](docs/SamlSettings.md)
 - [SecurityGroup](docs/SecurityGroup.md)
 - [StorageLocation](docs/StorageLocation.md)
 - [Subnet](docs/Subnet.md)
 - [Time](docs/Time.md)
 - [UpdateableScripts](docs/UpdateableScripts.md)
 - [UpdateableScriptsResult](docs/UpdateableScriptsResult.md)
 - [UpdateableScriptsResultOnPremiseVolumes](docs/UpdateableScriptsResultOnPremiseVolumes.md)
 - [UpgradeCounterDelay](docs/UpgradeCounterDelay.md)
 - [Usage](docs/Usage.md)
 - [UsageList](docs/UsageList.md)
 - [User](docs/User.md)
 - [UserReport](docs/UserReport.md)
 - [UserReportGcpMachinesFinanceData](docs/UserReportGcpMachinesFinanceData.md)
 - [UserReports](docs/UserReports.md)
 - [UserSettings](docs/UserSettings.md)
 - [UserSettingsSendNotifications](docs/UserSettingsSendNotifications.md)
 - [UsersAndRoles](docs/UsersAndRoles.md)
 - [UsersAndRolesItems](docs/UsersAndRolesItems.md)
 - [UsersList](docs/UsersList.md)


## Documentation For Authorization

 See the above example for authorization.

## Author

(2nd Watch)[https://www.2ndwatch.com]



## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in cloudendure.apis and cloudendure.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from cloudendure.api.default_api import DefaultApi`
- `from cloudendure.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import cloudendure
from cloudendure.apis import *
from cloudendure.models import *
```

## Generating the API

### Dependencies
First things first, you'll need these tools installed in order to build this
projects client code:
  * `curl`
  * `python`
  * (Poetry)[https://python-poetry.org/]
  * (openapi-generator)[https://github.com/OpenAPITools/openapi-generator]

### `Makefile`, Build / Rebuild
This project makes extensive use of `GNU make`.  You can view all the available
make commands by just typing the `make` command, or `make help`.  Each of the
components used to build this project are their own command, but the two that
we're looking for to do everything for us are:
  * `make build-api`
  * `make rebuild-api`

Both of these commands do all the things.  The only difference is that
`rebuild-api` deletes all the generated code first.  I prefer this method to
make sure any cruft that's different between the apis from cloudendure is
removed.  So, simply run:

```bash
%> make rebuild-api
```

... and boom!  it's built!

Now, commit the changes, then tag using the `make tag` command.  Do note that
the actual API version from CE is "5", so the versions here will not entirely
match up.  Given that this needed to be regenerated, it was likely a breaking
change, but we at _least_ want to stick with the "5", so we'll bump the MINOR
version.ie: the `X` in `v5.X.0`

once this step is done we should be complete.

