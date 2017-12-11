# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestTrafficController(BaseTestCase):
    """ TrafficController integration test stubs """

    def test_output_graph(self):
        """
        Test case for output_graph

        Gives out a graph of how much traffic can be estimated
        """
        query_string = [('hour_of_the_day', 'hour_of_the_day_example')]
        response = self.client.open('/traffic/graph',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_predict_time(self):
        """
        Test case for predict_time

        Analysis of the model
        """
        query_string = [('Choice', 'Choice_example')]
        response = self.client.open('/traffic',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
