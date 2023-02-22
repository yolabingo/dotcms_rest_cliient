# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import openapi_client
from openapi_client.paths.v1_workflow_actions_default_firemultipart_system_action import put  # noqa: E501
from openapi_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1WorkflowActionsDefaultFiremultipartSystemAction(ApiTestMixin, unittest.TestCase):
    """
    V1WorkflowActionsDefaultFiremultipartSystemAction unit test stubs
        Fire default action by name multipart  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = put.ApiForput(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
