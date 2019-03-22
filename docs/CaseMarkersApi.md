# oldp_client.CaseMarkersApi

All URIs are relative to *https://de.openlegaldata.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**case_markers_create**](CaseMarkersApi.md#case_markers_create) | **POST** /case_markers/ | 
[**case_markers_delete**](CaseMarkersApi.md#case_markers_delete) | **DELETE** /case_markers/{id}/ | 
[**case_markers_list**](CaseMarkersApi.md#case_markers_list) | **GET** /case_markers/ | 
[**case_markers_partial_update**](CaseMarkersApi.md#case_markers_partial_update) | **PATCH** /case_markers/{id}/ | 
[**case_markers_read**](CaseMarkersApi.md#case_markers_read) | **GET** /case_markers/{id}/ | 
[**case_markers_update**](CaseMarkersApi.md#case_markers_update) | **PUT** /case_markers/{id}/ | 


# **case_markers_create**
> CaseMarker case_markers_create(data)





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
api_instance = oldp_client.CaseMarkersApi(oldp_client.ApiClient(configuration))
data = oldp_client.CaseMarker() # CaseMarker | 

try:
    api_response = api_instance.case_markers_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseMarkersApi->case_markers_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**CaseMarker**](CaseMarker.md)|  | 

### Return type

[**CaseMarker**](CaseMarker.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **case_markers_delete**
> case_markers_delete(id)





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
api_instance = oldp_client.CaseMarkersApi(oldp_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this case marker.

try:
    api_instance.case_markers_delete(id)
except ApiException as e:
    print("Exception when calling CaseMarkersApi->case_markers_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this case marker. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **case_markers_list**
> InlineResponse2002 case_markers_list(belongs_to=belongs_to, label=label, limit=limit, offset=offset)





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
api_instance = oldp_client.CaseMarkersApi(oldp_client.ApiClient(configuration))
belongs_to = 8.14 # float |  (optional)
label = 8.14 # float |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.case_markers_list(belongs_to=belongs_to, label=label, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseMarkersApi->case_markers_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **belongs_to** | **float**|  | [optional] 
 **label** | **float**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **case_markers_partial_update**
> CaseMarker case_markers_partial_update(id, data)





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
api_instance = oldp_client.CaseMarkersApi(oldp_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this case marker.
data = oldp_client.CaseMarker() # CaseMarker | 

try:
    api_response = api_instance.case_markers_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseMarkersApi->case_markers_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this case marker. | 
 **data** | [**CaseMarker**](CaseMarker.md)|  | 

### Return type

[**CaseMarker**](CaseMarker.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **case_markers_read**
> CaseMarker case_markers_read(id)





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
api_instance = oldp_client.CaseMarkersApi(oldp_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this case marker.

try:
    api_response = api_instance.case_markers_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseMarkersApi->case_markers_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this case marker. | 

### Return type

[**CaseMarker**](CaseMarker.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **case_markers_update**
> CaseMarker case_markers_update(id, data)





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
api_instance = oldp_client.CaseMarkersApi(oldp_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this case marker.
data = oldp_client.CaseMarker() # CaseMarker | 

try:
    api_response = api_instance.case_markers_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseMarkersApi->case_markers_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this case marker. | 
 **data** | [**CaseMarker**](CaseMarker.md)|  | 

### Return type

[**CaseMarker**](CaseMarker.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

