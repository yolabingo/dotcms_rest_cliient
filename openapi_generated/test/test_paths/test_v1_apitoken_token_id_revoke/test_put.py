# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import dotcms_rest_client
from dotcms_rest_client.paths.v1_apitoken_token_id_revoke import put  # noqa: E501
from dotcms_rest_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1ApitokenTokenIdRevoke(ApiTestMixin, unittest.TestCase):
    """
    V1ApitokenTokenIdRevoke unit test stubs
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = put.ApiForput(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 0






if __name__ == '__main__':
    unittest.main()
