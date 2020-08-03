# openapi_client.BackupApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_backup**](BackupApi.md#create_backup) | **POST** /api/backups/export | Export backup.
[**download_backup**](BackupApi.md#download_backup) | **GET** /api/backups/export/{backupId}/download | Download backup
[**get_backup_status**](BackupApi.md#get_backup_status) | **GET** /api/backups/export/{backupId}/status | Get the backup status
[**get_backup_status1**](BackupApi.md#get_backup_status1) | **GET** /api/backups/import/{backupId}/status | Get the backup status
[**get_summary**](BackupApi.md#get_summary) | **GET** /api/backups/export/summary | Get the complete backup summary
[**get_summary1**](BackupApi.md#get_summary1) | **GET** /api/backups/import/summary | Get the complete backup summary
[**import_backup**](BackupApi.md#import_backup) | **POST** /api/backups/import | Import backup.


# **create_backup**
> str create_backup(backup_global=backup_global, include_project=include_project, use_local_crypto_key=use_local_crypto_key, backup_path=backup_path)

Export backup.

Triggers the creation of a backup and returns its ID. This service is public API since Teamscale 6.1. The user needs to have the permission to export global data provided the backup contains any and the permission to backup project data for all projects contained in the backup.

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
    api_instance = openapi_client.BackupApi(api_client)
    backup_global = True # bool | Include global data in the backup. (optional)
include_project = 'include_project_example' # list[str] | Include project data in the backup. May be present multiple times. (optional)
use_local_crypto_key = True # bool | Use the local key (if configured) instead of Teamscale default key for encryption. (optional)
backup_path = 'backup_path_example' # str | The backup path. If this is not set, a new internal path will be generated. (optional)

    try:
        # Export backup.
        api_response = api_instance.create_backup(backup_global=backup_global, include_project=include_project, use_local_crypto_key=use_local_crypto_key, backup_path=backup_path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackupApi->create_backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup_global** | **bool**| Include global data in the backup. | [optional] 
 **include_project** | [**list[str]**](str.md)| Include project data in the backup. May be present multiple times. | [optional] 
 **use_local_crypto_key** | **bool**| Use the local key (if configured) instead of Teamscale default key for encryption. | [optional] 
 **backup_path** | **str**| The backup path. If this is not set, a new internal path will be generated. | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_backup**
> download_backup(backup_id)

Download backup

Allows downloading a Teamscale backup from the temporary file store. This service is public API since Teamscale 6.1. The user needs to have the permission to backup global data provided it is contained in the backup and the permission to backup project data for all projects contained in the backup.

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
    api_instance = openapi_client.BackupApi(api_client)
    backup_id = 'backup_id_example' # str | The backup ID.

    try:
        # Download backup
        api_instance.download_backup(backup_id)
    except ApiException as e:
        print("Exception when calling BackupApi->download_backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup_id** | **str**| The backup ID. | 

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
**400** | The backup is not ready for download as it is still running or failed. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | The backup was not found. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backup_status**
> BackupStatusBase get_backup_status(backup_id)

Get the backup status

Get the current backup import/export status This service is public API since Teamscale 6.1. The user needs to be able to configure projects. In addition the user needs to have the permission to backup global data provided the backup contains any global data and the permission to backup project data for all projects contained in the backup.

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
    api_instance = openapi_client.BackupApi(api_client)
    backup_id = 'backup_id_example' # str | The backup ID.

    try:
        # Get the backup status
        api_response = api_instance.get_backup_status(backup_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackupApi->get_backup_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup_id** | **str**| The backup ID. | 

### Return type

[**BackupStatusBase**](BackupStatusBase.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | No backup for the provided ID found. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backup_status1**
> BackupStatusBase get_backup_status1(backup_id)

Get the backup status

Get the current backup import/export status This service is public API since Teamscale 6.1. The user needs to be able to configure projects. In addition the user needs to have the permission to backup global data provided the backup contains any global data and the permission to backup project data for all projects contained in the backup.

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
    api_instance = openapi_client.BackupApi(api_client)
    backup_id = 'backup_id_example' # str | The backup ID.

    try:
        # Get the backup status
        api_response = api_instance.get_backup_status1(backup_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackupApi->get_backup_status1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup_id** | **str**| The backup ID. | 

### Return type

[**BackupStatusBase**](BackupStatusBase.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**404** | No backup for the provided ID found. |  -  |
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary**
> list[BackupJobSummary] get_summary()

Get the complete backup summary

Get the summary of the 10 most recent backups. This service is public API since Teamscale 6.1. The API requires the user to have Backup Global Data permissions.

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
    api_instance = openapi_client.BackupApi(api_client)
    
    try:
        # Get the complete backup summary
        api_response = api_instance.get_summary()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackupApi->get_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BackupJobSummary]**](BackupJobSummary.md)

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
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary1**
> list[BackupJobSummary] get_summary1()

Get the complete backup summary

Get the summary of the 10 most recent backups. This service is public API since Teamscale 6.1. The API requires the user to have Backup Global Data permissions.

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
    api_instance = openapi_client.BackupApi(api_client)
    
    try:
        # Get the complete backup summary
        api_response = api_instance.get_summary1()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackupApi->get_summary1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BackupJobSummary]**](BackupJobSummary.md)

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
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_backup**
> str import_backup(backup=backup, backup_path=backup_path, shadow_mode=shadow_mode, skip_project_creation=skip_project_creation, skip_project_validation=skip_project_validation)

Import backup.

Triggers the import of a backup and returns the job ID. This service is public API since Teamscale 6.1. The API requires the user to have Backup Global Data permissions.

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
    api_instance = openapi_client.BackupApi(api_client)
    backup = None # list[object] | The backups to import. (optional)
backup_path = 'backup_path_example' # str | Path to the backup. (optional)
shadow_mode = True # bool | Whether to enable shadow mode right after import. (optional)
skip_project_creation = True # bool | Whether to skip the project creation and only import backup data into existing projects. (optional)
skip_project_validation = True # bool | Whether to skip the project validation on import (optional)

    try:
        # Import backup.
        api_response = api_instance.import_backup(backup=backup, backup_path=backup_path, shadow_mode=shadow_mode, skip_project_creation=skip_project_creation, skip_project_validation=skip_project_validation)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackupApi->import_backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup** | [**list[object]**](object.md)| The backups to import. | [optional] 
 **backup_path** | **str**| Path to the backup. | [optional] 
 **shadow_mode** | **bool**| Whether to enable shadow mode right after import. | [optional] 
 **skip_project_creation** | **bool**| Whether to skip the project creation and only import backup data into existing projects. | [optional] 
 **skip_project_validation** | **bool**| Whether to skip the project validation on import | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | No authentication header was provided or the credentials were invalid. |  -  |
**403** | The user is authenticated, but does not have the necessary permissions to access the endpoint. |  -  |
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

