# oldp_client.AnnotationLabelsApi

All URIs are relative to *https://de.openlegaldata.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**annotation_labels_create**](AnnotationLabelsApi.md#annotation_labels_create) | **POST** /annotation_labels/ | 
[**annotation_labels_delete**](AnnotationLabelsApi.md#annotation_labels_delete) | **DELETE** /annotation_labels/{id}/ | 
[**annotation_labels_list**](AnnotationLabelsApi.md#annotation_labels_list) | **GET** /annotation_labels/ | 
[**annotation_labels_partial_update**](AnnotationLabelsApi.md#annotation_labels_partial_update) | **PATCH** /annotation_labels/{id}/ | 
[**annotation_labels_read**](AnnotationLabelsApi.md#annotation_labels_read) | **GET** /annotation_labels/{id}/ | 
[**annotation_labels_update**](AnnotationLabelsApi.md#annotation_labels_update) | **PUT** /annotation_labels/{id}/ | 


# **annotation_labels_create**
> AnnotationLabel annotation_labels_create(data)





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
api_instance = oldp_client.AnnotationLabelsApi(oldp_client.ApiClient(configuration))
data = oldp_client.AnnotationLabel() # AnnotationLabel | 

try:
    api_response = api_instance.annotation_labels_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationLabelsApi->annotation_labels_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**AnnotationLabel**](AnnotationLabel.md)|  | 

### Return type

[**AnnotationLabel**](AnnotationLabel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **annotation_labels_delete**
> annotation_labels_delete(id)





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
api_instance = oldp_client.AnnotationLabelsApi(oldp_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this Label.

try:
    api_instance.annotation_labels_delete(id)
except ApiException as e:
    print("Exception when calling AnnotationLabelsApi->annotation_labels_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Label. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **annotation_labels_list**
> InlineResponse200 annotation_labels_list(ordering=ordering, owner=owner, slug=slug, private=private, trusted=trusted, limit=limit, offset=offset)





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
api_instance = oldp_client.AnnotationLabelsApi(oldp_client.ApiClient(configuration))
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
owner = 8.14 # float |  (optional)
slug = 'slug_example' # str |  (optional)
private = 'private_example' # str |  (optional)
trusted = 'trusted_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.annotation_labels_list(ordering=ordering, owner=owner, slug=slug, private=private, trusted=trusted, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationLabelsApi->annotation_labels_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **owner** | **float**|  | [optional] 
 **slug** | **str**|  | [optional] 
 **private** | **str**|  | [optional] 
 **trusted** | **str**|  | [optional] 
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

# **annotation_labels_partial_update**
> AnnotationLabel annotation_labels_partial_update(id, data)





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
api_instance = oldp_client.AnnotationLabelsApi(oldp_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this Label.
data = oldp_client.AnnotationLabel() # AnnotationLabel | 

try:
    api_response = api_instance.annotation_labels_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationLabelsApi->annotation_labels_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Label. | 
 **data** | [**AnnotationLabel**](AnnotationLabel.md)|  | 

### Return type

[**AnnotationLabel**](AnnotationLabel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **annotation_labels_read**
> AnnotationLabel annotation_labels_read(id)





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
api_instance = oldp_client.AnnotationLabelsApi(oldp_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this Label.

try:
    api_response = api_instance.annotation_labels_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationLabelsApi->annotation_labels_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Label. | 

### Return type

[**AnnotationLabel**](AnnotationLabel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **annotation_labels_update**
> AnnotationLabel annotation_labels_update(id, data)





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
api_instance = oldp_client.AnnotationLabelsApi(oldp_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this Label.
data = oldp_client.AnnotationLabel() # AnnotationLabel | 

try:
    api_response = api_instance.annotation_labels_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationLabelsApi->annotation_labels_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Label. | 
 **data** | [**AnnotationLabel**](AnnotationLabel.md)|  | 

### Return type

[**AnnotationLabel**](AnnotationLabel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

