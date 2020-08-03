# openapi_client.PreCommitApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pre_commit_server_limits**](PreCommitApi.md#get_pre_commit_server_limits) | **GET** /api/pre-commit/server-limits | Get pre-commit server limits
[**poll_pre_commit_results**](PreCommitApi.md#poll_pre_commit_results) | **GET** /api/projects/{project}/pre-commit | Poll pre-commit results
[**process_pre_commit**](PreCommitApi.md#process_pre_commit) | **POST** /api/projects/{project}/pre-commit/{baseCommit} | Trigger pre-commit analysis


# **get_pre_commit_server_limits**
> PreCommitServerLimits get_pre_commit_server_limits()

Get pre-commit server limits

Returns the configured limits for pre-commit analysis (file count, file size, etc.). This service is public API since Teamscale 5.6. The API requires no permissions

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
    api_instance = openapi_client.PreCommitApi(api_client)
    
    try:
        # Get pre-commit server limits
        api_response = api_instance.get_pre_commit_server_limits()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PreCommitApi->get_pre_commit_server_limits: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PreCommitServerLimits**](PreCommitServerLimits.md)

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

# **poll_pre_commit_results**
> FindingDelta poll_pre_commit_results(project)

Poll pre-commit results

Returns added/removed/missed findings if the analysis is finished. This service is public API since Teamscale 5.7. The API requires the user to have View Project permissions on the project.

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
    api_instance = openapi_client.PreCommitApi(api_client)
    project = 'project_example' # str | The project alias or id.

    try:
        # Poll pre-commit results
        api_response = api_instance.poll_pre_commit_results(project)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PreCommitApi->poll_pre_commit_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 

### Return type

[**FindingDelta**](FindingDelta.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | The project does not exist. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_pre_commit**
> str process_pre_commit(project, base_commit, pre_commit_upload_data)

Trigger pre-commit analysis

Uploads new change data and analyzes them on a user-specific pre-commit branch.Service that takes a parent commit as target path for performing pre-commit analysis. This service is public API since Teamscale 5.7. The API requires the user to have View Project permissions on the project.

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
    api_instance = openapi_client.PreCommitApi(api_client)
    project = 'project_example' # str | The project alias or id.
base_commit = 'base_commit_example' # str | 
pre_commit_upload_data = openapi_client.PreCommitUploadData() # PreCommitUploadData | The content and paths of added, modified and removed files.

    try:
        # Trigger pre-commit analysis
        api_response = api_instance.process_pre_commit(project, base_commit, pre_commit_upload_data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PreCommitApi->process_pre_commit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **base_commit** | **str**|  | 
 **pre_commit_upload_data** | [**PreCommitUploadData**](PreCommitUploadData.md)| The content and paths of added, modified and removed files. | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Returns the name of the artificial pre-commit branch that can be used to reference the changes. |  -  |
**413** | At least one of the configured limits has been violated. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | The project does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

