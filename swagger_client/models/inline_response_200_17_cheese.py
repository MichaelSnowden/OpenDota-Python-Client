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


class InlineResponse20017Cheese(object):
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
        'cheese': 'str',
        'goal': 'str'
    }

    attribute_map = {
        'cheese': 'cheese',
        'goal': 'goal'
    }

    def __init__(self, cheese=None, goal=None):
        """
        InlineResponse20017Cheese - a model defined in Swagger
        """

        self._cheese = None
        self._goal = None

        if cheese is not None:
          self.cheese = cheese
        if goal is not None:
          self.goal = goal

    @property
    def cheese(self):
        """
        Gets the cheese of this InlineResponse20017Cheese.
        cheese

        :return: The cheese of this InlineResponse20017Cheese.
        :rtype: str
        """
        return self._cheese

    @cheese.setter
    def cheese(self, cheese):
        """
        Sets the cheese of this InlineResponse20017Cheese.
        cheese

        :param cheese: The cheese of this InlineResponse20017Cheese.
        :type: str
        """

        self._cheese = cheese

    @property
    def goal(self):
        """
        Gets the goal of this InlineResponse20017Cheese.
        goal

        :return: The goal of this InlineResponse20017Cheese.
        :rtype: str
        """
        return self._goal

    @goal.setter
    def goal(self, goal):
        """
        Sets the goal of this InlineResponse20017Cheese.
        goal

        :param goal: The goal of this InlineResponse20017Cheese.
        :type: str
        """

        self._goal = goal

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
        if not isinstance(other, InlineResponse20017Cheese):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
