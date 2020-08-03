# openapi_client.ArchitectureApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_architecture_assessments**](ArchitectureApi.md#get_all_architecture_assessments) | **GET** /api/projects/{project}/architectures/assessments | Get all architecture assessments
[**upload_architecture**](ArchitectureApi.md#upload_architecture) | **POST** /api/projects/{project}/architectures | Upload architecture


# **get_all_architecture_assessments**
> list[ArchitectureOverviewInfo] get_all_architecture_assessments(project, t=t)

Get all architecture assessments

Returns available architecture assessments. All architectures in analyzed and in pending commits are returned including tags on the state of their analysis (added, modified, deleted). Returns an empty list if no assessments available. This service is public API since Teamscale 5.7. The API requires the user to have View Project permissions on the project.

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
    api_instance = openapi_client.ArchitectureApi(api_client)
    project = 'project_example' # str | The project alias or id.
t = 't_example' # str | This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. (optional)

    try:
        # Get all architecture assessments
        api_response = api_instance.get_all_architecture_assessments(project, t=t)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArchitectureApi->get_all_architecture_assessments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **t** | **str**| This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. | [optional] 

### Return type

[**list[ArchitectureOverviewInfo]**](ArchitectureOverviewInfo.md)

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

# **upload_architecture**
> upload_architecture(project, t=t, revision=revision, repository=repository, message=message, format=format, template=template, file=file)

Upload architecture

Imports an architecture file. This service is public API since Teamscale 5.9. The API requires the user to have Edit Architectures permissions on the project.

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
    api_instance = openapi_client.ArchitectureApi(api_client)
    project = 'project_example' # str | The project alias or id.
t = 't_example' # str | This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. (optional)
revision = 'revision_example' # str | This parameter allows to pass a revision instead of a timestamp. (optional)
repository = 'repository_example' # str | This parameter allows to pass a repository name (optional)
message = 'Imported new architecture' # str | The commit message describing the changes made by the upload. (optional) (default to 'Imported new architecture')
format = 'TEAMSCALE_ARCHITECTURE' # str | The parameter that determines the upload format. (optional) (default to 'TEAMSCALE_ARCHITECTURE')
template = 'template_example' # str | The parameter used for passing in a template architecture. (optional)
file = '/path/to/file' # list[file] |  (optional)

    try:
        # Upload architecture
        api_instance.upload_architecture(project, t=t, revision=revision, repository=repository, message=message, format=format, template=template, file=file)
    except ApiException as e:
        print("Exception when calling ArchitectureApi->upload_architecture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **t** | **str**| This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. | [optional] 
 **revision** | **str**| This parameter allows to pass a revision instead of a timestamp. | [optional] 
 **repository** | **str**| This parameter allows to pass a repository name | [optional] 
 **message** | **str**| The commit message describing the changes made by the upload. | [optional] [default to &#39;Imported new architecture&#39;]
 **format** | **str**| The parameter that determines the upload format. | [optional] [default to &#39;TEAMSCALE_ARCHITECTURE&#39;]
 **template** | **str**| The parameter used for passing in a template architecture. | [optional] 
 **file** | **list[file]**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | No path for architecture given.   Architecture path must have extension.architecture.   Upload was rejected, because it refers to a timestamp too far back in time. |  -  |
**404** | The project does not exist. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

