# oldp_client.CasesApi

All URIs are relative to *https://de.openlegaldata.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cases_create**](CasesApi.md#cases_create) | **POST** /cases/ | 
[**cases_delete**](CasesApi.md#cases_delete) | **DELETE** /cases/{id}/ | 
[**cases_list**](CasesApi.md#cases_list) | **GET** /cases/ | 
[**cases_partial_update**](CasesApi.md#cases_partial_update) | **PATCH** /cases/{id}/ | 
[**cases_read**](CasesApi.md#cases_read) | **GET** /cases/{id}/ | 
[**cases_search_list**](CasesApi.md#cases_search_list) | **GET** /cases/search/ | 
[**cases_search_read**](CasesApi.md#cases_search_read) | **GET** /cases/search/{id}/ | 
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
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

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
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

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
> InlineResponse2002 cases_list(ordering=ordering, _date=_date, slug=slug, file_number=file_number, ecli=ecli, court=court, court__slug=court__slug, court__jurisdiction=court__jurisdiction, court__level_of_appeal=court__level_of_appeal, court__state=court__state, page=page, page_size=page_size)





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
api_instance = oldp_client.CasesApi(oldp_client.ApiClient(configuration))
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
_date = '_date_example' # str |  (optional)
slug = 'slug_example' # str |  (optional)
file_number = 'file_number_example' # str |  (optional)
ecli = 'ecli_example' # str |  (optional)
court = 8.14 # float |  (optional)
court__slug = 'court__slug_example' # str |  (optional)
court__jurisdiction = 'court__jurisdiction_example' # str |  (optional)
court__level_of_appeal = 'court__level_of_appeal_example' # str |  (optional)
court__state = 'court__state_example' # str |  (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.cases_list(ordering=ordering, _date=_date, slug=slug, file_number=file_number, ecli=ecli, court=court, court__slug=court__slug, court__jurisdiction=court__jurisdiction, court__level_of_appeal=court__level_of_appeal, court__state=court__state, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CasesApi->cases_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **_date** | **str**|  | [optional] 
 **slug** | **str**|  | [optional] 
 **file_number** | **str**|  | [optional] 
 **ecli** | **str**|  | [optional] 
 **court** | **float**|  | [optional] 
 **court__slug** | **str**|  | [optional] 
 **court__jurisdiction** | **str**|  | [optional] 
 **court__level_of_appeal** | **str**|  | [optional] 
 **court__state** | **str**|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

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
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

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
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

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

# **cases_search_list**
> InlineResponse2003 cases_search_list(page=page, page_size=page_size)





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
api_instance = oldp_client.CasesApi(oldp_client.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.cases_search_list(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CasesApi->cases_search_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cases_search_read**
> CaseSearch cases_search_read(id)





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
api_instance = oldp_client.CasesApi(oldp_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.cases_search_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CasesApi->cases_search_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CaseSearch**](CaseSearch.md)

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
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

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

