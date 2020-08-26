# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: v0.12.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from onepanel.core.api.configuration import Configuration


class WorkflowTemplate(object):
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
        'created_at': 'str',
        'modified_at': 'str',
        'uid': 'str',
        'name': 'str',
        'version': 'str',
        'versions': 'str',
        'manifest': 'str',
        'is_latest': 'bool',
        'is_archived': 'bool',
        'labels': 'list[KeyValue]',
        'stats': 'WorkflowExecutionStatisticReport',
        'cron_stats': 'CronWorkflowStatisticsReport',
        'parameters': 'list[Parameter]'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'modified_at': 'modifiedAt',
        'uid': 'uid',
        'name': 'name',
        'version': 'version',
        'versions': 'versions',
        'manifest': 'manifest',
        'is_latest': 'isLatest',
        'is_archived': 'isArchived',
        'labels': 'labels',
        'stats': 'stats',
        'cron_stats': 'cronStats',
        'parameters': 'parameters'
    }

    def __init__(self, created_at=None, modified_at=None, uid=None, name=None, version=None, versions=None, manifest=None, is_latest=None, is_archived=None, labels=None, stats=None, cron_stats=None, parameters=None, local_vars_configuration=None):  # noqa: E501
        """WorkflowTemplate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_at = None
        self._modified_at = None
        self._uid = None
        self._name = None
        self._version = None
        self._versions = None
        self._manifest = None
        self._is_latest = None
        self._is_archived = None
        self._labels = None
        self._stats = None
        self._cron_stats = None
        self._parameters = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if modified_at is not None:
            self.modified_at = modified_at
        if uid is not None:
            self.uid = uid
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if versions is not None:
            self.versions = versions
        if manifest is not None:
            self.manifest = manifest
        if is_latest is not None:
            self.is_latest = is_latest
        if is_archived is not None:
            self.is_archived = is_archived
        if labels is not None:
            self.labels = labels
        if stats is not None:
            self.stats = stats
        if cron_stats is not None:
            self.cron_stats = cron_stats
        if parameters is not None:
            self.parameters = parameters

    @property
    def created_at(self):
        """Gets the created_at of this WorkflowTemplate.  # noqa: E501


        :return: The created_at of this WorkflowTemplate.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this WorkflowTemplate.


        :param created_at: The created_at of this WorkflowTemplate.  # noqa: E501
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this WorkflowTemplate.  # noqa: E501


        :return: The modified_at of this WorkflowTemplate.  # noqa: E501
        :rtype: str
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this WorkflowTemplate.


        :param modified_at: The modified_at of this WorkflowTemplate.  # noqa: E501
        :type modified_at: str
        """

        self._modified_at = modified_at

    @property
    def uid(self):
        """Gets the uid of this WorkflowTemplate.  # noqa: E501


        :return: The uid of this WorkflowTemplate.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this WorkflowTemplate.


        :param uid: The uid of this WorkflowTemplate.  # noqa: E501
        :type uid: str
        """

        self._uid = uid

    @property
    def name(self):
        """Gets the name of this WorkflowTemplate.  # noqa: E501


        :return: The name of this WorkflowTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkflowTemplate.


        :param name: The name of this WorkflowTemplate.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def version(self):
        """Gets the version of this WorkflowTemplate.  # noqa: E501


        :return: The version of this WorkflowTemplate.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this WorkflowTemplate.


        :param version: The version of this WorkflowTemplate.  # noqa: E501
        :type version: str
        """

        self._version = version

    @property
    def versions(self):
        """Gets the versions of this WorkflowTemplate.  # noqa: E501


        :return: The versions of this WorkflowTemplate.  # noqa: E501
        :rtype: str
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this WorkflowTemplate.


        :param versions: The versions of this WorkflowTemplate.  # noqa: E501
        :type versions: str
        """

        self._versions = versions

    @property
    def manifest(self):
        """Gets the manifest of this WorkflowTemplate.  # noqa: E501


        :return: The manifest of this WorkflowTemplate.  # noqa: E501
        :rtype: str
        """
        return self._manifest

    @manifest.setter
    def manifest(self, manifest):
        """Sets the manifest of this WorkflowTemplate.


        :param manifest: The manifest of this WorkflowTemplate.  # noqa: E501
        :type manifest: str
        """

        self._manifest = manifest

    @property
    def is_latest(self):
        """Gets the is_latest of this WorkflowTemplate.  # noqa: E501


        :return: The is_latest of this WorkflowTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._is_latest

    @is_latest.setter
    def is_latest(self, is_latest):
        """Sets the is_latest of this WorkflowTemplate.


        :param is_latest: The is_latest of this WorkflowTemplate.  # noqa: E501
        :type is_latest: bool
        """

        self._is_latest = is_latest

    @property
    def is_archived(self):
        """Gets the is_archived of this WorkflowTemplate.  # noqa: E501


        :return: The is_archived of this WorkflowTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """Sets the is_archived of this WorkflowTemplate.


        :param is_archived: The is_archived of this WorkflowTemplate.  # noqa: E501
        :type is_archived: bool
        """

        self._is_archived = is_archived

    @property
    def labels(self):
        """Gets the labels of this WorkflowTemplate.  # noqa: E501


        :return: The labels of this WorkflowTemplate.  # noqa: E501
        :rtype: list[KeyValue]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this WorkflowTemplate.


        :param labels: The labels of this WorkflowTemplate.  # noqa: E501
        :type labels: list[KeyValue]
        """

        self._labels = labels

    @property
    def stats(self):
        """Gets the stats of this WorkflowTemplate.  # noqa: E501


        :return: The stats of this WorkflowTemplate.  # noqa: E501
        :rtype: WorkflowExecutionStatisticReport
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this WorkflowTemplate.


        :param stats: The stats of this WorkflowTemplate.  # noqa: E501
        :type stats: WorkflowExecutionStatisticReport
        """

        self._stats = stats

    @property
    def cron_stats(self):
        """Gets the cron_stats of this WorkflowTemplate.  # noqa: E501


        :return: The cron_stats of this WorkflowTemplate.  # noqa: E501
        :rtype: CronWorkflowStatisticsReport
        """
        return self._cron_stats

    @cron_stats.setter
    def cron_stats(self, cron_stats):
        """Sets the cron_stats of this WorkflowTemplate.


        :param cron_stats: The cron_stats of this WorkflowTemplate.  # noqa: E501
        :type cron_stats: CronWorkflowStatisticsReport
        """

        self._cron_stats = cron_stats

    @property
    def parameters(self):
        """Gets the parameters of this WorkflowTemplate.  # noqa: E501


        :return: The parameters of this WorkflowTemplate.  # noqa: E501
        :rtype: list[Parameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this WorkflowTemplate.


        :param parameters: The parameters of this WorkflowTemplate.  # noqa: E501
        :type parameters: list[Parameter]
        """

        self._parameters = parameters

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
        if not isinstance(other, WorkflowTemplate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkflowTemplate):
            return True

        return self.to_dict() != other.to_dict()
