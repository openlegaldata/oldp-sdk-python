# oldp_client.TokenAuthApi

All URIs are relative to *https://de.openlegaldata.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**token_auth_create**](TokenAuthApi.md#token_auth_create) | **POST** /token-auth/ | 


# **token_auth_create**
> token_auth_create()





### Example
```python
from __future__ import print_function
import time
import oldp_client
from oldp_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = oldp_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oldp_client.TokenAuthApi(oldp_client.ApiClient(configuration))

try:
    api_instance.token_auth_create()
except ApiException as e:
    print("Exception when calling TokenAuthApi->token_auth_create: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

