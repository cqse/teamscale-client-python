# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_project_mappings**](DefaultApi.md#calculate_project_mappings) | **POST** /api/projects/{project}/auto-prefix-mappings | Calculate project mappings
[**get_commits_for_revision**](DefaultApi.md#get_commits_for_revision) | **GET** /api/projects/{project}/revision/{revision}/commits | Get teamscale commits
[**get_dashboard_gadget**](DefaultApi.md#get_dashboard_gadget) | **GET** /api/gadgets/jira/dashboard.xml | Get the dashboard gadget
[**get_dashboard_thumbnail**](DefaultApi.md#get_dashboard_thumbnail) | **GET** /api/gadgets/jira/dashboard-thumbnail.png | Get the thumbnail of the Jira dashboard gadget


# **calculate_project_mappings**
> list[ProjectMapping] calculate_project_mappings(project, request_body, branch=branch)

Calculate project mappings

Returns path prefix mappings to which the given paths could be mapped to. This service is public API since Teamscale 5.7. The API requires the user to have View Project permissions on the project.

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
    api_instance = openapi_client.DefaultApi(api_client)
    project = 'project_example' # str | The project alias or id.
request_body = ['request_body_example'] # list[str] | 
branch = 'branch_example' # str | Optional branch name, will use the default branch if not specified. (optional)

    try:
        # Calculate project mappings
        api_response = api_instance.calculate_project_mappings(project, request_body, branch=branch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->calculate_project_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **request_body** | [**list[str]**](str.md)|  | 
 **branch** | **str**| Optional branch name, will use the default branch if not specified. | [optional] 

### Return type

[**list[ProjectMapping]**](ProjectMapping.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | The project does not exist. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_commits_for_revision**
> list[CommitDescriptor] get_commits_for_revision(project, revision)

Get teamscale commits

Returns the teamscale commit representations for a given revision. As a revision can occur in multiple repositories, more than one commit may be returned. This service is public API since Teamscale 5.9.6. The API requires the user to have View Project permissions on the project.

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
    api_instance = openapi_client.DefaultApi(api_client)
    project = 'project_example' # str | The project alias or id.
revision = 'revision_example' # str | 

    try:
        # Get teamscale commits
        api_response = api_instance.get_commits_for_revision(project, revision)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_commits_for_revision: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **revision** | **str**|  | 

### Return type

[**list[CommitDescriptor]**](CommitDescriptor.md)

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

# **get_dashboard_gadget**
> get_dashboard_gadget()

Get the dashboard gadget

Returns the XML descriptor for the dashboard gadget. This service is public API since Teamscale 5.8. The API requires no login

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
    api_instance = openapi_client.DefaultApi(api_client)
    
    try:
        # Get the dashboard gadget
        api_instance.get_dashboard_gadget()
    except ApiException as e:
        print("Exception when calling DefaultApi->get_dashboard_gadget: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**400** | Must configure base URL before calling this service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_thumbnail**
> list[str] get_dashboard_thumbnail()

Get the thumbnail of the Jira dashboard gadget

Returns the thumbnail of the Jira dashboard gadget This service is public API since Teamscale 5.8. The API requires no login

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
    api_instance = openapi_client.DefaultApi(api_client)
    
    try:
        # Get the thumbnail of the Jira dashboard gadget
        api_response = api_instance.get_dashboard_thumbnail()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_dashboard_thumbnail: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

