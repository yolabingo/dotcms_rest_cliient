# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import openapi_client
from openapi_client.paths.v1_esindex_index_name import delete  # noqa: E501
from openapi_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1EsindexIndexName(ApiTestMixin, unittest.TestCase):
    """
    V1EsindexIndexName unit test stubs
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 0




if __name__ == '__main__':
    unittest.main()
