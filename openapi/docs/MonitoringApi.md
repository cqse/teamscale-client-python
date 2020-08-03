# openapi_client.MonitoringApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health_status**](MonitoringApi.md#get_health_status) | **GET** /api/health-check | Get system health status


# **get_health_status**
> str get_health_status(check=check, critical_only=critical_only)

Get system health status

Retrieves a log of system health status information. This service is public API since Teamscale 5.5. No login required to perform monitoring.

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
    api_instance = openapi_client.MonitoringApi(api_client)
    check = ['check_example'] # list[str] | List of system health checks to perform (optional)
critical_only = True # bool | Determines if only critical health check entries should be returned (optional)

    try:
        # Get system health status
        api_response = api_instance.get_health_status(check=check, critical_only=critical_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringApi->get_health_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check** | [**list[str]**](str.md)| List of system health checks to perform | [optional] 
 **critical_only** | **bool**| Determines if only critical health check entries should be returned | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Unknown system health check(s) requested. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

