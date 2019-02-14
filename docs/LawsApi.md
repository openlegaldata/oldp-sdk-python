# oldp_client.LawsApi

All URIs are relative to *https://de.openlegaldata.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**laws_create**](LawsApi.md#laws_create) | **POST** /laws/ | 
[**laws_delete**](LawsApi.md#laws_delete) | **DELETE** /laws/{id}/ | 
[**laws_list**](LawsApi.md#laws_list) | **GET** /laws/ | 
[**laws_partial_update**](LawsApi.md#laws_partial_update) | **PATCH** /laws/{id}/ | 
[**laws_read**](LawsApi.md#laws_read) | **GET** /laws/{id}/ | 
[**laws_search_list**](LawsApi.md#laws_search_list) | **GET** /laws/search/ | 
[**laws_search_read**](LawsApi.md#laws_search_read) | **GET** /laws/search/{id}/ | 
[**laws_update**](LawsApi.md#laws_update) | **PUT** /laws/{id}/ | 


# **laws_create**
> Law laws_create(data)





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
api_instance = oldp_client.LawsApi(oldp_client.ApiClient(configuration))
data = oldp_client.Law() # Law | 

try:
    api_response = api_instance.laws_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LawsApi->laws_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Law**](Law.md)|  | 

### Return type

[**Law**](Law.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **laws_delete**
> laws_delete(id)





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
api_instance = oldp_client.LawsApi(oldp_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this law.

try:
    api_instance.laws_delete(id)
except ApiException as e:
    print("Exception when calling LawsApi->laws_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this law. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **laws_list**
> InlineResponse2008 laws_list(book_id=book_id, book__latest=book__latest, book__revision_date=book__revision_date, limit=limit, offset=offset)





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
api_instance = oldp_client.LawsApi(oldp_client.ApiClient(configuration))
book_id = 'book_id_example' # str |  (optional)
book__latest = 'book__latest_example' # str |  (optional)
book__revision_date = 'book__revision_date_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.laws_list(book_id=book_id, book__latest=book__latest, book__revision_date=book__revision_date, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LawsApi->laws_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **str**|  | [optional] 
 **book__latest** | **str**|  | [optional] 
 **book__revision_date** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **laws_partial_update**
> Law laws_partial_update(id, data)





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
api_instance = oldp_client.LawsApi(oldp_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this law.
data = oldp_client.Law() # Law | 

try:
    api_response = api_instance.laws_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LawsApi->laws_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this law. | 
 **data** | [**Law**](Law.md)|  | 

### Return type

[**Law**](Law.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **laws_read**
> Law laws_read(id)





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
api_instance = oldp_client.LawsApi(oldp_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this law.

try:
    api_response = api_instance.laws_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LawsApi->laws_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this law. | 

### Return type

[**Law**](Law.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **laws_search_list**
> InlineResponse2009 laws_search_list(page=page, page_size=page_size)





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
api_instance = oldp_client.LawsApi(oldp_client.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.laws_search_list(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LawsApi->laws_search_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **laws_search_read**
> LawSearch laws_search_read(id)





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
api_instance = oldp_client.LawsApi(oldp_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.laws_search_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LawsApi->laws_search_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**LawSearch**](LawSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **laws_update**
> Law laws_update(id, data)





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
api_instance = oldp_client.LawsApi(oldp_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this law.
data = oldp_client.Law() # Law | 

try:
    api_response = api_instance.laws_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LawsApi->laws_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this law. | 
 **data** | [**Law**](Law.md)|  | 

### Return type

[**Law**](Law.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

