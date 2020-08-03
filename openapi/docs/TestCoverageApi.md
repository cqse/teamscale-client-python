# openapi_client.TestCoverageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_test_coverage**](TestCoverageApi.md#get_test_coverage) | **GET** /api/projects/{project}/test-coverage/{uniformPath} | Returns test coverage
[**get_test_coverage_partitions**](TestCoverageApi.md#get_test_coverage_partitions) | **GET** /api/projects/{project}/test-coverage-partitions/{uniformPath} | Test Coverage Partitions


# **get_test_coverage**
> LineCoverageInfo get_test_coverage(project, uniform_path, t=t, pretty=pretty, include_method_coverage=include_method_coverage)

Returns test coverage

Returns the line coverage data for an element. This may return no content if no line coverage is available. This service is public API since Teamscale 5.3. The API requires the user to have View Project permissions on the project.

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
    api_instance = openapi_client.TestCoverageApi(api_client)
    project = 'project_example' # str | The project alias or id.
uniform_path = 'uniform_path_example' # str | 
t = 't_example' # str | This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. (optional)
pretty = False # bool | If true, the coverage is adjusted to match a pretty printed version of the code. (optional) (default to False)
include_method_coverage = False # bool | If true, the coverage will include method-accurate coverage. (optional) (default to False)

    try:
        # Returns test coverage
        api_response = api_instance.get_test_coverage(project, uniform_path, t=t, pretty=pretty, include_method_coverage=include_method_coverage)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestCoverageApi->get_test_coverage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **uniform_path** | **str**|  | 
 **t** | **str**| This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. | [optional] 
 **pretty** | **bool**| If true, the coverage is adjusted to match a pretty printed version of the code. | [optional] [default to False]
 **include_method_coverage** | **bool**| If true, the coverage will include method-accurate coverage. | [optional] [default to False]

### Return type

[**LineCoverageInfo**](LineCoverageInfo.md)

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

# **get_test_coverage_partitions**
> list[TestCoveragePartitionInfo] get_test_coverage_partitions(project, uniform_path, t=t)

Test Coverage Partitions

Returns the line coverage partitions for an element. This service is public API since Teamscale 5.3. The API requires the user to have View Project permissions on the project.

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
    api_instance = openapi_client.TestCoverageApi(api_client)
    project = 'project_example' # str | The project alias or id.
uniform_path = 'uniform_path_example' # str | 
t = 't_example' # str | This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. (optional)

    try:
        # Test Coverage Partitions
        api_response = api_instance.get_test_coverage_partitions(project, uniform_path, t=t)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestCoverageApi->get_test_coverage_partitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **uniform_path** | **str**|  | 
 **t** | **str**| This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. | [optional] 

### Return type

[**list[TestCoveragePartitionInfo]**](TestCoveragePartitionInfo.md)

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

