# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import dotcms_rest_client
from dotcms_rest_client.paths.v2_contenttype_type_id_or_var_name_fields_id_field_id import delete  # noqa: E501
from dotcms_rest_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV2ContenttypeTypeIdOrVarNameFieldsIdFieldId(ApiTestMixin, unittest.TestCase):
    """
    V2ContenttypeTypeIdOrVarNameFieldsIdFieldId unit test stubs
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
