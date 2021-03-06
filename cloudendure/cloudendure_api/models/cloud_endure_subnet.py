# coding: utf-8

"""
    CloudEndure API documentation

    © 2017 CloudEndure All rights reserved  # General Request authentication in CloudEndure's API is done using session cookies. A session cookie is returned upon successful execution of the \"login\" method. This value must then be provided within the request headers of all subsequent API requests.  ## Errors Some errors are not specifically written in every method since they may always return. Those are: 1) 401 (Unauthorized) - for unauthenticated requests. 2) 405 (Method Not Allowed) - for using a method that is not supported (POST instead of GET). 3) 403 (Forbidden) - request is authenticated, but the user is not allowed to access. 4) 422 (Unprocessable Entity) - for invalid input.  ## Formats All strings with date-time format are according to RFC3339.  All strings with \"duration\" format are according to ISO8601. For example, a full day duration can be specified with \"PNNNND\".   # noqa: E501

    OpenAPI spec version: 5
    Contact: https://bit.ly/2T54hSc
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class CloudEndureSubnet:
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {"subnet_id": "str", "network_id": "str", "name": "str"}

    attribute_map = {"subnet_id": "subnetId", "network_id": "networkId", "name": "name"}

    def __init__(self, subnet_id=None, network_id=None, name=None):  # noqa: E501
        """CloudEndureSubnet - a model defined in Swagger"""  # noqa: E501
        self._subnet_id = None
        self._network_id = None
        self._name = None
        self.discriminator = None
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if network_id is not None:
            self.network_id = network_id
        if name is not None:
            self.name = name

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CloudEndureSubnet.  # noqa: E501


        :return: The subnet_id of this CloudEndureSubnet.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CloudEndureSubnet.


        :param subnet_id: The subnet_id of this CloudEndureSubnet.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

    @property
    def network_id(self):
        """Gets the network_id of this CloudEndureSubnet.  # noqa: E501


        :return: The network_id of this CloudEndureSubnet.  # noqa: E501
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this CloudEndureSubnet.


        :param network_id: The network_id of this CloudEndureSubnet.  # noqa: E501
        :type: str
        """

        self._network_id = network_id

    @property
    def name(self):
        """Gets the name of this CloudEndureSubnet.  # noqa: E501


        :return: The name of this CloudEndureSubnet.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloudEndureSubnet.


        :param name: The name of this CloudEndureSubnet.  # noqa: E501
        :type: str
        """

        self._name = name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(CloudEndureSubnet, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CloudEndureSubnet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
