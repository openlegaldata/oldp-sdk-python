# oldp_client.CaseAnnotationsApi

All URIs are relative to *http://de.openlegaldata.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**case_annotations_create**](CaseAnnotationsApi.md#case_annotations_create) | **POST** /case_annotations/ | 
[**case_annotations_delete**](CaseAnnotationsApi.md#case_annotations_delete) | **DELETE** /case_annotations/{id}/ | 
[**case_annotations_list**](CaseAnnotationsApi.md#case_annotations_list) | **GET** /case_annotations/ | 
[**case_annotations_partial_update**](CaseAnnotationsApi.md#case_annotations_partial_update) | **PATCH** /case_annotations/{id}/ | 
[**case_annotations_read**](CaseAnnotationsApi.md#case_annotations_read) | **GET** /case_annotations/{id}/ | 
[**case_annotations_update**](CaseAnnotationsApi.md#case_annotations_update) | **PUT** /case_annotations/{id}/ | 


# **case_annotations_create**
> CaseAnnotation case_annotations_create(data)





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
api_instance = oldp_client.CaseAnnotationsApi(oldp_client.ApiClient(configuration))
data = oldp_client.CaseAnnotation() # CaseAnnotation | 

try:
    api_response = api_instance.case_annotations_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseAnnotationsApi->case_annotations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**CaseAnnotation**](CaseAnnotation.md)|  | 

### Return type

[**CaseAnnotation**](CaseAnnotation.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **case_annotations_delete**
> case_annotations_delete(id)





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
api_instance = oldp_client.CaseAnnotationsApi(oldp_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this case annotation.

try:
    api_instance.case_annotations_delete(id)
except ApiException as e:
    print("Exception when calling CaseAnnotationsApi->case_annotations_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this case annotation. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **case_annotations_list**
> InlineResponse2001 case_annotations_list(belongs_to=belongs_to, label=label, limit=limit, offset=offset)





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
api_instance = oldp_client.CaseAnnotationsApi(oldp_client.ApiClient(configuration))
belongs_to = 8.14 # float |  (optional)
label = 8.14 # float |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.case_annotations_list(belongs_to=belongs_to, label=label, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseAnnotationsApi->case_annotations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **belongs_to** | **float**|  | [optional] 
 **label** | **float**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **case_annotations_partial_update**
> CaseAnnotation case_annotations_partial_update(id, data)





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
api_instance = oldp_client.CaseAnnotationsApi(oldp_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this case annotation.
data = oldp_client.CaseAnnotation() # CaseAnnotation | 

try:
    api_response = api_instance.case_annotations_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseAnnotationsApi->case_annotations_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this case annotation. | 
 **data** | [**CaseAnnotation**](CaseAnnotation.md)|  | 

### Return type

[**CaseAnnotation**](CaseAnnotation.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **case_annotations_read**
> CaseAnnotation case_annotations_read(id)





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
api_instance = oldp_client.CaseAnnotationsApi(oldp_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this case annotation.

try:
    api_response = api_instance.case_annotations_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseAnnotationsApi->case_annotations_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this case annotation. | 

### Return type

[**CaseAnnotation**](CaseAnnotation.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **case_annotations_update**
> CaseAnnotation case_annotations_update(id, data)





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
api_instance = oldp_client.CaseAnnotationsApi(oldp_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this case annotation.
data = oldp_client.CaseAnnotation() # CaseAnnotation | 

try:
    api_response = api_instance.case_annotations_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseAnnotationsApi->case_annotations_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this case annotation. | 
 **data** | [**CaseAnnotation**](CaseAnnotation.md)|  | 

### Return type

[**CaseAnnotation**](CaseAnnotation.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

