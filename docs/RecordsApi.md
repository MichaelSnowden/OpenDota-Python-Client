# swagger_client.RecordsApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**records_field_get**](RecordsApi.md#records_field_get) | **GET** /records/{field} | GET /records/{field}


# **records_field_get**
> list[InlineResponse20025] records_field_get(field)

GET /records/{field}

Get top performances in a stat

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RecordsApi()
field = 'field_example' # str | Field name to query

try: 
    # GET /records/{field}
    api_response = api_instance.records_field_get(field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordsApi->records_field_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**| Field name to query | 

### Return type

[**list[InlineResponse20025]**](InlineResponse20025.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

