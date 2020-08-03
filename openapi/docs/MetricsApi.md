# openapi_client.MetricsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_issue_metric_descriptor**](MetricsApi.md#create_issue_metric_descriptor) | **POST** /api/projects/{project}/issues/metrics | Create issue metric
[**get_metric_assessment_with_uniform_path**](MetricsApi.md#get_metric_assessment_with_uniform_path) | **GET** /api/projects/{project}/metric-assessments | Get metric assessment


# **create_issue_metric_descriptor**
> create_issue_metric_descriptor(project, issue_metric_descriptor)

Create issue metric

Creates an issue metric descriptor in the system. This service is public API since Teamscale 6.0. The API requires the user to have Edit Issue Metrics permissions on the project.

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
    api_instance = openapi_client.MetricsApi(api_client)
    project = 'project_example' # str | The project alias or id.
issue_metric_descriptor = openapi_client.IssueMetricDescriptor() # IssueMetricDescriptor | 

    try:
        # Create issue metric
        api_instance.create_issue_metric_descriptor(project, issue_metric_descriptor)
    except ApiException as e:
        print("Exception when calling MetricsApi->create_issue_metric_descriptor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **issue_metric_descriptor** | [**IssueMetricDescriptor**](IssueMetricDescriptor.md)|  | 

### Return type

void (empty response body)

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

# **get_metric_assessment_with_uniform_path**
> list[GroupAssessment] get_metric_assessment_with_uniform_path(project, uniform_path, t=t, configuration_name=configuration_name, baseline=baseline)

Get metric assessment

Provides a list of metrics and their assessment for a given path and threshold configuration This service is public API since Teamscale 6.1. The API requires the user to have View Project permissions on the project.

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
    api_instance = openapi_client.MetricsApi(api_client)
    project = 'project_example' # str | The project alias or id.
uniform_path = 'uniform_path_example' # str | Uniform path of requested file or directory.
t = 't_example' # str | This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. (optional)
configuration_name = 'configuration_name_example' # str | ID of the metric threshold configuration. (optional)
baseline = 'baseline_example' # str | The timestamp used as baseline for trends. If this parameter is missing, no trend is computed. (optional)

    try:
        # Get metric assessment
        api_response = api_instance.get_metric_assessment_with_uniform_path(project, uniform_path, t=t, configuration_name=configuration_name, baseline=baseline)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->get_metric_assessment_with_uniform_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **uniform_path** | **str**| Uniform path of requested file or directory. | 
 **t** | **str**| This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. | [optional] 
 **configuration_name** | **str**| ID of the metric threshold configuration. | [optional] 
 **baseline** | **str**| The timestamp used as baseline for trends. If this parameter is missing, no trend is computed. | [optional] 

### Return type

[**list[GroupAssessment]**](GroupAssessment.md)

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

