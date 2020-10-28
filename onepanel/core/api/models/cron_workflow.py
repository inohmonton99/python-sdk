# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 0.15.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from onepanel.core.api.configuration import Configuration


class CronWorkflow(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'uid': 'str',
        'manifest': 'str',
        'workflow_execution': 'WorkflowExecution',
        'labels': 'list[KeyValue]',
        'namespace': 'str'
    }

    attribute_map = {
        'name': 'name',
        'uid': 'uid',
        'manifest': 'manifest',
        'workflow_execution': 'workflowExecution',
        'labels': 'labels',
        'namespace': 'namespace'
    }

    def __init__(self, name=None, uid=None, manifest=None, workflow_execution=None, labels=None, namespace=None, local_vars_configuration=None):  # noqa: E501
        """CronWorkflow - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._uid = None
        self._manifest = None
        self._workflow_execution = None
        self._labels = None
        self._namespace = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if uid is not None:
            self.uid = uid
        if manifest is not None:
            self.manifest = manifest
        if workflow_execution is not None:
            self.workflow_execution = workflow_execution
        if labels is not None:
            self.labels = labels
        if namespace is not None:
            self.namespace = namespace

    @property
    def name(self):
        """Gets the name of this CronWorkflow.  # noqa: E501


        :return: The name of this CronWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CronWorkflow.


        :param name: The name of this CronWorkflow.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def uid(self):
        """Gets the uid of this CronWorkflow.  # noqa: E501


        :return: The uid of this CronWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this CronWorkflow.


        :param uid: The uid of this CronWorkflow.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def manifest(self):
        """Gets the manifest of this CronWorkflow.  # noqa: E501


        :return: The manifest of this CronWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._manifest

    @manifest.setter
    def manifest(self, manifest):
        """Sets the manifest of this CronWorkflow.


        :param manifest: The manifest of this CronWorkflow.  # noqa: E501
        :type: str
        """

        self._manifest = manifest

    @property
    def workflow_execution(self):
        """Gets the workflow_execution of this CronWorkflow.  # noqa: E501


        :return: The workflow_execution of this CronWorkflow.  # noqa: E501
        :rtype: WorkflowExecution
        """
        return self._workflow_execution

    @workflow_execution.setter
    def workflow_execution(self, workflow_execution):
        """Sets the workflow_execution of this CronWorkflow.


        :param workflow_execution: The workflow_execution of this CronWorkflow.  # noqa: E501
        :type: WorkflowExecution
        """

        self._workflow_execution = workflow_execution

    @property
    def labels(self):
        """Gets the labels of this CronWorkflow.  # noqa: E501


        :return: The labels of this CronWorkflow.  # noqa: E501
        :rtype: list[KeyValue]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this CronWorkflow.


        :param labels: The labels of this CronWorkflow.  # noqa: E501
        :type: list[KeyValue]
        """

        self._labels = labels

    @property
    def namespace(self):
        """Gets the namespace of this CronWorkflow.  # noqa: E501


        :return: The namespace of this CronWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this CronWorkflow.


        :param namespace: The namespace of this CronWorkflow.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CronWorkflow):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CronWorkflow):
            return True

        return self.to_dict() != other.to_dict()
