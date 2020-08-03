# openapi_client.SourceCodeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_code**](SourceCodeApi.md#get_code) | **GET** /api/projects/{project}/source-code-download/{uniformPath} | Download source code


# **get_code**
> get_code(project, uniform_path, t=t)

Download source code

Starts a download of the source code file at the given uniform path This service is public API since Teamscale 5.2. The API requires the user to have View Project permissions on the project.

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
    api_instance = openapi_client.SourceCodeApi(api_client)
    project = 'project_example' # str | The project alias or id.
uniform_path = 'uniform_path_example' # str | The uniform path of the source code file to be downloaded.
t = 't_example' # str | The commit for which the source code should be downloaded. (optional)

    try:
        # Download source code
        api_instance.get_code(project, uniform_path, t=t)
    except ApiException as e:
        print("Exception when calling SourceCodeApi->get_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **uniform_path** | **str**| The uniform path of the source code file to be downloaded. | 
 **t** | **str**| The commit for which the source code should be downloaded. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | The project does not exist. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

