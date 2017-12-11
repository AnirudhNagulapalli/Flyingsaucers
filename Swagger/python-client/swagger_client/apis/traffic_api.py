# coding: utf-8

"""
    Flying Saucers

    This is for MSCS710 Project Course

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class TrafficApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def output_graph(self, hour_of_the_day, **kwargs):
        """
        Gives out a graph of how much traffic can be estimated
        This can only be done by the logged in user.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.output_graph(hour_of_the_day, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str hour_of_the_day: The graph that needs to be fetched for the respective hour of travel.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.output_graph_with_http_info(hour_of_the_day, **kwargs)
        else:
            (data) = self.output_graph_with_http_info(hour_of_the_day, **kwargs)
            return data

    def output_graph_with_http_info(self, hour_of_the_day, **kwargs):
        """
        Gives out a graph of how much traffic can be estimated
        This can only be done by the logged in user.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.output_graph_with_http_info(hour_of_the_day, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str hour_of_the_day: The graph that needs to be fetched for the respective hour of travel.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hour_of_the_day']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method output_graph" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hour_of_the_day' is set
        if ('hour_of_the_day' not in params) or (params['hour_of_the_day'] is None):
            raise ValueError("Missing the required parameter `hour_of_the_day` when calling `output_graph`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'hour_of_the_day' in params:
            query_params.append(('hour_of_the_day', params['hour_of_the_day']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/xml', 'application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/traffic/graph', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def predict_time(self, choice, **kwargs):
        """
        Analysis of the model
        Enter '1' for the predicted values or '2' for the information about the model.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.predict_time(choice, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str choice: Accept input from user (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.predict_time_with_http_info(choice, **kwargs)
        else:
            (data) = self.predict_time_with_http_info(choice, **kwargs)
            return data

    def predict_time_with_http_info(self, choice, **kwargs):
        """
        Analysis of the model
        Enter '1' for the predicted values or '2' for the information about the model.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.predict_time_with_http_info(choice, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str choice: Accept input from user (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['choice']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method predict_time" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'choice' is set
        if ('choice' not in params) or (params['choice'] is None):
            raise ValueError("Missing the required parameter `choice` when calling `predict_time`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'choice' in params:
            query_params.append(('Choice', params['choice']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/xml', 'application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/traffic', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)