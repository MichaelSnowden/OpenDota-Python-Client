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


class InlineResponse20012(object):
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
        'account_id': 'float',
        'match_id': 'float',
        'solo_competitive_rank': 'float',
        'competitive_rank': 'float'
    }

    attribute_map = {
        'account_id': 'account_id',
        'match_id': 'match_id',
        'solo_competitive_rank': 'solo_competitive_rank',
        'competitive_rank': 'competitive_rank'
    }

    def __init__(self, account_id=None, match_id=None, solo_competitive_rank=None, competitive_rank=None):
        """
        InlineResponse20012 - a model defined in Swagger
        """

        self._account_id = None
        self._match_id = None
        self._solo_competitive_rank = None
        self._competitive_rank = None

        if account_id is not None:
          self.account_id = account_id
        if match_id is not None:
          self.match_id = match_id
        if solo_competitive_rank is not None:
          self.solo_competitive_rank = solo_competitive_rank
        if competitive_rank is not None:
          self.competitive_rank = competitive_rank

    @property
    def account_id(self):
        """
        Gets the account_id of this InlineResponse20012.
        account_id

        :return: The account_id of this InlineResponse20012.
        :rtype: float
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this InlineResponse20012.
        account_id

        :param account_id: The account_id of this InlineResponse20012.
        :type: float
        """

        self._account_id = account_id

    @property
    def match_id(self):
        """
        Gets the match_id of this InlineResponse20012.
        match_id

        :return: The match_id of this InlineResponse20012.
        :rtype: float
        """
        return self._match_id

    @match_id.setter
    def match_id(self, match_id):
        """
        Sets the match_id of this InlineResponse20012.
        match_id

        :param match_id: The match_id of this InlineResponse20012.
        :type: float
        """

        self._match_id = match_id

    @property
    def solo_competitive_rank(self):
        """
        Gets the solo_competitive_rank of this InlineResponse20012.
        solo_competitive_rank

        :return: The solo_competitive_rank of this InlineResponse20012.
        :rtype: float
        """
        return self._solo_competitive_rank

    @solo_competitive_rank.setter
    def solo_competitive_rank(self, solo_competitive_rank):
        """
        Sets the solo_competitive_rank of this InlineResponse20012.
        solo_competitive_rank

        :param solo_competitive_rank: The solo_competitive_rank of this InlineResponse20012.
        :type: float
        """

        self._solo_competitive_rank = solo_competitive_rank

    @property
    def competitive_rank(self):
        """
        Gets the competitive_rank of this InlineResponse20012.
        competitive_rank

        :return: The competitive_rank of this InlineResponse20012.
        :rtype: float
        """
        return self._competitive_rank

    @competitive_rank.setter
    def competitive_rank(self, competitive_rank):
        """
        Sets the competitive_rank of this InlineResponse20012.
        competitive_rank

        :param competitive_rank: The competitive_rank of this InlineResponse20012.
        :type: float
        """

        self._competitive_rank = competitive_rank

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
        if not isinstance(other, InlineResponse20012):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
