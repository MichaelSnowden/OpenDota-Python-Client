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


class InlineResponse20015(object):
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
        'match_seq_num': 'float',
        'radiant_win': 'float',
        'start_time': 'float',
        'duration': 'float',
        'avg_mmr': 'float',
        'num_mmr': 'float',
        'radiant_team': 'str',
        'dire_team': 'str'
    }

    attribute_map = {
        'match_id': 'match_id',
        'match_seq_num': 'match_seq_num',
        'radiant_win': 'radiant_win',
        'start_time': 'start_time',
        'duration': 'duration',
        'avg_mmr': 'avg_mmr',
        'num_mmr': 'num_mmr',
        'radiant_team': 'radiant_team',
        'dire_team': 'dire_team'
    }

    def __init__(self, match_id=None, match_seq_num=None, radiant_win=None, start_time=None, duration=None, avg_mmr=None, num_mmr=None, radiant_team=None, dire_team=None):
        """
        InlineResponse20015 - a model defined in Swagger
        """

        self._match_id = None
        self._match_seq_num = None
        self._radiant_win = None
        self._start_time = None
        self._duration = None
        self._avg_mmr = None
        self._num_mmr = None
        self._radiant_team = None
        self._dire_team = None

        if match_id is not None:
          self.match_id = match_id
        if match_seq_num is not None:
          self.match_seq_num = match_seq_num
        if radiant_win is not None:
          self.radiant_win = radiant_win
        if start_time is not None:
          self.start_time = start_time
        if duration is not None:
          self.duration = duration
        if avg_mmr is not None:
          self.avg_mmr = avg_mmr
        if num_mmr is not None:
          self.num_mmr = num_mmr
        if radiant_team is not None:
          self.radiant_team = radiant_team
        if dire_team is not None:
          self.dire_team = dire_team

    @property
    def match_id(self):
        """
        Gets the match_id of this InlineResponse20015.
        match_id

        :return: The match_id of this InlineResponse20015.
        :rtype: float
        """
        return self._match_id

    @match_id.setter
    def match_id(self, match_id):
        """
        Sets the match_id of this InlineResponse20015.
        match_id

        :param match_id: The match_id of this InlineResponse20015.
        :type: float
        """

        self._match_id = match_id

    @property
    def match_seq_num(self):
        """
        Gets the match_seq_num of this InlineResponse20015.
        match_seq_num

        :return: The match_seq_num of this InlineResponse20015.
        :rtype: float
        """
        return self._match_seq_num

    @match_seq_num.setter
    def match_seq_num(self, match_seq_num):
        """
        Sets the match_seq_num of this InlineResponse20015.
        match_seq_num

        :param match_seq_num: The match_seq_num of this InlineResponse20015.
        :type: float
        """

        self._match_seq_num = match_seq_num

    @property
    def radiant_win(self):
        """
        Gets the radiant_win of this InlineResponse20015.
        radiant_win

        :return: The radiant_win of this InlineResponse20015.
        :rtype: float
        """
        return self._radiant_win

    @radiant_win.setter
    def radiant_win(self, radiant_win):
        """
        Sets the radiant_win of this InlineResponse20015.
        radiant_win

        :param radiant_win: The radiant_win of this InlineResponse20015.
        :type: float
        """

        self._radiant_win = radiant_win

    @property
    def start_time(self):
        """
        Gets the start_time of this InlineResponse20015.
        start_time

        :return: The start_time of this InlineResponse20015.
        :rtype: float
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this InlineResponse20015.
        start_time

        :param start_time: The start_time of this InlineResponse20015.
        :type: float
        """

        self._start_time = start_time

    @property
    def duration(self):
        """
        Gets the duration of this InlineResponse20015.
        duration

        :return: The duration of this InlineResponse20015.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this InlineResponse20015.
        duration

        :param duration: The duration of this InlineResponse20015.
        :type: float
        """

        self._duration = duration

    @property
    def avg_mmr(self):
        """
        Gets the avg_mmr of this InlineResponse20015.
        avg_mmr

        :return: The avg_mmr of this InlineResponse20015.
        :rtype: float
        """
        return self._avg_mmr

    @avg_mmr.setter
    def avg_mmr(self, avg_mmr):
        """
        Sets the avg_mmr of this InlineResponse20015.
        avg_mmr

        :param avg_mmr: The avg_mmr of this InlineResponse20015.
        :type: float
        """

        self._avg_mmr = avg_mmr

    @property
    def num_mmr(self):
        """
        Gets the num_mmr of this InlineResponse20015.
        num_mmr

        :return: The num_mmr of this InlineResponse20015.
        :rtype: float
        """
        return self._num_mmr

    @num_mmr.setter
    def num_mmr(self, num_mmr):
        """
        Sets the num_mmr of this InlineResponse20015.
        num_mmr

        :param num_mmr: The num_mmr of this InlineResponse20015.
        :type: float
        """

        self._num_mmr = num_mmr

    @property
    def radiant_team(self):
        """
        Gets the radiant_team of this InlineResponse20015.
        radiant_team

        :return: The radiant_team of this InlineResponse20015.
        :rtype: str
        """
        return self._radiant_team

    @radiant_team.setter
    def radiant_team(self, radiant_team):
        """
        Sets the radiant_team of this InlineResponse20015.
        radiant_team

        :param radiant_team: The radiant_team of this InlineResponse20015.
        :type: str
        """

        self._radiant_team = radiant_team

    @property
    def dire_team(self):
        """
        Gets the dire_team of this InlineResponse20015.
        dire_team

        :return: The dire_team of this InlineResponse20015.
        :rtype: str
        """
        return self._dire_team

    @dire_team.setter
    def dire_team(self, dire_team):
        """
        Sets the dire_team of this InlineResponse20015.
        dire_team

        :param dire_team: The dire_team of this InlineResponse20015.
        :type: str
        """

        self._dire_team = dire_team

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
        if not isinstance(other, InlineResponse20015):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other