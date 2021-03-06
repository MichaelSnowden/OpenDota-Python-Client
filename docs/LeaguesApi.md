# swagger_client.LeaguesApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**leagues_get**](LeaguesApi.md#leagues_get) | **GET** /leagues | GET /leagues


# **leagues_get**
> list[InlineResponse20023] leagues_get()

GET /leagues

Get league data

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LeaguesApi()

try: 
    # GET /leagues
    api_response = api_instance.leagues_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaguesApi->leagues_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse20023]**](InlineResponse20023.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

