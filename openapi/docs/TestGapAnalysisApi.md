# openapi_client.TestGapAnalysisApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tga_percentage**](TestGapAnalysisApi.md#get_tga_percentage) | **GET** /api/projects/{project}/test-gaps/percentage | Get test gap percentage
[**post_tga_percentage**](TestGapAnalysisApi.md#post_tga_percentage) | **POST** /api/projects/{project}/test-gaps/percentage | Get test gap percentage


# **get_tga_percentage**
> float get_tga_percentage(project, auto_select_branch=auto_select_branch, branch_name=branch_name, include_child_issues=include_child_issues, end=end, baseline=baseline, only_executed_methods=only_executed_methods, issue_id=issue_id, merge_request_mode=merge_request_mode, uniform_path=uniform_path, merge_base_cache_key=merge_base_cache_key, all_partitions=all_partitions, partitions=partitions, cross_annotation_projects=cross_annotation_projects, execution_only=execution_only, churn=churn)

Get test gap percentage

Calculates the TGA percentage for the given uniform path or the given issue ID. This service is public API since Teamscale 5.9.6. The API requires the user to have View Project permissions on the project.

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
    api_instance = openapi_client.TestGapAnalysisApi(api_client)
    project = 'project_example' # str | The project alias or id.
auto_select_branch = True # bool | Will auto-select the issue branch if set to true. Otherwise, if given, the branchName will be used. As fallback the default branch will be used. (optional) (default to True)
branch_name = 'branch_name_example' # str | If this is given, all issues are shown on this branch. Otherwise, the branch is auto-determined for each issue separately. (optional)
include_child_issues = True # bool | Will include changes introduced by child issues. (optional)
end = 'end_example' # str | The end timestamp (inclusive). (optional)
baseline = 'baseline_example' # str | The baseline timestamp (inclusive). (optional)
only_executed_methods = True # bool | If this parameter is given, the service disregards code changes and only assesses execution of methods. (optional)
issue_id = 'issue_id_example' # str | If this parameter is given and is a valid issue ID, information about all methods changed in the context of this issue ID will be returned. In this case, the baseline parameter is ignored (the baseline is determined automatically for the issue instead). If the special value [no-issue] is given, instead all methods that were changed in commits without an issue link between the baseline and end date are returned. (optional)
merge_request_mode = True # bool | If this is true, we will compute TGA information based on the methods changed in the history of commit1 but not in the history of commit2. This simulates a merge from commit1 to commit2. (optional)
uniform_path = '' # str | Uniform path for which the request should be created (optional) (default to '')
merge_base_cache_key = 'merge_base_cache_key_example' # str | Optional key into the cache index for merge base calculation. If this is known it can be used to speed up calculation of the merge base. (optional)
all_partitions = True # bool | If this is true, all available test coverage partitions are considered. (optional)
partitions = ['partitions_example'] # list[str] | This parameter may be given multiple times. Specifies the test coverage partitions to consider. (optional)
cross_annotation_projects = ['cross_annotation_projects_example'] # list[str] | This parameter may be given multiple times. Specifies further Teamscale projects from which to consider test coverage. (optional)
execution_only = True # bool | If this parameter is given, the service disregards code changes and only assesses execution of methods. (optional)
churn = True # bool | Whether we want to view only the churn (optional)

    try:
        # Get test gap percentage
        api_response = api_instance.get_tga_percentage(project, auto_select_branch=auto_select_branch, branch_name=branch_name, include_child_issues=include_child_issues, end=end, baseline=baseline, only_executed_methods=only_executed_methods, issue_id=issue_id, merge_request_mode=merge_request_mode, uniform_path=uniform_path, merge_base_cache_key=merge_base_cache_key, all_partitions=all_partitions, partitions=partitions, cross_annotation_projects=cross_annotation_projects, execution_only=execution_only, churn=churn)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestGapAnalysisApi->get_tga_percentage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **auto_select_branch** | **bool**| Will auto-select the issue branch if set to true. Otherwise, if given, the branchName will be used. As fallback the default branch will be used. | [optional] [default to True]
 **branch_name** | **str**| If this is given, all issues are shown on this branch. Otherwise, the branch is auto-determined for each issue separately. | [optional] 
 **include_child_issues** | **bool**| Will include changes introduced by child issues. | [optional] 
 **end** | **str**| The end timestamp (inclusive). | [optional] 
 **baseline** | **str**| The baseline timestamp (inclusive). | [optional] 
 **only_executed_methods** | **bool**| If this parameter is given, the service disregards code changes and only assesses execution of methods. | [optional] 
 **issue_id** | **str**| If this parameter is given and is a valid issue ID, information about all methods changed in the context of this issue ID will be returned. In this case, the baseline parameter is ignored (the baseline is determined automatically for the issue instead). If the special value [no-issue] is given, instead all methods that were changed in commits without an issue link between the baseline and end date are returned. | [optional] 
 **merge_request_mode** | **bool**| If this is true, we will compute TGA information based on the methods changed in the history of commit1 but not in the history of commit2. This simulates a merge from commit1 to commit2. | [optional] 
 **uniform_path** | **str**| Uniform path for which the request should be created | [optional] [default to &#39;&#39;]
 **merge_base_cache_key** | **str**| Optional key into the cache index for merge base calculation. If this is known it can be used to speed up calculation of the merge base. | [optional] 
 **all_partitions** | **bool**| If this is true, all available test coverage partitions are considered. | [optional] 
 **partitions** | [**list[str]**](str.md)| This parameter may be given multiple times. Specifies the test coverage partitions to consider. | [optional] 
 **cross_annotation_projects** | [**list[str]**](str.md)| This parameter may be given multiple times. Specifies further Teamscale projects from which to consider test coverage. | [optional] 
 **execution_only** | **bool**| If this parameter is given, the service disregards code changes and only assesses execution of methods. | [optional] 
 **churn** | **bool**| Whether we want to view only the churn | [optional] 

### Return type

**float**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Could not determine common merge base. |  -  |
**404** | The project does not exist. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tga_percentage**
> float post_tga_percentage(project, auto_select_branch=auto_select_branch, branch_name=branch_name, include_child_issues=include_child_issues, end=end, baseline=baseline, only_executed_methods=only_executed_methods, issue_id=issue_id, merge_request_mode=merge_request_mode, uniform_path=uniform_path, merge_base_cache_key=merge_base_cache_key, inline_object2=inline_object2)

Get test gap percentage

Calculates the TGA percentage for the given uniform path or the given issue ID. This service is public API since Teamscale 5.9.6. The API requires the user to have View Project permissions on the project.

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
    api_instance = openapi_client.TestGapAnalysisApi(api_client)
    project = 'project_example' # str | The project alias or id.
auto_select_branch = True # bool | Will auto-select the issue branch if set to true. Otherwise, if given, the branchName will be used. As fallback the default branch will be used. (optional) (default to True)
branch_name = 'branch_name_example' # str | If this is given, all issues are shown on this branch. Otherwise, the branch is auto-determined for each issue separately. (optional)
include_child_issues = True # bool | Will include changes introduced by child issues. (optional)
end = 'end_example' # str | The end timestamp (inclusive). (optional)
baseline = 'baseline_example' # str | The baseline timestamp (inclusive). (optional)
only_executed_methods = True # bool | If this parameter is given, the service disregards code changes and only assesses execution of methods. (optional)
issue_id = 'issue_id_example' # str | If this parameter is given and is a valid issue ID, information about all methods changed in the context of this issue ID will be returned. In this case, the baseline parameter is ignored (the baseline is determined automatically for the issue instead). If the special value [no-issue] is given, instead all methods that were changed in commits without an issue link between the baseline and end date are returned. (optional)
merge_request_mode = True # bool | If this is true, we will compute TGA information based on the methods changed in the history of commit1 but not in the history of commit2. This simulates a merge from commit1 to commit2. (optional)
uniform_path = '' # str | Uniform path for which the request should be created (optional) (default to '')
merge_base_cache_key = 'merge_base_cache_key_example' # str | Optional key into the cache index for merge base calculation. If this is known it can be used to speed up calculation of the merge base. (optional)
inline_object2 = openapi_client.InlineObject2() # InlineObject2 |  (optional)

    try:
        # Get test gap percentage
        api_response = api_instance.post_tga_percentage(project, auto_select_branch=auto_select_branch, branch_name=branch_name, include_child_issues=include_child_issues, end=end, baseline=baseline, only_executed_methods=only_executed_methods, issue_id=issue_id, merge_request_mode=merge_request_mode, uniform_path=uniform_path, merge_base_cache_key=merge_base_cache_key, inline_object2=inline_object2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestGapAnalysisApi->post_tga_percentage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **auto_select_branch** | **bool**| Will auto-select the issue branch if set to true. Otherwise, if given, the branchName will be used. As fallback the default branch will be used. | [optional] [default to True]
 **branch_name** | **str**| If this is given, all issues are shown on this branch. Otherwise, the branch is auto-determined for each issue separately. | [optional] 
 **include_child_issues** | **bool**| Will include changes introduced by child issues. | [optional] 
 **end** | **str**| The end timestamp (inclusive). | [optional] 
 **baseline** | **str**| The baseline timestamp (inclusive). | [optional] 
 **only_executed_methods** | **bool**| If this parameter is given, the service disregards code changes and only assesses execution of methods. | [optional] 
 **issue_id** | **str**| If this parameter is given and is a valid issue ID, information about all methods changed in the context of this issue ID will be returned. In this case, the baseline parameter is ignored (the baseline is determined automatically for the issue instead). If the special value [no-issue] is given, instead all methods that were changed in commits without an issue link between the baseline and end date are returned. | [optional] 
 **merge_request_mode** | **bool**| If this is true, we will compute TGA information based on the methods changed in the history of commit1 but not in the history of commit2. This simulates a merge from commit1 to commit2. | [optional] 
 **uniform_path** | **str**| Uniform path for which the request should be created | [optional] [default to &#39;&#39;]
 **merge_base_cache_key** | **str**| Optional key into the cache index for merge base calculation. If this is known it can be used to speed up calculation of the merge base. | [optional] 
 **inline_object2** | [**InlineObject2**](InlineObject2.md)|  | [optional] 

### Return type

**float**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Could not determine common merge base. |  -  |
**404** | The project does not exist. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

