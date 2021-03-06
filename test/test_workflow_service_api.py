# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 0.12.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import onepanel.core.api
from onepanel.core.api.api.workflow_service_api import WorkflowServiceApi  # noqa: E501
from onepanel.core.api.rest import ApiException


class TestWorkflowServiceApi(unittest.TestCase):
    """WorkflowServiceApi unit test stubs"""

    def setUp(self):
        self.api = onepanel.core.api.api.workflow_service_api.WorkflowServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_workflow_execution_statistics(self):
        """Test case for add_workflow_execution_statistics

        """
        pass

    def test_clone_workflow_execution(self):
        """Test case for clone_workflow_execution

        """
        pass

    def test_create_workflow_execution(self):
        """Test case for create_workflow_execution

        """
        pass

    def test_cron_start_workflow_execution_statistic(self):
        """Test case for cron_start_workflow_execution_statistic

        """
        pass

    def test_get_artifact(self):
        """Test case for get_artifact

        """
        pass

    def test_get_workflow_execution(self):
        """Test case for get_workflow_execution

        """
        pass

    def test_get_workflow_execution_logs(self):
        """Test case for get_workflow_execution_logs

        """
        pass

    def test_get_workflow_execution_metrics(self):
        """Test case for get_workflow_execution_metrics

        """
        pass

    def test_list_files(self):
        """Test case for list_files

        """
        pass

    def test_list_workflow_executions(self):
        """Test case for list_workflow_executions

        """
        pass

    def test_resubmit_workflow_execution(self):
        """Test case for resubmit_workflow_execution

        """
        pass

    def test_terminate_workflow_execution(self):
        """Test case for terminate_workflow_execution

        """
        pass

    def test_update_workflow_execution_status(self):
        """Test case for update_workflow_execution_status

        """
        pass

    def test_watch_workflow_execution(self):
        """Test case for watch_workflow_execution

        """
        pass


if __name__ == '__main__':
    unittest.main()
