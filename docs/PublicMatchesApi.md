# swagger_client.PublicMatchesApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**public_matches_get**](PublicMatchesApi.md#public_matches_get) | **GET** /publicMatches | GET /publicMatches


# **public_matches_get**
> list[InlineResponse20015] public_matches_get(mmr_ascending=mmr_ascending)

GET /publicMatches

Get list of randomly sampled public matches ordered by MMR

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublicMatchesApi()
mmr_ascending = 56 # int | Order by MMR ascending (optional)

try: 
    # GET /publicMatches
    api_response = api_instance.public_matches_get(mmr_ascending=mmr_ascending)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicMatchesApi->public_matches_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mmr_ascending** | **int**| Order by MMR ascending | [optional] 

### Return type

[**list[InlineResponse20015]**](InlineResponse20015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

