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


class InlineResponse2003(object):
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
        'player_slot': 'float',
        'radiant_win': 'bool',
        'duration': 'float',
        'game_mode': 'float',
        'lobby_type': 'float',
        'hero_id': 'float',
        'start_time': 'float',
        'version': 'float',
        'kills': 'float',
        'deaths': 'float',
        'assists': 'float',
        'skill': 'float',
        'lane': 'float',
        'lane_role': 'float'
    }

    attribute_map = {
        'match_id': 'match_id',
        'player_slot': 'player_slot',
        'radiant_win': 'radiant_win',
        'duration': 'duration',
        'game_mode': 'game_mode',
        'lobby_type': 'lobby_type',
        'hero_id': 'hero_id',
        'start_time': 'start_time',
        'version': 'version',
        'kills': 'kills',
        'deaths': 'deaths',
        'assists': 'assists',
        'skill': 'skill',
        'lane': 'lane',
        'lane_role': 'lane_role'
    }

    def __init__(self, match_id=None, player_slot=None, radiant_win=None, duration=None, game_mode=None, lobby_type=None, hero_id=None, start_time=None, version=None, kills=None, deaths=None, assists=None, skill=None, lane=None, lane_role=None):
        """
        InlineResponse2003 - a model defined in Swagger
        """

        self._match_id = None
        self._player_slot = None
        self._radiant_win = None
        self._duration = None
        self._game_mode = None
        self._lobby_type = None
        self._hero_id = None
        self._start_time = None
        self._version = None
        self._kills = None
        self._deaths = None
        self._assists = None
        self._skill = None
        self._lane = None
        self._lane_role = None

        if match_id is not None:
          self.match_id = match_id
        if player_slot is not None:
          self.player_slot = player_slot
        if radiant_win is not None:
          self.radiant_win = radiant_win
        if duration is not None:
          self.duration = duration
        if game_mode is not None:
          self.game_mode = game_mode
        if lobby_type is not None:
          self.lobby_type = lobby_type
        if hero_id is not None:
          self.hero_id = hero_id
        if start_time is not None:
          self.start_time = start_time
        if version is not None:
          self.version = version
        if kills is not None:
          self.kills = kills
        if deaths is not None:
          self.deaths = deaths
        if assists is not None:
          self.assists = assists
        if skill is not None:
          self.skill = skill
        if lane is not None:
          self.lane = lane
        if lane_role is not None:
          self.lane_role = lane_role

    @property
    def match_id(self):
        """
        Gets the match_id of this InlineResponse2003.
        match_id

        :return: The match_id of this InlineResponse2003.
        :rtype: float
        """
        return self._match_id

    @match_id.setter
    def match_id(self, match_id):
        """
        Sets the match_id of this InlineResponse2003.
        match_id

        :param match_id: The match_id of this InlineResponse2003.
        :type: float
        """

        self._match_id = match_id

    @property
    def player_slot(self):
        """
        Gets the player_slot of this InlineResponse2003.
        player_slot

        :return: The player_slot of this InlineResponse2003.
        :rtype: float
        """
        return self._player_slot

    @player_slot.setter
    def player_slot(self, player_slot):
        """
        Sets the player_slot of this InlineResponse2003.
        player_slot

        :param player_slot: The player_slot of this InlineResponse2003.
        :type: float
        """

        self._player_slot = player_slot

    @property
    def radiant_win(self):
        """
        Gets the radiant_win of this InlineResponse2003.
        radiant_win

        :return: The radiant_win of this InlineResponse2003.
        :rtype: bool
        """
        return self._radiant_win

    @radiant_win.setter
    def radiant_win(self, radiant_win):
        """
        Sets the radiant_win of this InlineResponse2003.
        radiant_win

        :param radiant_win: The radiant_win of this InlineResponse2003.
        :type: bool
        """

        self._radiant_win = radiant_win

    @property
    def duration(self):
        """
        Gets the duration of this InlineResponse2003.
        duration

        :return: The duration of this InlineResponse2003.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this InlineResponse2003.
        duration

        :param duration: The duration of this InlineResponse2003.
        :type: float
        """

        self._duration = duration

    @property
    def game_mode(self):
        """
        Gets the game_mode of this InlineResponse2003.
        game_mode

        :return: The game_mode of this InlineResponse2003.
        :rtype: float
        """
        return self._game_mode

    @game_mode.setter
    def game_mode(self, game_mode):
        """
        Sets the game_mode of this InlineResponse2003.
        game_mode

        :param game_mode: The game_mode of this InlineResponse2003.
        :type: float
        """

        self._game_mode = game_mode

    @property
    def lobby_type(self):
        """
        Gets the lobby_type of this InlineResponse2003.
        lobby_type

        :return: The lobby_type of this InlineResponse2003.
        :rtype: float
        """
        return self._lobby_type

    @lobby_type.setter
    def lobby_type(self, lobby_type):
        """
        Sets the lobby_type of this InlineResponse2003.
        lobby_type

        :param lobby_type: The lobby_type of this InlineResponse2003.
        :type: float
        """

        self._lobby_type = lobby_type

    @property
    def hero_id(self):
        """
        Gets the hero_id of this InlineResponse2003.
        hero_id

        :return: The hero_id of this InlineResponse2003.
        :rtype: float
        """
        return self._hero_id

    @hero_id.setter
    def hero_id(self, hero_id):
        """
        Sets the hero_id of this InlineResponse2003.
        hero_id

        :param hero_id: The hero_id of this InlineResponse2003.
        :type: float
        """

        self._hero_id = hero_id

    @property
    def start_time(self):
        """
        Gets the start_time of this InlineResponse2003.
        start_time

        :return: The start_time of this InlineResponse2003.
        :rtype: float
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this InlineResponse2003.
        start_time

        :param start_time: The start_time of this InlineResponse2003.
        :type: float
        """

        self._start_time = start_time

    @property
    def version(self):
        """
        Gets the version of this InlineResponse2003.
        version

        :return: The version of this InlineResponse2003.
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this InlineResponse2003.
        version

        :param version: The version of this InlineResponse2003.
        :type: float
        """

        self._version = version

    @property
    def kills(self):
        """
        Gets the kills of this InlineResponse2003.
        kills

        :return: The kills of this InlineResponse2003.
        :rtype: float
        """
        return self._kills

    @kills.setter
    def kills(self, kills):
        """
        Sets the kills of this InlineResponse2003.
        kills

        :param kills: The kills of this InlineResponse2003.
        :type: float
        """

        self._kills = kills

    @property
    def deaths(self):
        """
        Gets the deaths of this InlineResponse2003.
        deaths

        :return: The deaths of this InlineResponse2003.
        :rtype: float
        """
        return self._deaths

    @deaths.setter
    def deaths(self, deaths):
        """
        Sets the deaths of this InlineResponse2003.
        deaths

        :param deaths: The deaths of this InlineResponse2003.
        :type: float
        """

        self._deaths = deaths

    @property
    def assists(self):
        """
        Gets the assists of this InlineResponse2003.
        assists

        :return: The assists of this InlineResponse2003.
        :rtype: float
        """
        return self._assists

    @assists.setter
    def assists(self, assists):
        """
        Sets the assists of this InlineResponse2003.
        assists

        :param assists: The assists of this InlineResponse2003.
        :type: float
        """

        self._assists = assists

    @property
    def skill(self):
        """
        Gets the skill of this InlineResponse2003.
        skill

        :return: The skill of this InlineResponse2003.
        :rtype: float
        """
        return self._skill

    @skill.setter
    def skill(self, skill):
        """
        Sets the skill of this InlineResponse2003.
        skill

        :param skill: The skill of this InlineResponse2003.
        :type: float
        """

        self._skill = skill

    @property
    def lane(self):
        """
        Gets the lane of this InlineResponse2003.
        lane

        :return: The lane of this InlineResponse2003.
        :rtype: float
        """
        return self._lane

    @lane.setter
    def lane(self, lane):
        """
        Sets the lane of this InlineResponse2003.
        lane

        :param lane: The lane of this InlineResponse2003.
        :type: float
        """

        self._lane = lane

    @property
    def lane_role(self):
        """
        Gets the lane_role of this InlineResponse2003.
        lane_role

        :return: The lane_role of this InlineResponse2003.
        :rtype: float
        """
        return self._lane_role

    @lane_role.setter
    def lane_role(self, lane_role):
        """
        Sets the lane_role of this InlineResponse2003.
        lane_role

        :param lane_role: The lane_role of this InlineResponse2003.
        :type: float
        """

        self._lane_role = lane_role

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
        if not isinstance(other, InlineResponse2003):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
