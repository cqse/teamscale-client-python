# openapi_client.ProjectApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**are_abap_projects_updating**](ProjectApi.md#are_abap_projects_updating) | **GET** /api/sap-sysid-projects/{sysid}/is-updating/{updateid} | Checks if any relevant ABAP project is updating
[**create_project**](ProjectApi.md#create_project) | **POST** /api/projects | Create project
[**delete_project**](ProjectApi.md#delete_project) | **DELETE** /api/projects/{project} | Delete project
[**edit_project**](ProjectApi.md#edit_project) | **PUT** /api/projects/{project} | Update project
[**edit_project1**](ProjectApi.md#edit_project1) | **PUT** /api/projects/{project}/configuration | Edit project
[**get_all_project_aliases_or_ids**](ProjectApi.md#get_all_project_aliases_or_ids) | **GET** /api/projects/aliases | Get project aliases
[**get_all_projects**](ProjectApi.md#get_all_projects) | **GET** /api/projects | Get projects
[**get_branches**](ProjectApi.md#get_branches) | **GET** /api/projects/{project}/branches | Get branches info
[**get_file_extensions**](ProjectApi.md#get_file_extensions) | **GET** /api/projects/{project}/file-extensions | Get project file extensions
[**get_languages**](ProjectApi.md#get_languages) | **GET** /api/projects/{project}/languages | Get project languages
[**get_project**](ProjectApi.md#get_project) | **GET** /api/projects/{project} | Get project
[**get_project_configuration**](ProjectApi.md#get_project_configuration) | **GET** /api/projects/{project}/configuration | Get project configuration
[**lookup_project_by_sap_system_id**](ProjectApi.md#lookup_project_by_sap_system_id) | **GET** /api/projects-by-sap-system-id/{sap-system-id} | Get projects corresponding to given SAP system ID.
[**trigger_reanalysis**](ProjectApi.md#trigger_reanalysis) | **POST** /api/projects/{project}/reanalysis | Trigger project reanalysis
[**update_abap_projects**](ProjectApi.md#update_abap_projects) | **POST** /api/sap-sysid-projects/{sysid}/update | Synchronize ABAP projects


# **are_abap_projects_updating**
> bool are_abap_projects_updating(sysid, updateid)

Checks if any relevant ABAP project is updating

Checks if any ABAP project with a configured SAP system id relative to the given update id (to allow multiple update requests) is currently updating. This service is public API since Teamscale 5.7. The API requires no permissions

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectApi(api_client)
    sysid = 'sysid_example' # str | SAP system id.
updateid = 'updateid_example' # str | Update UUID.

    try:
        # Checks if any relevant ABAP project is updating
        api_response = api_instance.are_abap_projects_updating(sysid, updateid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->are_abap_projects_updating: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sysid** | **str**| SAP system id. | 
 **updateid** | **str**| Update UUID. | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | SAP system id is not configured. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> create_project(copy_data_from_project=copy_data_from_project, skip_project_validation=skip_project_validation, project_configuration=project_configuration)

Create project

Creates project based on provided project configuration. This service is public API since Teamscale 5.6. The API requires the user to have Create Projects permissions.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectApi(api_client)
    copy_data_from_project = 'copy_data_from_project_example' # str | Indicates whether to copy all data (ext. uploads, finding exclusions, etc.) from an existing project. The value is the project id. (optional)
skip_project_validation = True # bool | Indicates whether to skip validation of the project. Can be used to force project creation despite validation errors. (optional)
project_configuration = openapi_client.ProjectConfiguration() # ProjectConfiguration |  (optional)

    try:
        # Create project
        api_instance.create_project(copy_data_from_project=copy_data_from_project, skip_project_validation=skip_project_validation, project_configuration=project_configuration)
    except ApiException as e:
        print("Exception when calling ProjectApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **copy_data_from_project** | **str**| Indicates whether to copy all data (ext. uploads, finding exclusions, etc.) from an existing project. The value is the project id. | [optional] 
 **skip_project_validation** | **bool**| Indicates whether to skip validation of the project. Can be used to force project creation despite validation errors. | [optional] 
 **project_configuration** | [**ProjectConfiguration**](ProjectConfiguration.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Project created based on provided configuration. |  -  |
**400** | Project validation error occurred. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(project, force_delete=force_delete, delete_all_assignments=delete_all_assignments, delete_all_dashboards=delete_all_dashboards)

Delete project

Deletes a project. This service is public API since Teamscale 5.2. The API requires the user to have Delete Project permissions on the project.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectApi(api_client)
    project = 'project_example' # str | The project alias or id.
force_delete = True # bool | Whether to force project deletion regardless of current deletion or re-analysis state. (optional)
delete_all_assignments = True # bool | Whether all current role assignments should be deleted. Otherwise these can be reimported if a project with the same id or alias is created. (optional)
delete_all_dashboards = True # bool | Whether dashboards that only refer to the project to delete or/and non-existing projects should be deleted. (optional)

    try:
        # Delete project
        api_instance.delete_project(project, force_delete=force_delete, delete_all_assignments=delete_all_assignments, delete_all_dashboards=delete_all_dashboards)
    except ApiException as e:
        print("Exception when calling ProjectApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **force_delete** | **bool**| Whether to force project deletion regardless of current deletion or re-analysis state. | [optional] 
 **delete_all_assignments** | **bool**| Whether all current role assignments should be deleted. Otherwise these can be reimported if a project with the same id or alias is created. | [optional] 
 **delete_all_dashboards** | **bool**| Whether dashboards that only refer to the project to delete or/and non-existing projects should be deleted. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | The project does not exist. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_project**
> ProjectUpdateResult edit_project(project, project_info=project_info)

Update project

Updates an existing project. This service is public API since Teamscale 5.2. The API requires the user to have Edit Project permissions on the project.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectApi(api_client)
    project = 'project_example' # str | The project alias or id.
project_info = openapi_client.ProjectInfo() # ProjectInfo |  (optional)

    try:
        # Update project
        api_response = api_instance.edit_project(project, project_info=project_info)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->edit_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **project_info** | [**ProjectInfo**](ProjectInfo.md)|  | [optional] 

### Return type

[**ProjectUpdateResult**](ProjectUpdateResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Invalid alias supplied or resource ID does not match supplied ProjectInfo |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | The project does not exist. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_project1**
> bool edit_project1(project, reanalyze_if_required=reanalyze_if_required, skip_project_validation=skip_project_validation, project_configuration=project_configuration)

Edit project

Edits project based on provided project configuration. This service is public API since Teamscale 5.6. The API requires the user to have Edit Project permissions on the project.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectApi(api_client)
    project = 'project_example' # str | The project alias or id.
reanalyze_if_required = True # bool | Parameter for controlling whether to perform a re-analyze of the project if required when changing the project configuration. Certain connector parameter  changes require the project to be re-analyzed for consistency reasons. This flag indicates that the user agreed for a re-analysis. (optional)
skip_project_validation = True # bool | Indicates whether to skip validation of the project. Can be used to force project creation despite validation errors. (optional)
project_configuration = openapi_client.ProjectConfiguration() # ProjectConfiguration |  (optional)

    try:
        # Edit project
        api_response = api_instance.edit_project1(project, reanalyze_if_required=reanalyze_if_required, skip_project_validation=skip_project_validation, project_configuration=project_configuration)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->edit_project1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **reanalyze_if_required** | **bool**| Parameter for controlling whether to perform a re-analyze of the project if required when changing the project configuration. Certain connector parameter  changes require the project to be re-analyzed for consistency reasons. This flag indicates that the user agreed for a re-analysis. | [optional] 
 **skip_project_validation** | **bool**| Indicates whether to skip validation of the project. Can be used to force project creation despite validation errors. | [optional] 
 **project_configuration** | [**ProjectConfiguration**](ProjectConfiguration.md)|  | [optional] 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, 

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Project validation error occurred. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | The project does not exist. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_project_aliases_or_ids**
> list[str] get_all_project_aliases_or_ids(include_deleting=include_deleting, include_reanalyzing=include_reanalyzing)

Get project aliases

Returns all projects by their aliases (if set) or id. This service is public API since Teamscale 5.2. Only projects visible to the user are returned in the get all queries.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectApi(api_client)
    include_deleting = True # bool | Whether to include projects marked as deleted or not. (optional)
include_reanalyzing = True # bool | Whether to include reanalyzing projects or not. (optional)

    try:
        # Get project aliases
        api_response = api_instance.get_all_project_aliases_or_ids(include_deleting=include_deleting, include_reanalyzing=include_reanalyzing)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_all_project_aliases_or_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_deleting** | **bool**| Whether to include projects marked as deleted or not. | [optional] 
 **include_reanalyzing** | **bool**| Whether to include reanalyzing projects or not. | [optional] 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_projects**
> list[ProjectInfo] get_all_projects(include_deleting=include_deleting, include_reanalyzing=include_reanalyzing)

Get projects

Returns a list of all projects. This service is public API since Teamscale 5.2. Only projects visible to the user are returned in the get all queries.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectApi(api_client)
    include_deleting = True # bool | Whether to include projects marked as deleted or not. (optional)
include_reanalyzing = True # bool | Whether to include reanalyzing projects or not. (optional)

    try:
        # Get projects
        api_response = api_instance.get_all_projects(include_deleting=include_deleting, include_reanalyzing=include_reanalyzing)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_all_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_deleting** | **bool**| Whether to include projects marked as deleted or not. | [optional] 
 **include_reanalyzing** | **bool**| Whether to include reanalyzing projects or not. | [optional] 

### Return type

[**list[ProjectInfo]**](ProjectInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_branches**
> BranchesInfo get_branches(project)

Get branches info

Gets the branches info containing a branch alias specific to the requesting user for the precommit branch. This service is public API since Teamscale 5.3. The API requires the user to have View Project permissions on the project.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectApi(api_client)
    project = 'project_example' # str | The project alias or id.

    try:
        # Get branches info
        api_response = api_instance.get_branches(project)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_branches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 

### Return type

[**BranchesInfo**](BranchesInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | The project does not exist. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_extensions**
> list[str] get_file_extensions(project)

Get project file extensions

Returns a list of file extensions a project has been configured for This service is public API since Teamscale 5.5.1. The API requires the user to have View Project permissions on the project.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectApi(api_client)
    project = 'project_example' # str | The project alias or id.

    try:
        # Get project file extensions
        api_response = api_instance.get_file_extensions(project)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_file_extensions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | The project does not exist. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_languages**
> list[str] get_languages(project)

Get project languages

Returns a list of languages a project has been configured for This service is public API since Teamscale 5.5. The API requires the user to have View Project permissions on the project.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectApi(api_client)
    project = 'project_example' # str | The project alias or id.

    try:
        # Get project languages
        api_response = api_instance.get_languages(project)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_languages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | The project does not exist. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> ProjectInfo get_project(project)

Get project

Returns details on a project. This service is public API since Teamscale 5.2. The API requires the user to have View Project permissions on the project.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectApi(api_client)
    project = 'project_example' # str | The project alias or id.

    try:
        # Get project
        api_response = api_instance.get_project(project)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 

### Return type

[**ProjectInfo**](ProjectInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | The project does not exist. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_configuration**
> ProjectConfiguration get_project_configuration(project, skip_alias_resolution=skip_alias_resolution)

Get project configuration

Returns the configuration used for creation of the project in the path parameter. This service is public API since Teamscale 5.6. The API requires the user to have View Project permissions on the project.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectApi(api_client)
    project = 'project_example' # str | The project alias or id.
skip_alias_resolution = True # bool | Allows to skip resolution of project alias in case project id is directly provided (optional)

    try:
        # Get project configuration
        api_response = api_instance.get_project_configuration(project, skip_alias_resolution=skip_alias_resolution)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_project_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **skip_alias_resolution** | **bool**| Allows to skip resolution of project alias in case project id is directly provided | [optional] 

### Return type

[**ProjectConfiguration**](ProjectConfiguration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | The project does not exist. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lookup_project_by_sap_system_id**
> list[str] lookup_project_by_sap_system_id(sap_system_id)

Get projects corresponding to given SAP system ID.

Looks up Teamscale projects by SAP System ID. Returns project aliases or project IDs if no alias available. This service is public API since Teamscale 5.7. The service will only search among projects visible to current user.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectApi(api_client)
    sap_system_id = 'sap_system_id_example' # str | System ID of SAP system

    try:
        # Get projects corresponding to given SAP system ID.
        api_response = api_instance.lookup_project_by_sap_system_id(sap_system_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->lookup_project_by_sap_system_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sap_system_id** | **str**| System ID of SAP system | 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_reanalysis**
> trigger_reanalysis(project, only_findings_schema_update=only_findings_schema_update)

Trigger project reanalysis

Triggers reanalysis of the project specified in the path parameter. This service is public API since Teamscale 5.9. The API requires the user to have Edit Project permissions on the project.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectApi(api_client)
    project = 'project_example' # str | The project alias or id.
only_findings_schema_update = True # bool | Indicates whether to only update the findings schema without re-analysis. (optional)

    try:
        # Trigger project reanalysis
        api_instance.trigger_reanalysis(project, only_findings_schema_update=only_findings_schema_update)
    except ApiException as e:
        print("Exception when calling ProjectApi->trigger_reanalysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **only_findings_schema_update** | **bool**| Indicates whether to only update the findings schema without re-analysis. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | The project does not exist. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_abap_projects**
> str update_abap_projects(sysid)

Synchronize ABAP projects

Incrementally synchronizes all ABAP projects with the given sap system id configured. This service is public API since Teamscale 5.7. The API requires no permissions

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectApi(api_client)
    sysid = 'sysid_example' # str | The id of the SAP Netweaver system, which shall be configured under `Project Options`.

    try:
        # Synchronize ABAP projects
        api_response = api_instance.update_abap_projects(sysid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->update_abap_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sysid** | **str**| The id of the SAP Netweaver system, which shall be configured under &#x60;Project Options&#x60;. | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | SAP system id is not configured. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

