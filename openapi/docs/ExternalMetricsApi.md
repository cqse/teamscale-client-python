# openapi_client.ExternalMetricsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_external_metrics**](ExternalMetricsApi.md#add_external_metrics) | **POST** /api/external-metrics | Add metrics
[**upload_external_metrics**](ExternalMetricsApi.md#upload_external_metrics) | **POST** /api/projects/{project}/external-analysis/session/{sessionId}/external-metrics | Upload external metrics
[**upload_non_code_metrics**](ExternalMetricsApi.md#upload_non_code_metrics) | **POST** /api/projects/{project}/external-analysis/session/{sessionId}/non-code-metrics | Upload non-code metrics


# **add_external_metrics**
> add_external_metrics(metric_schema_change_entry)

Add metrics

Adds a set of external metrics to the schema. This service is public API since Teamscale 5.8. The API requires the user to have Edit External Metrics Schema permissions.

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
    api_instance = openapi_client.ExternalMetricsApi(api_client)
    metric_schema_change_entry = [openapi_client.MetricSchemaChangeEntry()] # list[MetricSchemaChangeEntry] | 

    try:
        # Add metrics
        api_instance.add_external_metrics(metric_schema_change_entry)
    except ApiException as e:
        print("Exception when calling ExternalMetricsApi->add_external_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_schema_change_entry** | [**list[MetricSchemaChangeEntry]**](MetricSchemaChangeEntry.md)|  | 

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
**400** | Invalid external metric description. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_external_metrics**
> upload_external_metrics(project, session_id, external_metrics_entry, t=t, revision=revision, repository=repository, message=message, partition=partition, movetolastcommit=movetolastcommit)

Upload external metrics

Adds external metrics to the session. For performance reasons, it is recommended to batch calls to this service, i.e. not commit all files using single calls. This service is public API since Teamscale 5.9. The API requires the user to have Perform External Uploads permissions on the project.

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
    api_instance = openapi_client.ExternalMetricsApi(api_client)
    project = 'project_example' # str | The project alias or id.
session_id = 'session_id_example' # str | If session ID is provided, the results will be appended to the given session instead of creating a new session. Use \"auto-create\" in place of session ID to create a new session, perform upload and commit session in one step.
external_metrics_entry = [openapi_client.ExternalMetricsEntry()] # list[ExternalMetricsEntry] | 
t = 't_example' # str | This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. (optional)
revision = 'revision_example' # str | This parameter allows to pass a revision instead of a timestamp. (optional)
repository = 'repository_example' # str | This parameter allows to pass a repository name (optional)
message = 'External analysis data upload' # str | A message that describes the external analysis, similar to a commit message. (optional) (default to 'External analysis data upload')
partition = 'partition_example' # str | The name of the logical partition to store the results into. All existing data in this partition will be invalidated. A partition typically corresponds to one analysis run, i.e. if there are two independent builds/runs, they must use different partitions. (optional)
movetolastcommit = True # bool | Whether to move the upload timestamp to right after the last commit. (optional)

    try:
        # Upload external metrics
        api_instance.upload_external_metrics(project, session_id, external_metrics_entry, t=t, revision=revision, repository=repository, message=message, partition=partition, movetolastcommit=movetolastcommit)
    except ApiException as e:
        print("Exception when calling ExternalMetricsApi->upload_external_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **session_id** | **str**| If session ID is provided, the results will be appended to the given session instead of creating a new session. Use \&quot;auto-create\&quot; in place of session ID to create a new session, perform upload and commit session in one step. | 
 **external_metrics_entry** | [**list[ExternalMetricsEntry]**](ExternalMetricsEntry.md)|  | 
 **t** | **str**| This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. | [optional] 
 **revision** | **str**| This parameter allows to pass a revision instead of a timestamp. | [optional] 
 **repository** | **str**| This parameter allows to pass a repository name | [optional] 
 **message** | **str**| A message that describes the external analysis, similar to a commit message. | [optional] [default to &#39;External analysis data upload&#39;]
 **partition** | **str**| The name of the logical partition to store the results into. All existing data in this partition will be invalidated. A partition typically corresponds to one analysis run, i.e. if there are two independent builds/runs, they must use different partitions. | [optional] 
 **movetolastcommit** | **bool**| Whether to move the upload timestamp to right after the last commit. | [optional] 

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
**404** | The project does not exist. |  -  |
**400** | Upload of non-numeric value as component type for assessment metric is not supported. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_non_code_metrics**
> upload_non_code_metrics(project, session_id, non_code_metrics_entry, t=t, revision=revision, repository=repository, message=message, partition=partition, movetolastcommit=movetolastcommit)

Upload non-code metrics

Adds non-code metrics to the session. For performance reasons, it is recommended to batch calls to this service, i.e. not commit all files using single calls. This service is public API since Teamscale 5.9. The API requires the user to have Perform External Uploads permissions on the project.

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
    api_instance = openapi_client.ExternalMetricsApi(api_client)
    project = 'project_example' # str | The project alias or id.
session_id = 'session_id_example' # str | If session ID is provided, the results will be appended to the given session instead of creating a new session. Use \"auto-create\" in place of session ID to create a new session, perform upload and commit session in one step.
non_code_metrics_entry = [openapi_client.NonCodeMetricsEntry()] # list[NonCodeMetricsEntry] | 
t = 't_example' # str | This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. (optional)
revision = 'revision_example' # str | This parameter allows to pass a revision instead of a timestamp. (optional)
repository = 'repository_example' # str | This parameter allows to pass a repository name (optional)
message = 'External analysis data upload' # str | A message that describes the external analysis, similar to a commit message. (optional) (default to 'External analysis data upload')
partition = 'partition_example' # str | The name of the logical partition to store the results into. All existing data in this partition will be invalidated. A partition typically corresponds to one analysis run, i.e. if there are two independent builds/runs, they must use different partitions. (optional)
movetolastcommit = True # bool | Whether to move the upload timestamp to right after the last commit. (optional)

    try:
        # Upload non-code metrics
        api_instance.upload_non_code_metrics(project, session_id, non_code_metrics_entry, t=t, revision=revision, repository=repository, message=message, partition=partition, movetolastcommit=movetolastcommit)
    except ApiException as e:
        print("Exception when calling ExternalMetricsApi->upload_non_code_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **session_id** | **str**| If session ID is provided, the results will be appended to the given session instead of creating a new session. Use \&quot;auto-create\&quot; in place of session ID to create a new session, perform upload and commit session in one step. | 
 **non_code_metrics_entry** | [**list[NonCodeMetricsEntry]**](NonCodeMetricsEntry.md)|  | 
 **t** | **str**| This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. | [optional] 
 **revision** | **str**| This parameter allows to pass a revision instead of a timestamp. | [optional] 
 **repository** | **str**| This parameter allows to pass a repository name | [optional] 
 **message** | **str**| A message that describes the external analysis, similar to a commit message. | [optional] [default to &#39;External analysis data upload&#39;]
 **partition** | **str**| The name of the logical partition to store the results into. All existing data in this partition will be invalidated. A partition typically corresponds to one analysis run, i.e. if there are two independent builds/runs, they must use different partitions. | [optional] 
 **movetolastcommit** | **bool**| Whether to move the upload timestamp to right after the last commit. | [optional] 

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
**400** | Invalid content provided. |  -  |
**404** | The project does not exist. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

