# coding: utf-8

"""
    Open Legal Data API

    With the Open Legal Data API you can access various data from the legal domain, e.g. law text or case files. The data may be used for semantic analysis or to create statistics. For more information visit our website.  # noqa: E501

    OpenAPI spec version: v1
    Contact: api@openlegaldata.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import oldp_client
from oldp_client.models.case import Case  # noqa: E501
from oldp_client.rest import ApiException


class TestCase(unittest.TestCase):
    """Case unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCase(self):
        """Test Case"""
        # FIXME: construct object with mandatory attributes with example values
        # model = oldp_client.models.case.Case()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
