# coding: utf-8

"""
    OpenDota API

    # Introduction This API provides Dota 2 related data. Please keep request rate to approximately 1/s. 

    OpenAPI spec version: 14.3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InlineResponse20022(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'float',
        'name': 'str',
        'localized_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'localized_name': 'localized_name'
    }

    def __init__(self, id=None, name=None, localized_name=None):
        """
        InlineResponse20022 - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._localized_name = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if localized_name is not None:
          self.localized_name = localized_name

    @property
    def id(self):
        """
        Gets the id of this InlineResponse20022.
        id

        :return: The id of this InlineResponse20022.
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InlineResponse20022.
        id

        :param id: The id of this InlineResponse20022.
        :type: float
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this InlineResponse20022.
        name

        :return: The name of this InlineResponse20022.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InlineResponse20022.
        name

        :param name: The name of this InlineResponse20022.
        :type: str
        """

        self._name = name

    @property
    def localized_name(self):
        """
        Gets the localized_name of this InlineResponse20022.
        localized_name

        :return: The localized_name of this InlineResponse20022.
        :rtype: str
        """
        return self._localized_name

    @localized_name.setter
    def localized_name(self, localized_name):
        """
        Sets the localized_name of this InlineResponse20022.
        localized_name

        :param localized_name: The localized_name of this InlineResponse20022.
        :type: str
        """

        self._localized_name = localized_name

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, InlineResponse20022):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
