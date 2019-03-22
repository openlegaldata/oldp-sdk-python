# oldp_client.LawBooksApi

All URIs are relative to *https://de.openlegaldata.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**law_books_create**](LawBooksApi.md#law_books_create) | **POST** /law_books/ | 
[**law_books_delete**](LawBooksApi.md#law_books_delete) | **DELETE** /law_books/{id}/ | 
[**law_books_list**](LawBooksApi.md#law_books_list) | **GET** /law_books/ | 
[**law_books_partial_update**](LawBooksApi.md#law_books_partial_update) | **PATCH** /law_books/{id}/ | 
[**law_books_read**](LawBooksApi.md#law_books_read) | **GET** /law_books/{id}/ | 
[**law_books_update**](LawBooksApi.md#law_books_update) | **PUT** /law_books/{id}/ | 


# **law_books_create**
> LawBook law_books_create(data)





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
api_instance = oldp_client.LawBooksApi(oldp_client.ApiClient(configuration))
data = oldp_client.LawBook() # LawBook | 

try:
    api_response = api_instance.law_books_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LawBooksApi->law_books_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**LawBook**](LawBook.md)|  | 

### Return type

[**LawBook**](LawBook.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **law_books_delete**
> law_books_delete(id)





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
api_instance = oldp_client.LawBooksApi(oldp_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this law book.

try:
    api_instance.law_books_delete(id)
except ApiException as e:
    print("Exception when calling LawBooksApi->law_books_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this law book. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **law_books_list**
> InlineResponse2008 law_books_list(slug=slug, code=code, latest=latest, revision_date=revision_date, limit=limit, offset=offset)





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
api_instance = oldp_client.LawBooksApi(oldp_client.ApiClient(configuration))
slug = 'slug_example' # str |  (optional)
code = 'code_example' # str |  (optional)
latest = 'latest_example' # str |  (optional)
revision_date = 'revision_date_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.law_books_list(slug=slug, code=code, latest=latest, revision_date=revision_date, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LawBooksApi->law_books_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | [optional] 
 **code** | **str**|  | [optional] 
 **latest** | **str**|  | [optional] 
 **revision_date** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **law_books_partial_update**
> LawBook law_books_partial_update(id, data)





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
api_instance = oldp_client.LawBooksApi(oldp_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this law book.
data = oldp_client.LawBook() # LawBook | 

try:
    api_response = api_instance.law_books_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LawBooksApi->law_books_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this law book. | 
 **data** | [**LawBook**](LawBook.md)|  | 

### Return type

[**LawBook**](LawBook.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **law_books_read**
> LawBook law_books_read(id)





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
api_instance = oldp_client.LawBooksApi(oldp_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this law book.

try:
    api_response = api_instance.law_books_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LawBooksApi->law_books_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this law book. | 

### Return type

[**LawBook**](LawBook.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **law_books_update**
> LawBook law_books_update(id, data)





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
api_instance = oldp_client.LawBooksApi(oldp_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this law book.
data = oldp_client.LawBook() # LawBook | 

try:
    api_response = api_instance.law_books_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LawBooksApi->law_books_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this law book. | 
 **data** | [**LawBook**](LawBook.md)|  | 

### Return type

[**LawBook**](LawBook.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

