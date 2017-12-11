# swagger_client.TrafficApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**output_graph**](TrafficApi.md#output_graph) | **GET** /traffic/graph | Gives out a graph of how much traffic can be estimated
[**predict_time**](TrafficApi.md#predict_time) | **GET** /traffic | Analysis of the model


# **output_graph**
> output_graph(hour_of_the_day)

Gives out a graph of how much traffic can be estimated

This can only be done by the logged in user.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TrafficApi()
hour_of_the_day = 'hour_of_the_day_example' # str | The graph that needs to be fetched for the respective hour of travel. 

try: 
    # Gives out a graph of how much traffic can be estimated
    api_instance.output_graph(hour_of_the_day)
except ApiException as e:
    print("Exception when calling TrafficApi->output_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hour_of_the_day** | **str**| The graph that needs to be fetched for the respective hour of travel.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **predict_time**
> predict_time(choice)

Analysis of the model

Enter '1' for the predicted values or '2' for the information about the model.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TrafficApi()
choice = 'choice_example' # str | Accept input from user

try: 
    # Analysis of the model
    api_instance.predict_time(choice)
except ApiException as e:
    print("Exception when calling TrafficApi->predict_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **choice** | **str**| Accept input from user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

