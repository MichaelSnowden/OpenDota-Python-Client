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


class InlineResponse20025(object):
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
        'match_id': 'float',
        'start_time': 'float',
        'hero_id': 'float',
        'score': 'float'
    }

    attribute_map = {
        'match_id': 'match_id',
        'start_time': 'start_time',
        'hero_id': 'hero_id',
        'score': 'score'
    }

    def __init__(self, match_id=None, start_time=None, hero_id=None, score=None):
        """
        InlineResponse20025 - a model defined in Swagger
        """

        self._match_id = None
        self._start_time = None
        self._hero_id = None
        self._score = None

        if match_id is not None:
          self.match_id = match_id
        if start_time is not None:
          self.start_time = start_time
        if hero_id is not None:
          self.hero_id = hero_id
        if score is not None:
          self.score = score

    @property
    def match_id(self):
        """
        Gets the match_id of this InlineResponse20025.
        match_id

        :return: The match_id of this InlineResponse20025.
        :rtype: float
        """
        return self._match_id

    @match_id.setter
    def match_id(self, match_id):
        """
        Sets the match_id of this InlineResponse20025.
        match_id

        :param match_id: The match_id of this InlineResponse20025.
        :type: float
        """

        self._match_id = match_id

    @property
    def start_time(self):
        """
        Gets the start_time of this InlineResponse20025.
        start_time

        :return: The start_time of this InlineResponse20025.
        :rtype: float
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this InlineResponse20025.
        start_time

        :param start_time: The start_time of this InlineResponse20025.
        :type: float
        """

        self._start_time = start_time

    @property
    def hero_id(self):
        """
        Gets the hero_id of this InlineResponse20025.
        hero_id

        :return: The hero_id of this InlineResponse20025.
        :rtype: float
        """
        return self._hero_id

    @hero_id.setter
    def hero_id(self, hero_id):
        """
        Sets the hero_id of this InlineResponse20025.
        hero_id

        :param hero_id: The hero_id of this InlineResponse20025.
        :type: float
        """

        self._hero_id = hero_id

    @property
    def score(self):
        """
        Gets the score of this InlineResponse20025.
        score

        :return: The score of this InlineResponse20025.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Sets the score of this InlineResponse20025.
        score

        :param score: The score of this InlineResponse20025.
        :type: float
        """

        self._score = score

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
        if not isinstance(other, InlineResponse20025):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
