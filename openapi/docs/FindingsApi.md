# openapi_client.FindingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_external_analysis_group**](FindingsApi.md#create_external_analysis_group) | **POST** /api/external-findings/groups | Create external analysis group
[**create_external_finding_description**](FindingsApi.md#create_external_finding_description) | **POST** /api/external-findings/descriptions | Create external finding description
[**get_abap_findings**](FindingsApi.md#get_abap_findings) | **GET** /api/projects/{project}/findings/abap/{objectType}/{sourceObject} | Get ABAP findings
[**get_abap_findings1**](FindingsApi.md#get_abap_findings1) | **GET** /api/projects/{project}/findings/abap | Get all ABAP findings
[**get_finding**](FindingsApi.md#get_finding) | **GET** /api/projects/{project}/findings/{id} | Get finding
[**get_finding_delta_badge**](FindingsApi.md#get_finding_delta_badge) | **GET** /api/projects/{project}/findings/delta/badge | Get finding delta badge
[**get_finding_with_diff_info**](FindingsApi.md#get_finding_with_diff_info) | **GET** /api/projects/{project}/findings/{id}/with-diff-info | Get finding with diff information
[**get_findings**](FindingsApi.md#get_findings) | **GET** /api/projects/{project}/findings/list | Get findings
[**get_findings_with_ids**](FindingsApi.md#get_findings_with_ids) | **POST** /api/projects/{project}/findings/list/with-ids | Get findings with provided ids
[**get_issue_finding_badge**](FindingsApi.md#get_issue_finding_badge) | **GET** /api/projects/{project}/issues/{issueId}/findings-badge | Get issue finding badge
[**get_issue_finding_churn**](FindingsApi.md#get_issue_finding_churn) | **GET** /api/projects/{project}/issues/{issueId}/finding-churn | Get issue finding churn
[**mark_findings_false_positive**](FindingsApi.md#mark_findings_false_positive) | **PUT** /api/projects/{project}/findings/false-positive | Mark/unmark false positive findings.
[**mark_findings_tolerated**](FindingsApi.md#mark_findings_tolerated) | **PUT** /api/projects/{project}/findings/tolerated | Mark/unmark tolerated findings.
[**upload_external_findings**](FindingsApi.md#upload_external_findings) | **POST** /api/projects/{project}/external-analysis/session/{sessionId}/external-findings | Upload external findings


# **create_external_analysis_group**
> create_external_analysis_group(external_analysis_group)

Create external analysis group

Creates a new external analysis group. This service is public API since Teamscale 6.0. The API requires the user to have Edit External Findings Schema permissions.

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
    api_instance = openapi_client.FindingsApi(api_client)
    external_analysis_group = openapi_client.ExternalAnalysisGroup() # ExternalAnalysisGroup | 

    try:
        # Create external analysis group
        api_instance.create_external_analysis_group(external_analysis_group)
    except ApiException as e:
        print("Exception when calling FindingsApi->create_external_analysis_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_analysis_group** | [**ExternalAnalysisGroup**](ExternalAnalysisGroup.md)|  | 

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
**400** | Invalid external analysis group provided. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_external_finding_description**
> create_external_finding_description(external_findings_description, analysis_tool=analysis_tool)

Create external finding description

Create a new external finding description in the system. This service is public API since Teamscale 6.0. The API requires the user to have Edit External Findings Schema permissions.

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
    api_instance = openapi_client.FindingsApi(api_client)
    external_findings_description = openapi_client.ExternalFindingsDescription() # ExternalFindingsDescription | 
analysis_tool = 'CUSTOM' # str | Parameter name for specifying the analysis tool used (optional) (default to 'CUSTOM')

    try:
        # Create external finding description
        api_instance.create_external_finding_description(external_findings_description, analysis_tool=analysis_tool)
    except ApiException as e:
        print("Exception when calling FindingsApi->create_external_finding_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_findings_description** | [**ExternalFindingsDescription**](ExternalFindingsDescription.md)|  | 
 **analysis_tool** | **str**| Parameter name for specifying the analysis tool used | [optional] [default to &#39;CUSTOM&#39;]

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
**400** | The given analysis tool is not supported as an external tool for custom findings. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_abap_findings**
> FindingsWithCount get_abap_findings(project, object_type, source_object, t=t, regex=regex, exclude_regex=exclude_regex, added_to_task=added_to_task, filter=filter, invert=invert, assessment_filters=assessment_filters, blacklisted=blacklisted, baseline=baseline, qualified_name=qualified_name, include_changed_code_findings=include_changed_code_findings, blacklist_rationale=blacklist_rationale, sort_by=sort_by, sort_order=sort_order, start=start, max=max, all=all)

Get ABAP findings

Returns findings for an ABAP source object, function group, or project. The element is expected in the form OBJTYPE/OBJNAME, e.g. 'PROG/ZTEST' or 'FUGR/!ABC!MY_FUNCTION_GROUP'. This service is public API since Teamscale 5.6. The API requires the user to have View Project permissions on the project.

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
    api_instance = openapi_client.FindingsApi(api_client)
    project = 'project_example' # str | The project alias or id.
object_type = 'object_type_example' # str | 
source_object = 'source_object_example' # str | 
t = 't_example' # str | This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. (optional)
regex = 'regex_example' # str | The regex filter. Filters findings by this regex. Considered Fields are Message and Location. Matches will be included in the result. (optional)
exclude_regex = True # bool | Whether regex excludes or includes findings. (optional)
added_to_task = True # bool | The added to task filter. Filter findings that already have a task assigned. (optional)
filter = ['filter_example'] # list[str] | The finding category and group filter. Notation: category/group. The group part is optional. If a category or group is given, all matching findings will be filtered out and not included in the result. (optional)
invert = True # bool | Whether to invert the category and group filter. (optional)
assessment_filters = ['assessment_filters_example'] # list[str] | The assessment filter. All mentioned assessment colors will be filtered out and not included in the result. (optional)
blacklisted = 'excluded' # str | The blacklist filtering option. (optional) (default to 'excluded')
baseline = 'baseline_example' # str | The baseline name or baseline timestamp, with regards to which the findings shall be filtered. (optional)
qualified_name = 'qualified_name_example' # str | If this parameter is given, general findings and such covering the specified qualified location are returned. (optional)
include_changed_code_findings = True # bool | If this is true, findings in changed code as included as well. Only used if a baseline is provided as well. (optional)
blacklist_rationale = 'blacklist_rationale_example' # str | A pattern to be matched against the rationale for which the findings was tolerated or marked as false positive. (optional)
sort_by = 'sort_by_example' # str | The finding property by which the result is sorted. If none is given the result is not sorted. One of group, location, message, or a finding property, or random (optional)
sort_order = 'ASCENDING' # str | The sort order (optional) (default to 'ASCENDING')
start = 0 # int | If this parameter is given, the findings returned will start from this index (0 based), i.e. the first start findings in the list (for current sorting) will be skipped. (optional) (default to 0)
max = 300 # int | Limits the number of findings returned. If also the parameter 'all' is used, the limit is ignored. Providing no limit will use the default limit of 300. (optional) (default to 300)
all = True # bool | If this is true, the finding list is not truncated to 300 elements. (optional)

    try:
        # Get ABAP findings
        api_response = api_instance.get_abap_findings(project, object_type, source_object, t=t, regex=regex, exclude_regex=exclude_regex, added_to_task=added_to_task, filter=filter, invert=invert, assessment_filters=assessment_filters, blacklisted=blacklisted, baseline=baseline, qualified_name=qualified_name, include_changed_code_findings=include_changed_code_findings, blacklist_rationale=blacklist_rationale, sort_by=sort_by, sort_order=sort_order, start=start, max=max, all=all)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FindingsApi->get_abap_findings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **object_type** | **str**|  | 
 **source_object** | **str**|  | 
 **t** | **str**| This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. | [optional] 
 **regex** | **str**| The regex filter. Filters findings by this regex. Considered Fields are Message and Location. Matches will be included in the result. | [optional] 
 **exclude_regex** | **bool**| Whether regex excludes or includes findings. | [optional] 
 **added_to_task** | **bool**| The added to task filter. Filter findings that already have a task assigned. | [optional] 
 **filter** | [**list[str]**](str.md)| The finding category and group filter. Notation: category/group. The group part is optional. If a category or group is given, all matching findings will be filtered out and not included in the result. | [optional] 
 **invert** | **bool**| Whether to invert the category and group filter. | [optional] 
 **assessment_filters** | [**list[str]**](str.md)| The assessment filter. All mentioned assessment colors will be filtered out and not included in the result. | [optional] 
 **blacklisted** | **str**| The blacklist filtering option. | [optional] [default to &#39;excluded&#39;]
 **baseline** | **str**| The baseline name or baseline timestamp, with regards to which the findings shall be filtered. | [optional] 
 **qualified_name** | **str**| If this parameter is given, general findings and such covering the specified qualified location are returned. | [optional] 
 **include_changed_code_findings** | **bool**| If this is true, findings in changed code as included as well. Only used if a baseline is provided as well. | [optional] 
 **blacklist_rationale** | **str**| A pattern to be matched against the rationale for which the findings was tolerated or marked as false positive. | [optional] 
 **sort_by** | **str**| The finding property by which the result is sorted. If none is given the result is not sorted. One of group, location, message, or a finding property, or random | [optional] 
 **sort_order** | **str**| The sort order | [optional] [default to &#39;ASCENDING&#39;]
 **start** | **int**| If this parameter is given, the findings returned will start from this index (0 based), i.e. the first start findings in the list (for current sorting) will be skipped. | [optional] [default to 0]
 **max** | **int**| Limits the number of findings returned. If also the parameter &#39;all&#39; is used, the limit is ignored. Providing no limit will use the default limit of 300. | [optional] [default to 300]
 **all** | **bool**| If this is true, the finding list is not truncated to 300 elements. | [optional] 

### Return type

[**FindingsWithCount**](FindingsWithCount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml, application/xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | One of the filter options is invalid. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | The project does not exist. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_abap_findings1**
> FindingsWithCount get_abap_findings1(project, t=t, regex=regex, exclude_regex=exclude_regex, added_to_task=added_to_task, filter=filter, invert=invert, assessment_filters=assessment_filters, blacklisted=blacklisted, baseline=baseline, qualified_name=qualified_name, include_changed_code_findings=include_changed_code_findings, blacklist_rationale=blacklist_rationale, sort_by=sort_by, sort_order=sort_order, start=start, max=max, all=all)

Get all ABAP findings

Returns all findings for the given project. This service is public API since Teamscale 5.6. The API requires the user to have View Project permissions on the project.

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
    api_instance = openapi_client.FindingsApi(api_client)
    project = 'project_example' # str | The project alias or id.
t = 't_example' # str | This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. (optional)
regex = 'regex_example' # str | The regex filter. Filters findings by this regex. Considered Fields are Message and Location. Matches will be included in the result. (optional)
exclude_regex = True # bool | Whether regex excludes or includes findings. (optional)
added_to_task = True # bool | The added to task filter. Filter findings that already have a task assigned. (optional)
filter = ['filter_example'] # list[str] | The finding category and group filter. Notation: category/group. The group part is optional. If a category or group is given, all matching findings will be filtered out and not included in the result. (optional)
invert = True # bool | Whether to invert the category and group filter. (optional)
assessment_filters = ['assessment_filters_example'] # list[str] | The assessment filter. All mentioned assessment colors will be filtered out and not included in the result. (optional)
blacklisted = 'excluded' # str | The blacklist filtering option. (optional) (default to 'excluded')
baseline = 'baseline_example' # str | The baseline name or baseline timestamp, with regards to which the findings shall be filtered. (optional)
qualified_name = 'qualified_name_example' # str | If this parameter is given, general findings and such covering the specified qualified location are returned. (optional)
include_changed_code_findings = True # bool | If this is true, findings in changed code as included as well. Only used if a baseline is provided as well. (optional)
blacklist_rationale = 'blacklist_rationale_example' # str | A pattern to be matched against the rationale for which the findings was tolerated or marked as false positive. (optional)
sort_by = 'sort_by_example' # str | The finding property by which the result is sorted. If none is given the result is not sorted. One of group, location, message, or a finding property, or random (optional)
sort_order = 'ASCENDING' # str | The sort order (optional) (default to 'ASCENDING')
start = 0 # int | If this parameter is given, the findings returned will start from this index (0 based), i.e. the first start findings in the list (for current sorting) will be skipped. (optional) (default to 0)
max = 300 # int | Limits the number of findings returned. If also the parameter 'all' is used, the limit is ignored. Providing no limit will use the default limit of 300. (optional) (default to 300)
all = True # bool | If this is true, the finding list is not truncated to 300 elements. (optional)

    try:
        # Get all ABAP findings
        api_response = api_instance.get_abap_findings1(project, t=t, regex=regex, exclude_regex=exclude_regex, added_to_task=added_to_task, filter=filter, invert=invert, assessment_filters=assessment_filters, blacklisted=blacklisted, baseline=baseline, qualified_name=qualified_name, include_changed_code_findings=include_changed_code_findings, blacklist_rationale=blacklist_rationale, sort_by=sort_by, sort_order=sort_order, start=start, max=max, all=all)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FindingsApi->get_abap_findings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **t** | **str**| This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. | [optional] 
 **regex** | **str**| The regex filter. Filters findings by this regex. Considered Fields are Message and Location. Matches will be included in the result. | [optional] 
 **exclude_regex** | **bool**| Whether regex excludes or includes findings. | [optional] 
 **added_to_task** | **bool**| The added to task filter. Filter findings that already have a task assigned. | [optional] 
 **filter** | [**list[str]**](str.md)| The finding category and group filter. Notation: category/group. The group part is optional. If a category or group is given, all matching findings will be filtered out and not included in the result. | [optional] 
 **invert** | **bool**| Whether to invert the category and group filter. | [optional] 
 **assessment_filters** | [**list[str]**](str.md)| The assessment filter. All mentioned assessment colors will be filtered out and not included in the result. | [optional] 
 **blacklisted** | **str**| The blacklist filtering option. | [optional] [default to &#39;excluded&#39;]
 **baseline** | **str**| The baseline name or baseline timestamp, with regards to which the findings shall be filtered. | [optional] 
 **qualified_name** | **str**| If this parameter is given, general findings and such covering the specified qualified location are returned. | [optional] 
 **include_changed_code_findings** | **bool**| If this is true, findings in changed code as included as well. Only used if a baseline is provided as well. | [optional] 
 **blacklist_rationale** | **str**| A pattern to be matched against the rationale for which the findings was tolerated or marked as false positive. | [optional] 
 **sort_by** | **str**| The finding property by which the result is sorted. If none is given the result is not sorted. One of group, location, message, or a finding property, or random | [optional] 
 **sort_order** | **str**| The sort order | [optional] [default to &#39;ASCENDING&#39;]
 **start** | **int**| If this parameter is given, the findings returned will start from this index (0 based), i.e. the first start findings in the list (for current sorting) will be skipped. | [optional] [default to 0]
 **max** | **int**| Limits the number of findings returned. If also the parameter &#39;all&#39; is used, the limit is ignored. Providing no limit will use the default limit of 300. | [optional] [default to 300]
 **all** | **bool**| If this is true, the finding list is not truncated to 300 elements. | [optional] 

### Return type

[**FindingsWithCount**](FindingsWithCount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml, application/xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | One of the filter options is invalid. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | The project does not exist. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finding**
> TrackedFinding get_finding(project, id, t=t)

Get finding

Retrieves a finding by its ID. This service is public API since Teamscale 5.3. The API requires the user to have View Project permissions on the project.

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
    api_instance = openapi_client.FindingsApi(api_client)
    project = 'project_example' # str | The project alias or id.
id = 'id_example' # str | 
t = 't_example' # str | This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. (optional)

    try:
        # Get finding
        api_response = api_instance.get_finding(project, id, t=t)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FindingsApi->get_finding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **id** | **str**|  | 
 **t** | **str**| This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. | [optional] 

### Return type

[**TrackedFinding**](TrackedFinding.md)

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
    api_instance = openapi_client.FindingsApi(api_client)
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
        print("Exception when calling FindingsApi->get_finding_delta_badge: %s\n" % e)
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

# **get_finding_with_diff_info**
> TrackedFindingWithDiffInfo get_finding_with_diff_info(project, id, t=t)

Get finding with diff information

Retrieves a finding by its ID with additional information on when and where the finding was introduced or removed. This service is public API since Teamscale 5.3. The API requires the user to have View Project permissions on the project.

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
    api_instance = openapi_client.FindingsApi(api_client)
    project = 'project_example' # str | The project alias or id.
id = 'id_example' # str | 
t = 't_example' # str | This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. (optional)

    try:
        # Get finding with diff information
        api_response = api_instance.get_finding_with_diff_info(project, id, t=t)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FindingsApi->get_finding_with_diff_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **id** | **str**|  | 
 **t** | **str**| This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. | [optional] 

### Return type

[**TrackedFindingWithDiffInfo**](TrackedFindingWithDiffInfo.md)

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

# **get_findings**
> list[TrackedFinding] get_findings(project, uniform_path=uniform_path, recursive=recursive, pretty=pretty, t=t, regex=regex, exclude_regex=exclude_regex, added_to_task=added_to_task, filter=filter, invert=invert, assessment_filters=assessment_filters, blacklisted=blacklisted, baseline=baseline, qualified_name=qualified_name, include_changed_code_findings=include_changed_code_findings, blacklist_rationale=blacklist_rationale, sort_by=sort_by, sort_order=sort_order, start=start, max=max, all=all)

Get findings

Gets a list of all findings. Findings can be filtered by path prefix. For recursive queries, these are all findings found in the sub-tree. Filter parameters allow to only retrieve findings in a specific category and/or group. There is an upper limit for the number of returned findings. This service is public API since Teamscale 5.6. The API requires the user to have View Project permissions on the project.

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
    api_instance = openapi_client.FindingsApi(api_client)
    project = 'project_example' # str | The project alias or id.
uniform_path = '' # str | The uniform path for which findings should be retrieved. This can be either a concrete file or a container. In the latter case the recursive parameter can be used to specify whether sub-trees should be considered. (optional) (default to '')
recursive = True # bool | If this parameter is set to 'true', the query is recursive and results for all elements in the sub-tree are returned. (optional)
pretty = True # bool | If this is true, the findings are adjusted to match a pretty printed version of the code. This may not be used together with recursive queries to directories. (optional)
t = openapi_client.FindingsFilterSettings() # FindingsFilterSettings | This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. (optional)
regex = openapi_client.FindingsFilterSettings() # FindingsFilterSettings | The regex filter. Filters findings by this regex. Considered Fields are Message and Location. Matches will be included in the result. (optional)
exclude_regex = openapi_client.FindingsFilterSettings() # FindingsFilterSettings | Whether regex excludes or includes findings. (optional)
added_to_task = openapi_client.FindingsFilterSettings() # FindingsFilterSettings | The added to task filter. Filter findings that already have a task assigned. (optional)
filter = openapi_client.FindingsFilterSettings() # FindingsFilterSettings | The finding category and group filter. Notation: category/group. The group part is optional. If a category or group is given, all matching findings will be filtered out and not included in the result. (optional)
invert = openapi_client.FindingsFilterSettings() # FindingsFilterSettings | Whether to invert the category and group filter. (optional)
assessment_filters = openapi_client.FindingsFilterSettings() # FindingsFilterSettings | The assessment filter. All mentioned assessment colors will be filtered out and not included in the result. (optional)
blacklisted = openapi_client.FindingsFilterSettings() # FindingsFilterSettings | The blacklist filtering option. (optional)
baseline = openapi_client.FindingsFilterSettings() # FindingsFilterSettings | The baseline name or baseline timestamp, with regards to which the findings shall be filtered. (optional)
qualified_name = openapi_client.FindingsFilterSettings() # FindingsFilterSettings | If this parameter is given, general findings and such covering the specified qualified location are returned. (optional)
include_changed_code_findings = openapi_client.FindingsFilterSettings() # FindingsFilterSettings | If this is true, findings in changed code as included as well. Only used if a baseline is provided as well. (optional)
blacklist_rationale = openapi_client.FindingsFilterSettings() # FindingsFilterSettings | A pattern to be matched against the rationale for which the findings was tolerated or marked as false positive. (optional)
sort_by = openapi_client.FindingSortOptions() # FindingSortOptions | The finding property by which the result is sorted. If none is given the result is not sorted. One of group, location, message, or a finding property, or random (optional)
sort_order = openapi_client.FindingSortOptions() # FindingSortOptions | The sort order (optional)
start = openapi_client.FindingsPaginationOptions() # FindingsPaginationOptions | If this parameter is given, the findings returned will start from this index (0 based), i.e. the first start findings in the list (for current sorting) will be skipped. (optional)
max = openapi_client.FindingsPaginationOptions() # FindingsPaginationOptions | Limits the number of findings returned. If also the parameter 'all' is used, the limit is ignored. Providing no limit will use the default limit of 300. (optional)
all = openapi_client.FindingsPaginationOptions() # FindingsPaginationOptions | If this is true, the finding list is not truncated to 300 elements. (optional)

    try:
        # Get findings
        api_response = api_instance.get_findings(project, uniform_path=uniform_path, recursive=recursive, pretty=pretty, t=t, regex=regex, exclude_regex=exclude_regex, added_to_task=added_to_task, filter=filter, invert=invert, assessment_filters=assessment_filters, blacklisted=blacklisted, baseline=baseline, qualified_name=qualified_name, include_changed_code_findings=include_changed_code_findings, blacklist_rationale=blacklist_rationale, sort_by=sort_by, sort_order=sort_order, start=start, max=max, all=all)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FindingsApi->get_findings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **uniform_path** | **str**| The uniform path for which findings should be retrieved. This can be either a concrete file or a container. In the latter case the recursive parameter can be used to specify whether sub-trees should be considered. | [optional] [default to &#39;&#39;]
 **recursive** | **bool**| If this parameter is set to &#39;true&#39;, the query is recursive and results for all elements in the sub-tree are returned. | [optional] 
 **pretty** | **bool**| If this is true, the findings are adjusted to match a pretty printed version of the code. This may not be used together with recursive queries to directories. | [optional] 
 **t** | [**FindingsFilterSettings**](.md)| This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. | [optional] 
 **regex** | [**FindingsFilterSettings**](.md)| The regex filter. Filters findings by this regex. Considered Fields are Message and Location. Matches will be included in the result. | [optional] 
 **exclude_regex** | [**FindingsFilterSettings**](.md)| Whether regex excludes or includes findings. | [optional] 
 **added_to_task** | [**FindingsFilterSettings**](.md)| The added to task filter. Filter findings that already have a task assigned. | [optional] 
 **filter** | [**FindingsFilterSettings**](.md)| The finding category and group filter. Notation: category/group. The group part is optional. If a category or group is given, all matching findings will be filtered out and not included in the result. | [optional] 
 **invert** | [**FindingsFilterSettings**](.md)| Whether to invert the category and group filter. | [optional] 
 **assessment_filters** | [**FindingsFilterSettings**](.md)| The assessment filter. All mentioned assessment colors will be filtered out and not included in the result. | [optional] 
 **blacklisted** | [**FindingsFilterSettings**](.md)| The blacklist filtering option. | [optional] 
 **baseline** | [**FindingsFilterSettings**](.md)| The baseline name or baseline timestamp, with regards to which the findings shall be filtered. | [optional] 
 **qualified_name** | [**FindingsFilterSettings**](.md)| If this parameter is given, general findings and such covering the specified qualified location are returned. | [optional] 
 **include_changed_code_findings** | [**FindingsFilterSettings**](.md)| If this is true, findings in changed code as included as well. Only used if a baseline is provided as well. | [optional] 
 **blacklist_rationale** | [**FindingsFilterSettings**](.md)| A pattern to be matched against the rationale for which the findings was tolerated or marked as false positive. | [optional] 
 **sort_by** | [**FindingSortOptions**](.md)| The finding property by which the result is sorted. If none is given the result is not sorted. One of group, location, message, or a finding property, or random | [optional] 
 **sort_order** | [**FindingSortOptions**](.md)| The sort order | [optional] 
 **start** | [**FindingsPaginationOptions**](.md)| If this parameter is given, the findings returned will start from this index (0 based), i.e. the first start findings in the list (for current sorting) will be skipped. | [optional] 
 **max** | [**FindingsPaginationOptions**](.md)| Limits the number of findings returned. If also the parameter &#39;all&#39; is used, the limit is ignored. Providing no limit will use the default limit of 300. | [optional] 
 **all** | [**FindingsPaginationOptions**](.md)| If this is true, the finding list is not truncated to 300 elements. | [optional] 

### Return type

[**list[TrackedFinding]**](TrackedFinding.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | One of the filter options is invalid. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | The project does not exist. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_findings_with_ids**
> list[TrackedFinding] get_findings_with_ids(project, t=t, request_body=request_body)

Get findings with provided ids

Gets a list of all findings with provided ids. This service is public API since Teamscale 6.0. The API requires the user to have View Project permissions on the project.

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
    api_instance = openapi_client.FindingsApi(api_client)
    project = 'project_example' # str | The project alias or id.
t = 't_example' # str | This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. (optional)
request_body = ['request_body_example'] # list[str] |  (optional)

    try:
        # Get findings with provided ids
        api_response = api_instance.get_findings_with_ids(project, t=t, request_body=request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FindingsApi->get_findings_with_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **t** | **str**| This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. | [optional] 
 **request_body** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**list[TrackedFinding]**](TrackedFinding.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | One of the filter options is invalid. |  -  |
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
    api_instance = openapi_client.FindingsApi(api_client)
    project = 'project_example' # str | The project alias or id.
issue_id = 'issue_id_example' # str | ID of the issue to create a finding badge for

    try:
        # Get issue finding badge
        api_instance.get_issue_finding_badge(project, issue_id)
    except ApiException as e:
        print("Exception when calling FindingsApi->get_issue_finding_badge: %s\n" % e)
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
    api_instance = openapi_client.FindingsApi(api_client)
    project = 'project_example' # str | The project alias or id.
issue_id = 'issue_id_example' # str | ID of the issue to determine the finding churn for

    try:
        # Get issue finding churn
        api_response = api_instance.get_issue_finding_churn(project, issue_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FindingsApi->get_issue_finding_churn: %s\n" % e)
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

# **mark_findings_false_positive**
> mark_findings_false_positive(project, operation, finding_blacklist_request_body, t=t)

Mark/unmark false positive findings.

Marks/unmarks the given findings as false positive. This service is public API since Teamscale 5.7. The API requires the user to have View Project permissions on the project.

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
    api_instance = openapi_client.FindingsApi(api_client)
    project = 'project_example' # str | The project alias or id.
operation = 'operation_example' # str | Request operation to perform (e.g. add or remove blacklisting information).
finding_blacklist_request_body = openapi_client.FindingBlacklistRequestBody() # FindingBlacklistRequestBody | 
t = 't_example' # str | This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. (optional)

    try:
        # Mark/unmark false positive findings.
        api_instance.mark_findings_false_positive(project, operation, finding_blacklist_request_body, t=t)
    except ApiException as e:
        print("Exception when calling FindingsApi->mark_findings_false_positive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **operation** | **str**| Request operation to perform (e.g. add or remove blacklisting information). | 
 **finding_blacklist_request_body** | [**FindingBlacklistRequestBody**](FindingBlacklistRequestBody.md)|  | 
 **t** | **str**| This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. | [optional] 

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
**400** | Requested finding does not belong to false positive findings. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | The project does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_findings_tolerated**
> mark_findings_tolerated(project, operation, finding_blacklist_request_body, t=t)

Mark/unmark tolerated findings.

Marks/unmarks the given findings as tolerated. This service is public API since Teamscale 5.7. The API requires the user to have View Project permissions on the project.

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
    api_instance = openapi_client.FindingsApi(api_client)
    project = 'project_example' # str | The project alias or id.
operation = 'operation_example' # str | Request operation to perform (e.g. add or remove blacklisting information).
finding_blacklist_request_body = openapi_client.FindingBlacklistRequestBody() # FindingBlacklistRequestBody | 
t = 't_example' # str | This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. (optional)

    try:
        # Mark/unmark tolerated findings.
        api_instance.mark_findings_tolerated(project, operation, finding_blacklist_request_body, t=t)
    except ApiException as e:
        print("Exception when calling FindingsApi->mark_findings_tolerated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **operation** | **str**| Request operation to perform (e.g. add or remove blacklisting information). | 
 **finding_blacklist_request_body** | [**FindingBlacklistRequestBody**](FindingBlacklistRequestBody.md)|  | 
 **t** | **str**| This parameter can be used to pass a timestamp giving the time (in milliseconds since 1970) for which the data should be provided. This can optionally be prefixed by the name of the branch, followed by a colon. | [optional] 

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
**400** | Requested finding does not belong to tolerated findings. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | The project does not exist. |  -  |

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
    api_instance = openapi_client.FindingsApi(api_client)
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
        print("Exception when calling FindingsApi->upload_external_findings: %s\n" % e)
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

