# oldp_client.CourtsApi

All URIs are relative to *https://de.openlegaldata.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**courts_list**](CourtsApi.md#courts_list) | **GET** /courts/ | 
[**courts_read**](CourtsApi.md#courts_read) | **GET** /courts/{id}/ | 


# **courts_list**
> InlineResponse2006 courts_list(court_type=court_type, slug=slug, code=code, state_id=state_id, city_id=city_id, limit=limit, offset=offset)





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
api_instance = oldp_client.CourtsApi(oldp_client.ApiClient(configuration))
court_type = 'court_type_example' # str |  (optional)
slug = 'slug_example' # str |  (optional)
code = 'code_example' # str |  (optional)
state_id = 'state_id_example' # str |  (optional)
city_id = 'city_id_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.courts_list(court_type=court_type, slug=slug, code=code, state_id=state_id, city_id=city_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CourtsApi->courts_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **court_type** | **str**|  | [optional] 
 **slug** | **str**|  | [optional] 
 **code** | **str**|  | [optional] 
 **state_id** | **str**|  | [optional] 
 **city_id** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courts_read**
> Court courts_read(id)





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
api_instance = oldp_client.CourtsApi(oldp_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this court.

try:
    api_response = api_instance.courts_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CourtsApi->courts_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this court. | 

### Return type

[**Court**](Court.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

