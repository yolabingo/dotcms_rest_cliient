# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import openapi_client
from openapi_client.paths.v1_contenttype_type_id_fields_id_field_id_variables_id_field_var_id import delete  # noqa: E501
from openapi_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1ContenttypeTypeIdFieldsIdFieldIdVariablesIdFieldVarId(ApiTestMixin, unittest.TestCase):
    """
    V1ContenttypeTypeIdFieldsIdFieldIdVariablesIdFieldVarId unit test stubs
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
