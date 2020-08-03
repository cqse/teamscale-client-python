# openapi_client.DeltaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_finding_delta_badge**](DeltaApi.md#get_finding_delta_badge) | **GET** /api/projects/{project}/findings/delta/badge | Get finding delta badge
[**get_token_element_churn**](DeltaApi.md#get_token_element_churn) | **GET** /api/projects/{project}/delta/affected-files | Get token element churn


# **get_finding_delta_badge**
> get_finding_delta_badge(project, t1=t1, t2=t2, max_milliseconds=max_milliseconds, uniform_path=uniform_path, t=t, regex=regex, exclude_regex=exclude_regex, added_to_task=added_to_task, filter=filter, invert=invert, assessment_filters=assessment_filters, blacklisted=blacklisted, numeric_delta_only=numeric_delta_only)

Get finding delta badge

Creates a badge for the finding delta, i.e. for the count of newly added, unmodified, and deleted findings. This service is public API since Teamscale 5.9. The API requires the user to have View Project permissions on the project.

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
    api_instance = openapi_client.DeltaApi(api_client)
    project = 'project_example' # str | The project alias or id.
t1 = 't1_example' # str | Range start timestamp (optional)
t2 = 't2_example' # str | Range end timestamp (optional)
max_milliseconds = -1 # int | Range duration in milliseconds (optional) (default to -1)
uniform_path = '' # str | Uniform path to retrieve data for (optional) (default to '')
t = 't_example' # str | This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. (optional)
regex = 'regex_example' # str | The regex filter. Filters findings by this regex. Considered Fields are Message and Location. Matches will be included in the result. (optional)
exclude_regex = True # bool | Whether regex excludes or includes findings. (optional)
added_to_task = True # bool | The added to task filter. Filter findings that already have a task assigned. (optional)
filter = ['filter_example'] # list[str] | The finding category and group filter. Notation: category/group. The group part is optional. If a category or group is given, all matching findings will be filtered out and not included in the result. (optional)
invert = True # bool | Whether to invert the category and group filter. (optional)
assessment_filters = ['assessment_filters_example'] # list[str] | The assessment filter. All mentioned assessment colors will be filtered out and not included in the result. (optional)
blacklisted = 'excluded' # str | The blacklist filtering option. (optional) (default to 'excluded')
numeric_delta_only = True # bool | Indicates whether the result should contain the actual delta findings. (optional)

    try:
        # Get finding delta badge
        api_instance.get_finding_delta_badge(project, t1=t1, t2=t2, max_milliseconds=max_milliseconds, uniform_path=uniform_path, t=t, regex=regex, exclude_regex=exclude_regex, added_to_task=added_to_task, filter=filter, invert=invert, assessment_filters=assessment_filters, blacklisted=blacklisted, numeric_delta_only=numeric_delta_only)
    except ApiException as e:
        print("Exception when calling DeltaApi->get_finding_delta_badge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **t1** | **str**| Range start timestamp | [optional] 
 **t2** | **str**| Range end timestamp | [optional] 
 **max_milliseconds** | **int**| Range duration in milliseconds | [optional] [default to -1]
 **uniform_path** | **str**| Uniform path to retrieve data for | [optional] [default to &#39;&#39;]
 **t** | **str**| This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. | [optional] 
 **regex** | **str**| The regex filter. Filters findings by this regex. Considered Fields are Message and Location. Matches will be included in the result. | [optional] 
 **exclude_regex** | **bool**| Whether regex excludes or includes findings. | [optional] 
 **added_to_task** | **bool**| The added to task filter. Filter findings that already have a task assigned. | [optional] 
 **filter** | [**list[str]**](str.md)| The finding category and group filter. Notation: category/group. The group part is optional. If a category or group is given, all matching findings will be filtered out and not included in the result. | [optional] 
 **invert** | **bool**| Whether to invert the category and group filter. | [optional] 
 **assessment_filters** | [**list[str]**](str.md)| The assessment filter. All mentioned assessment colors will be filtered out and not included in the result. | [optional] 
 **blacklisted** | **str**| The blacklist filtering option. | [optional] [default to &#39;excluded&#39;]
 **numeric_delta_only** | **bool**| Indicates whether the result should contain the actual delta findings. | [optional] 

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
**400** | Provided end timestamp is smaller than start timestamp. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | The project does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_element_churn**
> list[TokenElementChurnInfo] get_token_element_churn(project, t1=t1, t2=t2, max_milliseconds=max_milliseconds, uniform_path=uniform_path)

Get token element churn

Provides a token element churn (i.e., the list of changed elements) for a given uniform path and time range. This service is public API since Teamscale 5.9.10. The API requires the user to have View Project permissions on the project.

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
    api_instance = openapi_client.DeltaApi(api_client)
    project = 'project_example' # str | The project alias or id.
t1 = 't1_example' # str | Range start timestamp (optional)
t2 = 't2_example' # str | Range end timestamp (optional)
max_milliseconds = -1 # int | Range duration in milliseconds (optional) (default to -1)
uniform_path = '' # str | Uniform path to retrieve data for (optional) (default to '')

    try:
        # Get token element churn
        api_response = api_instance.get_token_element_churn(project, t1=t1, t2=t2, max_milliseconds=max_milliseconds, uniform_path=uniform_path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeltaApi->get_token_element_churn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **t1** | **str**| Range start timestamp | [optional] 
 **t2** | **str**| Range end timestamp | [optional] 
 **max_milliseconds** | **int**| Range duration in milliseconds | [optional] [default to -1]
 **uniform_path** | **str**| Uniform path to retrieve data for | [optional] [default to &#39;&#39;]

### Return type

[**list[TokenElementChurnInfo]**](TokenElementChurnInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Provided end timestamp is smaller than start timestamp. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | The project does not exist. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

