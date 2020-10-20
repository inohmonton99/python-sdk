# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 0.13.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import onepanel.core.api
from onepanel.core.api.models.get_workspace_statistics_for_namespace_response import GetWorkspaceStatisticsForNamespaceResponse  # noqa: E501
from onepanel.core.api.rest import ApiException

class TestGetWorkspaceStatisticsForNamespaceResponse(unittest.TestCase):
    """GetWorkspaceStatisticsForNamespaceResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetWorkspaceStatisticsForNamespaceResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = onepanel.core.api.models.get_workspace_statistics_for_namespace_response.GetWorkspaceStatisticsForNamespaceResponse()  # noqa: E501
        if include_optional :
            return GetWorkspaceStatisticsForNamespaceResponse(
                stats = onepanel.core.api.models.workspace_statistic_report.WorkspaceStatisticReport(
                    total = 56, 
                    last_created = '0', 
                    launching = 56, 
                    running = 56, 
                    updating = 56, 
                    pausing = 56, 
                    paused = 56, 
                    terminating = 56, 
                    terminated = 56, 
                    failed_to_pause = 56, 
                    failed_to_resume = 56, 
                    failed_to_terminate = 56, 
                    failed_to_launch = 56, 
                    failed_to_update = 56, 
                    failed = 56, )
            )
        else :
            return GetWorkspaceStatisticsForNamespaceResponse(
        )

    def testGetWorkspaceStatisticsForNamespaceResponse(self):
        """Test GetWorkspaceStatisticsForNamespaceResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()