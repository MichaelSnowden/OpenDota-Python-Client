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


class InlineResponse2006(object):
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
        'last_played': 'float',
        'win': 'float',
        'games': 'float',
        'with_win': 'float',
        'with_games': 'float',
        'against_win': 'float',
        'against_games': 'float',
        'with_gpm_sum': 'float',
        'with_xpm_sum': 'float',
        'personaname': 'str',
        'last_login': 'str',
        'avatar': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'last_played': 'last_played',
        'win': 'win',
        'games': 'games',
        'with_win': 'with_win',
        'with_games': 'with_games',
        'against_win': 'against_win',
        'against_games': 'against_games',
        'with_gpm_sum': 'with_gpm_sum',
        'with_xpm_sum': 'with_xpm_sum',
        'personaname': 'personaname',
        'last_login': 'last_login',
        'avatar': 'avatar'
    }

    def __init__(self, account_id=None, last_played=None, win=None, games=None, with_win=None, with_games=None, against_win=None, against_games=None, with_gpm_sum=None, with_xpm_sum=None, personaname=None, last_login=None, avatar=None):
        """
        InlineResponse2006 - a model defined in Swagger
        """

        self._account_id = None
        self._last_played = None
        self._win = None
        self._games = None
        self._with_win = None
        self._with_games = None
        self._against_win = None
        self._against_games = None
        self._with_gpm_sum = None
        self._with_xpm_sum = None
        self._personaname = None
        self._last_login = None
        self._avatar = None

        if account_id is not None:
          self.account_id = account_id
        if last_played is not None:
          self.last_played = last_played
        if win is not None:
          self.win = win
        if games is not None:
          self.games = games
        if with_win is not None:
          self.with_win = with_win
        if with_games is not None:
          self.with_games = with_games
        if against_win is not None:
          self.against_win = against_win
        if against_games is not None:
          self.against_games = against_games
        if with_gpm_sum is not None:
          self.with_gpm_sum = with_gpm_sum
        if with_xpm_sum is not None:
          self.with_xpm_sum = with_xpm_sum
        if personaname is not None:
          self.personaname = personaname
        if last_login is not None:
          self.last_login = last_login
        if avatar is not None:
          self.avatar = avatar

    @property
    def account_id(self):
        """
        Gets the account_id of this InlineResponse2006.
        account_id

        :return: The account_id of this InlineResponse2006.
        :rtype: float
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this InlineResponse2006.
        account_id

        :param account_id: The account_id of this InlineResponse2006.
        :type: float
        """

        self._account_id = account_id

    @property
    def last_played(self):
        """
        Gets the last_played of this InlineResponse2006.
        last_played

        :return: The last_played of this InlineResponse2006.
        :rtype: float
        """
        return self._last_played

    @last_played.setter
    def last_played(self, last_played):
        """
        Sets the last_played of this InlineResponse2006.
        last_played

        :param last_played: The last_played of this InlineResponse2006.
        :type: float
        """

        self._last_played = last_played

    @property
    def win(self):
        """
        Gets the win of this InlineResponse2006.
        win

        :return: The win of this InlineResponse2006.
        :rtype: float
        """
        return self._win

    @win.setter
    def win(self, win):
        """
        Sets the win of this InlineResponse2006.
        win

        :param win: The win of this InlineResponse2006.
        :type: float
        """

        self._win = win

    @property
    def games(self):
        """
        Gets the games of this InlineResponse2006.
        games

        :return: The games of this InlineResponse2006.
        :rtype: float
        """
        return self._games

    @games.setter
    def games(self, games):
        """
        Sets the games of this InlineResponse2006.
        games

        :param games: The games of this InlineResponse2006.
        :type: float
        """

        self._games = games

    @property
    def with_win(self):
        """
        Gets the with_win of this InlineResponse2006.
        with_win

        :return: The with_win of this InlineResponse2006.
        :rtype: float
        """
        return self._with_win

    @with_win.setter
    def with_win(self, with_win):
        """
        Sets the with_win of this InlineResponse2006.
        with_win

        :param with_win: The with_win of this InlineResponse2006.
        :type: float
        """

        self._with_win = with_win

    @property
    def with_games(self):
        """
        Gets the with_games of this InlineResponse2006.
        with_games

        :return: The with_games of this InlineResponse2006.
        :rtype: float
        """
        return self._with_games

    @with_games.setter
    def with_games(self, with_games):
        """
        Sets the with_games of this InlineResponse2006.
        with_games

        :param with_games: The with_games of this InlineResponse2006.
        :type: float
        """

        self._with_games = with_games

    @property
    def against_win(self):
        """
        Gets the against_win of this InlineResponse2006.
        against_win

        :return: The against_win of this InlineResponse2006.
        :rtype: float
        """
        return self._against_win

    @against_win.setter
    def against_win(self, against_win):
        """
        Sets the against_win of this InlineResponse2006.
        against_win

        :param against_win: The against_win of this InlineResponse2006.
        :type: float
        """

        self._against_win = against_win

    @property
    def against_games(self):
        """
        Gets the against_games of this InlineResponse2006.
        against_games

        :return: The against_games of this InlineResponse2006.
        :rtype: float
        """
        return self._against_games

    @against_games.setter
    def against_games(self, against_games):
        """
        Sets the against_games of this InlineResponse2006.
        against_games

        :param against_games: The against_games of this InlineResponse2006.
        :type: float
        """

        self._against_games = against_games

    @property
    def with_gpm_sum(self):
        """
        Gets the with_gpm_sum of this InlineResponse2006.
        with_gpm_sum

        :return: The with_gpm_sum of this InlineResponse2006.
        :rtype: float
        """
        return self._with_gpm_sum

    @with_gpm_sum.setter
    def with_gpm_sum(self, with_gpm_sum):
        """
        Sets the with_gpm_sum of this InlineResponse2006.
        with_gpm_sum

        :param with_gpm_sum: The with_gpm_sum of this InlineResponse2006.
        :type: float
        """

        self._with_gpm_sum = with_gpm_sum

    @property
    def with_xpm_sum(self):
        """
        Gets the with_xpm_sum of this InlineResponse2006.
        with_xpm_sum

        :return: The with_xpm_sum of this InlineResponse2006.
        :rtype: float
        """
        return self._with_xpm_sum

    @with_xpm_sum.setter
    def with_xpm_sum(self, with_xpm_sum):
        """
        Sets the with_xpm_sum of this InlineResponse2006.
        with_xpm_sum

        :param with_xpm_sum: The with_xpm_sum of this InlineResponse2006.
        :type: float
        """

        self._with_xpm_sum = with_xpm_sum

    @property
    def personaname(self):
        """
        Gets the personaname of this InlineResponse2006.
        personaname

        :return: The personaname of this InlineResponse2006.
        :rtype: str
        """
        return self._personaname

    @personaname.setter
    def personaname(self, personaname):
        """
        Sets the personaname of this InlineResponse2006.
        personaname

        :param personaname: The personaname of this InlineResponse2006.
        :type: str
        """

        self._personaname = personaname

    @property
    def last_login(self):
        """
        Gets the last_login of this InlineResponse2006.
        last_login

        :return: The last_login of this InlineResponse2006.
        :rtype: str
        """
        return self._last_login

    @last_login.setter
    def last_login(self, last_login):
        """
        Sets the last_login of this InlineResponse2006.
        last_login

        :param last_login: The last_login of this InlineResponse2006.
        :type: str
        """

        self._last_login = last_login

    @property
    def avatar(self):
        """
        Gets the avatar of this InlineResponse2006.
        avatar

        :return: The avatar of this InlineResponse2006.
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """
        Sets the avatar of this InlineResponse2006.
        avatar

        :param avatar: The avatar of this InlineResponse2006.
        :type: str
        """

        self._avatar = avatar

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
        if not isinstance(other, InlineResponse2006):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other