# coding: utf-8

"""
    OpenDota API

    # Introduction This API provides Dota 2 related data. Please keep request rate to approximately 1/s. 

    OpenAPI spec version: 14.3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.teams_api import TeamsApi


class TestTeamsApi(unittest.TestCase):
    """ TeamsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.teams_api.TeamsApi()

    def tearDown(self):
        pass

    def test_teams_get(self):
        """
        Test case for teams_get

        GET /teams
        """
        pass


if __name__ == '__main__':
    unittest.main()
