# openapi_client.TestImpactAnalysisApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_impacted_tests**](TestImpactAnalysisApi.md#get_impacted_tests) | **PUT** /api/projects/{project}/impacted-tests | Get impacted tests
[**get_impacted_tests1**](TestImpactAnalysisApi.md#get_impacted_tests1) | **GET** /api/projects/{project}/impacted-tests | Get impacted tests


# **get_impacted_tests**
> list[PrioritizableTestCluster] get_impacted_tests(project, end, baseline=baseline, partitions=partitions, prioritization_strategy=prioritization_strategy, ensure_processed=ensure_processed, include_non_impacted=include_non_impacted, include_failed_and_skipped=include_failed_and_skipped, clustered_test_details=clustered_test_details)

Get impacted tests

Returns an ordered list of test clusters that are impacted by the given changes. The returned list of test clusters is a subset of the tests given in the request body. Clusters of selected and prioritized tests are formed based on the clustering information given in the request body. The tests from the request body are furthermore used to determine if any tests have changed or new tests were added. These are always included in the returned list of impacted tests. This service is public API since Teamscale 5.7. The API requires the user to have View Project permissions on the project.

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
    api_instance = openapi_client.TestImpactAnalysisApi(api_client)
    project = 'project_example' # str | The project alias or id.
end = 'end_example' # str | The end timestamp (inclusive).
baseline = '1' # str | The baseline timestamp (inclusive). (optional) (default to '1')
partitions = ['partitions_example'] # list[str] | This parameter may be given multiple times. Specifies the test coverage partitions to consider. (optional)
prioritization_strategy = 'ADDITIONAL_COVERAGE_PER_TIME' # str | The name of the test prioritization strategy (optional) (default to 'ADDITIONAL_COVERAGE_PER_TIME')
ensure_processed = True # bool | If set to true the request will fail with '412 PRECONDITION FAILED' if the exact given end commit has not been processed yet and therefore data may not be up-to-date. (optional) (default to True)
include_non_impacted = True # bool | Append and prioritize non-impacted tests after impacted tests (optional)
include_failed_and_skipped = False # bool | Append and prioritize previously failed and skipped tests before impacted tests. (optional) (default to False)
clustered_test_details = [openapi_client.ClusteredTestDetails()] # list[ClusteredTestDetails] |  (optional)

    try:
        # Get impacted tests
        api_response = api_instance.get_impacted_tests(project, end, baseline=baseline, partitions=partitions, prioritization_strategy=prioritization_strategy, ensure_processed=ensure_processed, include_non_impacted=include_non_impacted, include_failed_and_skipped=include_failed_and_skipped, clustered_test_details=clustered_test_details)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestImpactAnalysisApi->get_impacted_tests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **end** | **str**| The end timestamp (inclusive). | 
 **baseline** | **str**| The baseline timestamp (inclusive). | [optional] [default to &#39;1&#39;]
 **partitions** | [**list[str]**](str.md)| This parameter may be given multiple times. Specifies the test coverage partitions to consider. | [optional] 
 **prioritization_strategy** | **str**| The name of the test prioritization strategy | [optional] [default to &#39;ADDITIONAL_COVERAGE_PER_TIME&#39;]
 **ensure_processed** | **bool**| If set to true the request will fail with &#39;412 PRECONDITION FAILED&#39; if the exact given end commit has not been processed yet and therefore data may not be up-to-date. | [optional] [default to True]
 **include_non_impacted** | **bool**| Append and prioritize non-impacted tests after impacted tests | [optional] 
 **include_failed_and_skipped** | **bool**| Append and prioritize previously failed and skipped tests before impacted tests. | [optional] [default to False]
 **clustered_test_details** | [**list[ClusteredTestDetails]**](ClusteredTestDetails.md)|  | [optional] 

### Return type

[**list[PrioritizableTestCluster]**](PrioritizableTestCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**412** | The given commit has not been processed yet. |  -  |
**400** | One of the given options is invalid. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | The project does not exist. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_impacted_tests1**
> list[PrioritizableTest] get_impacted_tests1(project, end, baseline=baseline, partitions=partitions, prioritization_strategy=prioritization_strategy, ensure_processed=ensure_processed, include_non_impacted=include_non_impacted, include_failed_and_skipped=include_failed_and_skipped)

Get impacted tests

Returns an ordered list of test clusters that are impacted by the given changes. The returned flat list of tests is a subset of all tests known to Teamscale. When the tests themselves have changed, new tests were added or tests have been deleted, this service cannot take that into account. Please use the PUT endpoint instead to provide a list of available tests. In particular, this endpoint may return tests that no longer exist. Callers must handle this case. This service is public API since Teamscale 5.7. The API requires the user to have View Project permissions on the project.

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
    api_instance = openapi_client.TestImpactAnalysisApi(api_client)
    project = 'project_example' # str | The project alias or id.
end = 'end_example' # str | The end timestamp (inclusive).
baseline = '1' # str | The baseline timestamp (inclusive). (optional) (default to '1')
partitions = ['partitions_example'] # list[str] | This parameter may be given multiple times. Specifies the test coverage partitions to consider. (optional)
prioritization_strategy = 'ADDITIONAL_COVERAGE_PER_TIME' # str | The name of the test prioritization strategy (optional) (default to 'ADDITIONAL_COVERAGE_PER_TIME')
ensure_processed = True # bool | If set to true the request will fail with '412 PRECONDITION FAILED' if the exact given end commit has not been processed yet and therefore data may not be up-to-date. (optional) (default to True)
include_non_impacted = True # bool | Append and prioritize non-impacted tests after impacted tests (optional)
include_failed_and_skipped = False # bool | Append and prioritize previously failed and skipped tests before impacted tests. (optional) (default to False)

    try:
        # Get impacted tests
        api_response = api_instance.get_impacted_tests1(project, end, baseline=baseline, partitions=partitions, prioritization_strategy=prioritization_strategy, ensure_processed=ensure_processed, include_non_impacted=include_non_impacted, include_failed_and_skipped=include_failed_and_skipped)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestImpactAnalysisApi->get_impacted_tests1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project alias or id. | 
 **end** | **str**| The end timestamp (inclusive). | 
 **baseline** | **str**| The baseline timestamp (inclusive). | [optional] [default to &#39;1&#39;]
 **partitions** | [**list[str]**](str.md)| This parameter may be given multiple times. Specifies the test coverage partitions to consider. | [optional] 
 **prioritization_strategy** | **str**| The name of the test prioritization strategy | [optional] [default to &#39;ADDITIONAL_COVERAGE_PER_TIME&#39;]
 **ensure_processed** | **bool**| If set to true the request will fail with &#39;412 PRECONDITION FAILED&#39; if the exact given end commit has not been processed yet and therefore data may not be up-to-date. | [optional] [default to True]
 **include_non_impacted** | **bool**| Append and prioritize non-impacted tests after impacted tests | [optional] 
 **include_failed_and_skipped** | **bool**| Append and prioritize previously failed and skipped tests before impacted tests. | [optional] [default to False]

### Return type

[**list[PrioritizableTest]**](PrioritizableTest.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**412** | The given commit has not been processed yet. |  -  |
**400** | One of the given options is invalid. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | The project does not exist. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

