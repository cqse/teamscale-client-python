# openapi_client.ExternalAnalysisApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commit_analysis_results**](ExternalAnalysisApi.md#commit_analysis_results) | **POST** /api/projects/{project}/external-analysis/session/{sessionId} | Commit session
[**create_session**](ExternalAnalysisApi.md#create_session) | **POST** /api/projects/{project}/external-analysis/session | Get session ID
[**delete_analysis_results**](ExternalAnalysisApi.md#delete_analysis_results) | **DELETE** /api/projects/{project}/external-analysis/session/{sessionId} | Delete session
[**get_source_map**](ExternalAnalysisApi.md#get_source_map) | **GET** /api/projects/{project}/javascript-source-maps | Get source map
[**upload_debug_info**](ExternalAnalysisApi.md#upload_debug_info) | **POST** /api/projects/{project}/external-analysis/dotnet-debug-info | Upload debug info
[**upload_dot_net_ephemeral_trace**](ExternalAnalysisApi.md#upload_dot_net_ephemeral_trace) | **POST** /api/projects/{project}/external-analysis/dotnet-ephemeral-trace | Upload .NET ephemeral profiler coverage
[**upload_external_analysis_results**](ExternalAnalysisApi.md#upload_external_analysis_results) | **POST** /api/projects/{project}/external-analysis/session/{sessionId}/external-analysis-import-infos | Upload external analysis results
[**upload_external_findings**](ExternalAnalysisApi.md#upload_external_findings) | **POST** /api/projects/{project}/external-analysis/session/{sessionId}/external-findings | Upload external findings
[**upload_external_metrics**](ExternalAnalysisApi.md#upload_external_metrics) | **POST** /api/projects/{project}/external-analysis/session/{sessionId}/external-metrics | Upload external metrics
[**upload_istanbul_source_mapped_coverage**](ExternalAnalysisApi.md#upload_istanbul_source_mapped_coverage) | **POST** /api/projects/{project}/external-analysis/istanbul-test-coverage | Upload Istanbul-based coverage
[**upload_non_code_metrics**](ExternalAnalysisApi.md#upload_non_code_metrics) | **POST** /api/projects/{project}/external-analysis/session/{sessionId}/non-code-metrics | Upload non-code metrics
[**upload_report**](ExternalAnalysisApi.md#upload_report) | **POST** /api/projects/{project}/external-analysis/session/{sessionId}/report | Upload external report(s)
[**upload_source_maps**](ExternalAnalysisApi.md#upload_source_maps) | **POST** /api/projects/{project}/javascript-source-maps | Upload source map


# **commit_analysis_results**
> commit_analysis_results(project, session_id)

Commit session

Commits and closes the given session. This service is public API since Teamscale 5.9. The API requires the user to have Perform External Uploads permissions on the project.

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
    api_instance = openapi_client.ExternalAnalysisApi(api_client)
    project = 'project_example' # str | The project alias or id.
session_id = 'session_id_example' # str | If session ID is provided, the results will be appended to the given session instead of creating a new session. Use \"auto-create\" in place of session ID to create a new session, perform upload and commit session in one step.

    try:
        # Commit session
        api_instance.commit_analysis_results(project, session_id)
    except ApiException as e:
        print("Exception when calling ExternalAnalysisApi->commit_analysis_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **session_id** | **str**| If session ID is provided, the results will be appended to the given session instead of creating a new session. Use \&quot;auto-create\&quot; in place of session ID to create a new session, perform upload and commit session in one step. | 

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

# **create_session**
> str create_session(project, t=t, revision=revision, repository=repository, message=message, partition=partition, movetolastcommit=movetolastcommit)

Get session ID

Obtains a new session ID. Using session ID allows to perform external uploads in multiple calls that all belong to the same session. This service is public API since Teamscale 5.9. The API requires the user to have Perform External Uploads permissions on the project.

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
    api_instance = openapi_client.ExternalAnalysisApi(api_client)
    project = 'project_example' # str | The project alias or id.
t = 't_example' # str | This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. (optional)
revision = 'revision_example' # str | This parameter allows to pass a revision instead of a timestamp. (optional)
repository = 'repository_example' # str | This parameter allows to pass a repository name (optional)
message = 'External analysis data upload' # str | A message that describes the external analysis, similar to a commit message. (optional) (default to 'External analysis data upload')
partition = 'partition_example' # str | The name of the logical partition to store the results into. All existing data in this partition will be invalidated. A partition typically corresponds to one analysis run, i.e. if there are two independent builds/runs, they must use different partitions. (optional)
movetolastcommit = True # bool | Whether to move the upload timestamp to right after the last commit. (optional)

    try:
        # Get session ID
        api_response = api_instance.create_session(project, t=t, revision=revision, repository=repository, message=message, partition=partition, movetolastcommit=movetolastcommit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExternalAnalysisApi->create_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **t** | **str**| This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. | [optional] 
 **revision** | **str**| This parameter allows to pass a revision instead of a timestamp. | [optional] 
 **repository** | **str**| This parameter allows to pass a repository name | [optional] 
 **message** | **str**| A message that describes the external analysis, similar to a commit message. | [optional] [default to &#39;External analysis data upload&#39;]
 **partition** | **str**| The name of the logical partition to store the results into. All existing data in this partition will be invalidated. A partition typically corresponds to one analysis run, i.e. if there are two independent builds/runs, they must use different partitions. | [optional] 
 **movetolastcommit** | **bool**| Whether to move the upload timestamp to right after the last commit. | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Upload was rejected, because it refers to a timestamp too far back in time. |  -  |
**404** | The project does not exist. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_analysis_results**
> delete_analysis_results(project, session_id)

Delete session

Deletes a session in case of abortion. This service is public API since Teamscale 5.9. The API requires the user to have Perform External Uploads permissions on the project.

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
    api_instance = openapi_client.ExternalAnalysisApi(api_client)
    project = 'project_example' # str | The project alias or id.
session_id = 'session_id_example' # str | If session ID is provided, the results will be appended to the given session instead of creating a new session. Use \"auto-create\" in place of session ID to create a new session, perform upload and commit session in one step.

    try:
        # Delete session
        api_instance.delete_analysis_results(project, session_id)
    except ApiException as e:
        print("Exception when calling ExternalAnalysisApi->delete_analysis_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **session_id** | **str**| If session ID is provided, the results will be appended to the given session instead of creating a new session. Use \&quot;auto-create\&quot; in place of session ID to create a new session, perform upload and commit session in one step. | 

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

# **get_source_map**
> JavaScriptSourceMap get_source_map(project, t, version, generated_file)

Get source map

Retrieves the javascript source map stored for an application version and generated file. This service is public API since Teamscale 5.9. The API requires the user to have Perform External Uploads permissions on the project.

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
    api_instance = openapi_client.ExternalAnalysisApi(api_client)
    project = 'project_example' # str | The project alias or id.
t = 't_example' # str | This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon.
version = 'version_example' # str | The application version to which the uploaded mappings belong
generated_file = 'generated_file_example' # str | The name of the generated source file whose mappings should be returned

    try:
        # Get source map
        api_response = api_instance.get_source_map(project, t, version, generated_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExternalAnalysisApi->get_source_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **t** | **str**| This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. | 
 **version** | **str**| The application version to which the uploaded mappings belong | 
 **generated_file** | **str**| The name of the generated source file whose mappings should be returned | 

### Return type

[**JavaScriptSourceMap**](JavaScriptSourceMap.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | No upload for given commit, the CQSE JavaScript Profiler is probably not enabled as a Test Coverage tool. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | The project does not exist. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_debug_info**
> upload_debug_info(project, version, t=t, file=file)

Upload debug info

Uploads PDB or MDB files for analysis. Processes an upload of method mapping information. This service is public API since Teamscale 5.9. The API requires the user to have Perform External Uploads permissions on the project.

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
    api_instance = openapi_client.ExternalAnalysisApi(api_client)
    project = 'project_example' # str | The project alias or id.
version = 'version_example' # str | The parameter that contains the program version to which the uploaded coverage belongs.
t = 't_example' # str | This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. (optional)
file = '/path/to/file' # list[file] |  (optional)

    try:
        # Upload debug info
        api_instance.upload_debug_info(project, version, t=t, file=file)
    except ApiException as e:
        print("Exception when calling ExternalAnalysisApi->upload_debug_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **version** | **str**| The parameter that contains the program version to which the uploaded coverage belongs. | 
 **t** | **str**| This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. | [optional] 
 **file** | **list[file]**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | The project does not exist. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_dot_net_ephemeral_trace**
> upload_dot_net_ephemeral_trace(project, version, partition, t=t, message=message, report=report)

Upload .NET ephemeral profiler coverage

Imports coverage information from the .NET ephemeral profiler (profiles only on the method level). This service is public API since Teamscale 5.9. The API requires the user to have Perform External Uploads permissions on the project.

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
    api_instance = openapi_client.ExternalAnalysisApi(api_client)
    project = 'project_example' # str | The project alias or id.
version = 'version_example' # str | The parameter that contains the program version to which the uploaded coverage belongs.
partition = 'partition_example' # str | The name of the logical partition to store the results into. All existing data in this partition will be invalidated. A partition typically corresponds to one analysis run, i.e. if there are two independent builds/runs, they must use different partitions.
t = 't_example' # str | This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. (optional)
message = 'External analysis data upload' # str | A message that describes the external analysis, similar to a commit message. (optional) (default to 'External analysis data upload')
report = '/path/to/file' # list[file] |  (optional)

    try:
        # Upload .NET ephemeral profiler coverage
        api_instance.upload_dot_net_ephemeral_trace(project, version, partition, t=t, message=message, report=report)
    except ApiException as e:
        print("Exception when calling ExternalAnalysisApi->upload_dot_net_ephemeral_trace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **version** | **str**| The parameter that contains the program version to which the uploaded coverage belongs. | 
 **partition** | **str**| The name of the logical partition to store the results into. All existing data in this partition will be invalidated. A partition typically corresponds to one analysis run, i.e. if there are two independent builds/runs, they must use different partitions. | 
 **t** | **str**| This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. | [optional] 
 **message** | **str**| A message that describes the external analysis, similar to a commit message. | [optional] [default to &#39;External analysis data upload&#39;]
 **report** | **list[file]**|  | [optional] 

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
**400** | No reports provided via the report multi-part form data parameter |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | The project does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_external_analysis_results**
> upload_external_analysis_results(project, session_id, external_analysis_import_infos, t=t, revision=revision, repository=repository, message=message, partition=partition, movetolastcommit=movetolastcommit)

Upload external analysis results

Adds external analysis results to the session. For performance reasons, it is recommended to batch calls to this service, i.e. not commit all files using single calls. This service is public API since Teamscale 5.9. The API requires the user to have Perform External Uploads permissions on the project.

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
    api_instance = openapi_client.ExternalAnalysisApi(api_client)
    project = 'project_example' # str | The project alias or id.
session_id = 'session_id_example' # str | If session ID is provided, the results will be appended to the given session instead of creating a new session. Use \"auto-create\" in place of session ID to create a new session, perform upload and commit session in one step.
external_analysis_import_infos = openapi_client.ExternalAnalysisImportInfos() # ExternalAnalysisImportInfos | 
t = 't_example' # str | This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. (optional)
revision = 'revision_example' # str | This parameter allows to pass a revision instead of a timestamp. (optional)
repository = 'repository_example' # str | This parameter allows to pass a repository name (optional)
message = 'External analysis data upload' # str | A message that describes the external analysis, similar to a commit message. (optional) (default to 'External analysis data upload')
partition = 'partition_example' # str | The name of the logical partition to store the results into. All existing data in this partition will be invalidated. A partition typically corresponds to one analysis run, i.e. if there are two independent builds/runs, they must use different partitions. (optional)
movetolastcommit = True # bool | Whether to move the upload timestamp to right after the last commit. (optional)

    try:
        # Upload external analysis results
        api_instance.upload_external_analysis_results(project, session_id, external_analysis_import_infos, t=t, revision=revision, repository=repository, message=message, partition=partition, movetolastcommit=movetolastcommit)
    except ApiException as e:
        print("Exception when calling ExternalAnalysisApi->upload_external_analysis_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **session_id** | **str**| If session ID is provided, the results will be appended to the given session instead of creating a new session. Use \&quot;auto-create\&quot; in place of session ID to create a new session, perform upload and commit session in one step. | 
 **external_analysis_import_infos** | [**ExternalAnalysisImportInfos**](ExternalAnalysisImportInfos.md)|  | 
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
**400** | Session has been committed or deleted. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_external_findings**
> upload_external_findings(project, session_id, external_finding_file_data, t=t, revision=revision, repository=repository, message=message, partition=partition, movetolastcommit=movetolastcommit)

Upload external findings

Adds external findings to the session. For performance reasons, it is recommended to batch calls to this service, i.e. not commit all files using single calls. This service is public API since Teamscale 5.9. The API requires the user to have Perform External Uploads permissions on the project.

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
    api_instance = openapi_client.ExternalAnalysisApi(api_client)
    project = 'project_example' # str | The project alias or id.
session_id = 'session_id_example' # str | If session ID is provided, the results will be appended to the given session instead of creating a new session. Use \"auto-create\" in place of session ID to create a new session, perform upload and commit session in one step.
external_finding_file_data = [openapi_client.ExternalFindingFileData()] # list[ExternalFindingFileData] | 
t = 't_example' # str | This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. (optional)
revision = 'revision_example' # str | This parameter allows to pass a revision instead of a timestamp. (optional)
repository = 'repository_example' # str | This parameter allows to pass a repository name (optional)
message = 'External analysis data upload' # str | A message that describes the external analysis, similar to a commit message. (optional) (default to 'External analysis data upload')
partition = 'partition_example' # str | The name of the logical partition to store the results into. All existing data in this partition will be invalidated. A partition typically corresponds to one analysis run, i.e. if there are two independent builds/runs, they must use different partitions. (optional)
movetolastcommit = True # bool | Whether to move the upload timestamp to right after the last commit. (optional)

    try:
        # Upload external findings
        api_instance.upload_external_findings(project, session_id, external_finding_file_data, t=t, revision=revision, repository=repository, message=message, partition=partition, movetolastcommit=movetolastcommit)
    except ApiException as e:
        print("Exception when calling ExternalAnalysisApi->upload_external_findings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **session_id** | **str**| If session ID is provided, the results will be appended to the given session instead of creating a new session. Use \&quot;auto-create\&quot; in place of session ID to create a new session, perform upload and commit session in one step. | 
 **external_finding_file_data** | [**list[ExternalFindingFileData]**](ExternalFindingFileData.md)|  | 
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
**400** | Failed to parse provided report. |  -  |
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
    api_instance = openapi_client.ExternalAnalysisApi(api_client)
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
        print("Exception when calling ExternalAnalysisApi->upload_external_metrics: %s\n" % e)
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

# **upload_istanbul_source_mapped_coverage**
> upload_istanbul_source_mapped_coverage(project, version, partition, istanbul_json, t=t, message=message)

Upload Istanbul-based coverage

Uploads coverage information from the Istanbul-based TGA profiler. Performs resolution of line numbers based on uploaded source maps. This service is public API since Teamscale 5.9. The API requires the user to have Perform External Uploads permissions on the project.

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
    api_instance = openapi_client.ExternalAnalysisApi(api_client)
    project = 'project_example' # str | The project alias or id.
version = 'version_example' # str | The parameter that contains the program version to which the uploaded coverage belongs.
partition = 'partition_example' # str | The name of the logical partition to store the results into. All existing data in this partition will be invalidated. A partition typically corresponds to one analysis run, i.e. if there are two independent builds/runs, they must use different partitions.
istanbul_json = openapi_client.IstanbulJson() # IstanbulJson | 
t = 't_example' # str | This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. (optional)
message = 'External analysis data upload' # str | A message that describes the external analysis, similar to a commit message. (optional) (default to 'External analysis data upload')

    try:
        # Upload Istanbul-based coverage
        api_instance.upload_istanbul_source_mapped_coverage(project, version, partition, istanbul_json, t=t, message=message)
    except ApiException as e:
        print("Exception when calling ExternalAnalysisApi->upload_istanbul_source_mapped_coverage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **version** | **str**| The parameter that contains the program version to which the uploaded coverage belongs. | 
 **partition** | **str**| The name of the logical partition to store the results into. All existing data in this partition will be invalidated. A partition typically corresponds to one analysis run, i.e. if there are two independent builds/runs, they must use different partitions. | 
 **istanbul_json** | [**IstanbulJson**](IstanbulJson.md)|  | 
 **t** | **str**| This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. | [optional] 
 **message** | **str**| A message that describes the external analysis, similar to a commit message. | [optional] [default to &#39;External analysis data upload&#39;]

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
**400** | Upload failed. Probably the CQSE JavaScript Profiler is not enabled as a Test Coverage tool. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | The project does not exist. |  -  |

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
    api_instance = openapi_client.ExternalAnalysisApi(api_client)
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
        print("Exception when calling ExternalAnalysisApi->upload_non_code_metrics: %s\n" % e)
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

# **upload_report**
> upload_report(project, session_id, format, t=t, revision=revision, repository=repository, message=message, partition=partition, movetolastcommit=movetolastcommit, path_prefix=path_prefix, report=report)

Upload external report(s)

Adds external reports to the session. For performance reasons, it is recommended to batch calls to this service, i.e. not commit all files using single calls. This service is public API since Teamscale 5.9. The API requires the user to have Perform External Uploads permissions on the project.

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
    api_instance = openapi_client.ExternalAnalysisApi(api_client)
    project = 'project_example' # str | The project alias or id.
session_id = 'session_id_example' # str | If session ID is provided, the results will be appended to the given session instead of creating a new session. Use \"auto-create\" in place of session ID to create a new session, perform upload and commit session in one step.
format = 'format_example' # str | The format of the uploaded report.
t = 't_example' # str | This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. (optional)
revision = 'revision_example' # str | This parameter allows to pass a revision instead of a timestamp. (optional)
repository = 'repository_example' # str | This parameter allows to pass a repository name (optional)
message = 'External analysis data upload' # str | A message that describes the external analysis, similar to a commit message. (optional) (default to 'External analysis data upload')
partition = 'partition_example' # str | The name of the logical partition to store the results into. All existing data in this partition will be invalidated. A partition typically corresponds to one analysis run, i.e. if there are two independent builds/runs, they must use different partitions. (optional)
movetolastcommit = True # bool | Whether to move the upload timestamp to right after the last commit. (optional)
path_prefix = 'path_prefix_example' # str | The path prefix for the uploaded test artifacts. (optional)
report = '/path/to/file' # list[file] |  (optional)

    try:
        # Upload external report(s)
        api_instance.upload_report(project, session_id, format, t=t, revision=revision, repository=repository, message=message, partition=partition, movetolastcommit=movetolastcommit, path_prefix=path_prefix, report=report)
    except ApiException as e:
        print("Exception when calling ExternalAnalysisApi->upload_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **session_id** | **str**| If session ID is provided, the results will be appended to the given session instead of creating a new session. Use \&quot;auto-create\&quot; in place of session ID to create a new session, perform upload and commit session in one step. | 
 **format** | **str**| The format of the uploaded report. | 
 **t** | **str**| This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. | [optional] 
 **revision** | **str**| This parameter allows to pass a revision instead of a timestamp. | [optional] 
 **repository** | **str**| This parameter allows to pass a repository name | [optional] 
 **message** | **str**| A message that describes the external analysis, similar to a commit message. | [optional] [default to &#39;External analysis data upload&#39;]
 **partition** | **str**| The name of the logical partition to store the results into. All existing data in this partition will be invalidated. A partition typically corresponds to one analysis run, i.e. if there are two independent builds/runs, they must use different partitions. | [optional] 
 **movetolastcommit** | **bool**| Whether to move the upload timestamp to right after the last commit. | [optional] 
 **path_prefix** | **str**| The path prefix for the uploaded test artifacts. | [optional] 
 **report** | **list[file]**|  | [optional] 

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
**404** | The project does not exist. |  -  |
**400** | The required analyses or tools for the external upload of the report are enabled. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_source_maps**
> upload_source_maps(project, t, version, java_script_source_map)

Upload source map

Uploads javascript source maps for an application version. This service is public API since Teamscale 5.9. The API requires the user to have Perform External Uploads permissions on the project.

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
    api_instance = openapi_client.ExternalAnalysisApi(api_client)
    project = 'project_example' # str | The project alias or id.
t = 't_example' # str | This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon.
version = 'version_example' # str | The application version to which the uploaded mappings belong
java_script_source_map = openapi_client.JavaScriptSourceMap() # JavaScriptSourceMap | Source mapping files to be stored

    try:
        # Upload source map
        api_instance.upload_source_maps(project, t, version, java_script_source_map)
    except ApiException as e:
        print("Exception when calling ExternalAnalysisApi->upload_source_maps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **t** | **str**| This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. | 
 **version** | **str**| The application version to which the uploaded mappings belong | 
 **java_script_source_map** | [**JavaScriptSourceMap**](JavaScriptSourceMap.md)| Source mapping files to be stored | 

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
**400** | Deserialization of the uploaded source map(s) failed. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | The project does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

