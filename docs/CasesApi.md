# oldp_client.CasesApi

All URIs are relative to *http://de.openlegaldata.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cases_create**](CasesApi.md#cases_create) | **POST** /cases/ | 
[**cases_delete**](CasesApi.md#cases_delete) | **DELETE** /cases/{id}/ | 
[**cases_list**](CasesApi.md#cases_list) | **GET** /cases/ | 
[**cases_partial_update**](CasesApi.md#cases_partial_update) | **PATCH** /cases/{id}/ | 
[**cases_read**](CasesApi.md#cases_read) | **GET** /cases/{id}/ | 
[**cases_update**](CasesApi.md#cases_update) | **PUT** /cases/{id}/ | 


# **cases_create**
> Case cases_create(data)





### Example
```python
from __future__ import print_function
import time
import oldp_client
from oldp_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = oldp_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = oldp_client.CasesApi(oldp_client.ApiClient(configuration))
data = oldp_client.Case() # Case | 

try:
    api_response = api_instance.cases_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CasesApi->cases_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Case**](Case.md)|  | 

### Return type

[**Case**](Case.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cases_delete**
> cases_delete(id)





### Example
```python
from __future__ import print_function
import time
import oldp_client
from oldp_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = oldp_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = oldp_client.CasesApi(oldp_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this case.

try:
    api_instance.cases_delete(id)
except ApiException as e:
    print("Exception when calling CasesApi->cases_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this case. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cases_list**
> InlineResponse200 cases_list(slug=slug, file_number=file_number, court_id=court_id, limit=limit, offset=offset)





### Example
```python
from __future__ import print_function
import time
import oldp_client
from oldp_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = oldp_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = oldp_client.CasesApi(oldp_client.ApiClient(configuration))
slug = 'slug_example' # str |  (optional)
file_number = 'file_number_example' # str |  (optional)
court_id = 'court_id_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.cases_list(slug=slug, file_number=file_number, court_id=court_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CasesApi->cases_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | [optional] 
 **file_number** | **str**|  | [optional] 
 **court_id** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cases_partial_update**
> Case cases_partial_update(id, data)





### Example
```python
from __future__ import print_function
import time
import oldp_client
from oldp_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = oldp_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = oldp_client.CasesApi(oldp_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this case.
data = oldp_client.Case() # Case | 

try:
    api_response = api_instance.cases_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CasesApi->cases_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this case. | 
 **data** | [**Case**](Case.md)|  | 

### Return type

[**Case**](Case.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cases_read**
> Case cases_read(id)





### Example
```python
from __future__ import print_function
import time
import oldp_client
from oldp_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = oldp_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = oldp_client.CasesApi(oldp_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this case.

try:
    api_response = api_instance.cases_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CasesApi->cases_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this case. | 

### Return type

[**Case**](Case.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cases_update**
> Case cases_update(id, data)





### Example
```python
from __future__ import print_function
import time
import oldp_client
from oldp_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = oldp_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = oldp_client.CasesApi(oldp_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this case.
data = oldp_client.Case() # Case | 

try:
    api_response = api_instance.cases_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CasesApi->cases_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this case. | 
 **data** | [**Case**](Case.md)|  | 

### Return type

[**Case**](Case.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

