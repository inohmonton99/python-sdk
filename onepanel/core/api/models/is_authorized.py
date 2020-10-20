# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 0.14.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from onepanel.core.api.configuration import Configuration


class IsAuthorized(object):
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
        'namespace': 'str',
        'verb': 'str',
        'group': 'str',
        'resource': 'str',
        'resource_name': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'verb': 'verb',
        'group': 'group',
        'resource': 'resource',
        'resource_name': 'resourceName'
    }

    def __init__(self, namespace=None, verb=None, group=None, resource=None, resource_name=None, local_vars_configuration=None):  # noqa: E501
        """IsAuthorized - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._namespace = None
        self._verb = None
        self._group = None
        self._resource = None
        self._resource_name = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if verb is not None:
            self.verb = verb
        if group is not None:
            self.group = group
        if resource is not None:
            self.resource = resource
        if resource_name is not None:
            self.resource_name = resource_name

    @property
    def namespace(self):
        """Gets the namespace of this IsAuthorized.  # noqa: E501


        :return: The namespace of this IsAuthorized.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this IsAuthorized.


        :param namespace: The namespace of this IsAuthorized.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def verb(self):
        """Gets the verb of this IsAuthorized.  # noqa: E501


        :return: The verb of this IsAuthorized.  # noqa: E501
        :rtype: str
        """
        return self._verb

    @verb.setter
    def verb(self, verb):
        """Sets the verb of this IsAuthorized.


        :param verb: The verb of this IsAuthorized.  # noqa: E501
        :type: str
        """

        self._verb = verb

    @property
    def group(self):
        """Gets the group of this IsAuthorized.  # noqa: E501


        :return: The group of this IsAuthorized.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this IsAuthorized.


        :param group: The group of this IsAuthorized.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def resource(self):
        """Gets the resource of this IsAuthorized.  # noqa: E501


        :return: The resource of this IsAuthorized.  # noqa: E501
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this IsAuthorized.


        :param resource: The resource of this IsAuthorized.  # noqa: E501
        :type: str
        """

        self._resource = resource

    @property
    def resource_name(self):
        """Gets the resource_name of this IsAuthorized.  # noqa: E501


        :return: The resource_name of this IsAuthorized.  # noqa: E501
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this IsAuthorized.


        :param resource_name: The resource_name of this IsAuthorized.  # noqa: E501
        :type: str
        """

        self._resource_name = resource_name

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
        if not isinstance(other, IsAuthorized):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IsAuthorized):
            return True

        return self.to_dict() != other.to_dict()
