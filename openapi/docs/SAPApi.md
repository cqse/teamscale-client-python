# openapi_client.SAPApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_abap_findings**](SAPApi.md#get_abap_findings) | **GET** /api/projects/{project}/findings/abap/{objectType}/{sourceObject} | Get ABAP findings
[**get_abap_findings1**](SAPApi.md#get_abap_findings1) | **GET** /api/projects/{project}/findings/abap | Get all ABAP findings
[**lookup_project_by_sap_system_id**](SAPApi.md#lookup_project_by_sap_system_id) | **GET** /api/projects-by-sap-system-id/{sap-system-id} | Get projects corresponding to given SAP system ID.


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
    api_instance = openapi_client.SAPApi(api_client)
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
        print("Exception when calling SAPApi->get_abap_findings: %s\n" % e)
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
    api_instance = openapi_client.SAPApi(api_client)
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
        print("Exception when calling SAPApi->get_abap_findings1: %s\n" % e)
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

# **lookup_project_by_sap_system_id**
> list[str] lookup_project_by_sap_system_id(sap_system_id)

Get projects corresponding to given SAP system ID.

Looks up Teamscale projects by SAP System ID. Returns project aliases or project IDs if no alias available. This service is public API since Teamscale 5.7. The service will only search among projects visible to current user.

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
    api_instance = openapi_client.SAPApi(api_client)
    sap_system_id = 'sap_system_id_example' # str | System ID of SAP system

    try:
        # Get projects corresponding to given SAP system ID.
        api_response = api_instance.lookup_project_by_sap_system_id(sap_system_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SAPApi->lookup_project_by_sap_system_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sap_system_id** | **str**| System ID of SAP system | 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

