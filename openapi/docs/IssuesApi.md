# openapi_client.IssuesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_issue_metric_descriptor**](IssuesApi.md#create_issue_metric_descriptor) | **POST** /api/projects/{project}/issues/metrics | Create issue metric
[**get_issue_finding_badge**](IssuesApi.md#get_issue_finding_badge) | **GET** /api/projects/{project}/issues/{issueId}/findings-badge | Get issue finding badge
[**get_issue_finding_churn**](IssuesApi.md#get_issue_finding_churn) | **GET** /api/projects/{project}/issues/{issueId}/finding-churn | Get issue finding churn


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
    api_instance = openapi_client.IssuesApi(api_client)
    project = 'project_example' # str | The project alias or id.
issue_metric_descriptor = openapi_client.IssueMetricDescriptor() # IssueMetricDescriptor | 

    try:
        # Create issue metric
        api_instance.create_issue_metric_descriptor(project, issue_metric_descriptor)
    except ApiException as e:
        print("Exception when calling IssuesApi->create_issue_metric_descriptor: %s\n" % e)
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

# **get_issue_finding_badge**
> get_issue_finding_badge(project, issue_id)

Get issue finding badge

Creates a finding badge for the given issue. This service is public API since Teamscale 5.9. The API requires the user to have View Project permissions on the project.

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
    api_instance = openapi_client.IssuesApi(api_client)
    project = 'project_example' # str | The project alias or id.
issue_id = 'issue_id_example' # str | ID of the issue to create a finding badge for

    try:
        # Get issue finding badge
        api_instance.get_issue_finding_badge(project, issue_id)
    except ApiException as e:
        print("Exception when calling IssuesApi->get_issue_finding_badge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **issue_id** | **str**| ID of the issue to create a finding badge for | 

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

# **get_issue_finding_churn**
> FindingChurnList get_issue_finding_churn(project, issue_id)

Get issue finding churn

Determines an aggregated finding churn across all commits of the issue. This service is public API since Teamscale 5.9. The API requires the user to have View Project permissions on the project.

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
    api_instance = openapi_client.IssuesApi(api_client)
    project = 'project_example' # str | The project alias or id.
issue_id = 'issue_id_example' # str | ID of the issue to determine the finding churn for

    try:
        # Get issue finding churn
        api_response = api_instance.get_issue_finding_churn(project, issue_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IssuesApi->get_issue_finding_churn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **issue_id** | **str**| ID of the issue to determine the finding churn for | 

### Return type

[**FindingChurnList**](FindingChurnList.md)

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

