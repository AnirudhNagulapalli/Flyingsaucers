# coding: utf-8

"""
    Flying Saucers

    This is for MSCS710 Project Course

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into sdk package
from .models.user import User

# import apis into sdk package
from .apis.traffic_api import TrafficApi
from .apis.user_api import UserApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()