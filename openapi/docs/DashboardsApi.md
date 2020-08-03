# openapi_client.DashboardsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_file**](DashboardsApi.md#import_file) | **POST** /api/dashboards | Post a dashboard or a dashboard template


# **import_file**
> list[str] import_file(teamscale_version_container)

Post a dashboard or a dashboard template

Performs an import of a dashboard or a dashboard template. Redirects to the templates overview page or the last edited dashboard. Adds the uploaded descriptor to the list of dashboards/templates. The descriptor must be packaged within an XML Teamscale Version Container. This service is public API since Teamscale 5.8. The API requires no permissions

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
    api_instance = openapi_client.DashboardsApi(api_client)
    teamscale_version_container = openapi_client.TeamscaleVersionContainer() # TeamscaleVersionContainer | 

    try:
        # Post a dashboard or a dashboard template
        api_response = api_instance.import_file(teamscale_version_container)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->import_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamscale_version_container** | [**TeamscaleVersionContainer**](TeamscaleVersionContainer.md)|  | 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | No descriptor data given. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

