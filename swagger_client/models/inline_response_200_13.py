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


class InlineResponse20013(object):
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
        'steamid': 'str',
        'avatar': 'str',
        'avatarmedium': 'str',
        'avatarfull': 'str',
        'profileurl': 'str',
        'personaname': 'str',
        'cheese': 'float',
        'fh_unavailable': 'bool',
        'loccountrycode': 'str',
        'name': 'str',
        'country_code': 'str',
        'fantasy_role': 'float',
        'team_id': 'float',
        'team_name': 'str',
        'team_tag': 'str',
        'is_locked': 'bool',
        'is_pro': 'bool',
        'locked_until': 'float'
    }

    attribute_map = {
        'account_id': 'account_id',
        'steamid': 'steamid',
        'avatar': 'avatar',
        'avatarmedium': 'avatarmedium',
        'avatarfull': 'avatarfull',
        'profileurl': 'profileurl',
        'personaname': 'personaname',
        'cheese': 'cheese',
        'fh_unavailable': 'fh_unavailable',
        'loccountrycode': 'loccountrycode',
        'name': 'name',
        'country_code': 'country_code',
        'fantasy_role': 'fantasy_role',
        'team_id': 'team_id',
        'team_name': 'team_name',
        'team_tag': 'team_tag',
        'is_locked': 'is_locked',
        'is_pro': 'is_pro',
        'locked_until': 'locked_until'
    }

    def __init__(self, account_id=None, steamid=None, avatar=None, avatarmedium=None, avatarfull=None, profileurl=None, personaname=None, cheese=None, fh_unavailable=None, loccountrycode=None, name=None, country_code=None, fantasy_role=None, team_id=None, team_name=None, team_tag=None, is_locked=None, is_pro=None, locked_until=None):
        """
        InlineResponse20013 - a model defined in Swagger
        """

        self._account_id = None
        self._steamid = None
        self._avatar = None
        self._avatarmedium = None
        self._avatarfull = None
        self._profileurl = None
        self._personaname = None
        self._cheese = None
        self._fh_unavailable = None
        self._loccountrycode = None
        self._name = None
        self._country_code = None
        self._fantasy_role = None
        self._team_id = None
        self._team_name = None
        self._team_tag = None
        self._is_locked = None
        self._is_pro = None
        self._locked_until = None

        if account_id is not None:
          self.account_id = account_id
        if steamid is not None:
          self.steamid = steamid
        if avatar is not None:
          self.avatar = avatar
        if avatarmedium is not None:
          self.avatarmedium = avatarmedium
        if avatarfull is not None:
          self.avatarfull = avatarfull
        if profileurl is not None:
          self.profileurl = profileurl
        if personaname is not None:
          self.personaname = personaname
        if cheese is not None:
          self.cheese = cheese
        if fh_unavailable is not None:
          self.fh_unavailable = fh_unavailable
        if loccountrycode is not None:
          self.loccountrycode = loccountrycode
        if name is not None:
          self.name = name
        if country_code is not None:
          self.country_code = country_code
        if fantasy_role is not None:
          self.fantasy_role = fantasy_role
        if team_id is not None:
          self.team_id = team_id
        if team_name is not None:
          self.team_name = team_name
        if team_tag is not None:
          self.team_tag = team_tag
        if is_locked is not None:
          self.is_locked = is_locked
        if is_pro is not None:
          self.is_pro = is_pro
        if locked_until is not None:
          self.locked_until = locked_until

    @property
    def account_id(self):
        """
        Gets the account_id of this InlineResponse20013.
        account_id

        :return: The account_id of this InlineResponse20013.
        :rtype: float
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this InlineResponse20013.
        account_id

        :param account_id: The account_id of this InlineResponse20013.
        :type: float
        """

        self._account_id = account_id

    @property
    def steamid(self):
        """
        Gets the steamid of this InlineResponse20013.
        steamid

        :return: The steamid of this InlineResponse20013.
        :rtype: str
        """
        return self._steamid

    @steamid.setter
    def steamid(self, steamid):
        """
        Sets the steamid of this InlineResponse20013.
        steamid

        :param steamid: The steamid of this InlineResponse20013.
        :type: str
        """

        self._steamid = steamid

    @property
    def avatar(self):
        """
        Gets the avatar of this InlineResponse20013.
        avatar

        :return: The avatar of this InlineResponse20013.
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """
        Sets the avatar of this InlineResponse20013.
        avatar

        :param avatar: The avatar of this InlineResponse20013.
        :type: str
        """

        self._avatar = avatar

    @property
    def avatarmedium(self):
        """
        Gets the avatarmedium of this InlineResponse20013.
        avatarmedium

        :return: The avatarmedium of this InlineResponse20013.
        :rtype: str
        """
        return self._avatarmedium

    @avatarmedium.setter
    def avatarmedium(self, avatarmedium):
        """
        Sets the avatarmedium of this InlineResponse20013.
        avatarmedium

        :param avatarmedium: The avatarmedium of this InlineResponse20013.
        :type: str
        """

        self._avatarmedium = avatarmedium

    @property
    def avatarfull(self):
        """
        Gets the avatarfull of this InlineResponse20013.
        avatarfull

        :return: The avatarfull of this InlineResponse20013.
        :rtype: str
        """
        return self._avatarfull

    @avatarfull.setter
    def avatarfull(self, avatarfull):
        """
        Sets the avatarfull of this InlineResponse20013.
        avatarfull

        :param avatarfull: The avatarfull of this InlineResponse20013.
        :type: str
        """

        self._avatarfull = avatarfull

    @property
    def profileurl(self):
        """
        Gets the profileurl of this InlineResponse20013.
        profileurl

        :return: The profileurl of this InlineResponse20013.
        :rtype: str
        """
        return self._profileurl

    @profileurl.setter
    def profileurl(self, profileurl):
        """
        Sets the profileurl of this InlineResponse20013.
        profileurl

        :param profileurl: The profileurl of this InlineResponse20013.
        :type: str
        """

        self._profileurl = profileurl

    @property
    def personaname(self):
        """
        Gets the personaname of this InlineResponse20013.
        personaname

        :return: The personaname of this InlineResponse20013.
        :rtype: str
        """
        return self._personaname

    @personaname.setter
    def personaname(self, personaname):
        """
        Sets the personaname of this InlineResponse20013.
        personaname

        :param personaname: The personaname of this InlineResponse20013.
        :type: str
        """

        self._personaname = personaname

    @property
    def cheese(self):
        """
        Gets the cheese of this InlineResponse20013.
        cheese

        :return: The cheese of this InlineResponse20013.
        :rtype: float
        """
        return self._cheese

    @cheese.setter
    def cheese(self, cheese):
        """
        Sets the cheese of this InlineResponse20013.
        cheese

        :param cheese: The cheese of this InlineResponse20013.
        :type: float
        """

        self._cheese = cheese

    @property
    def fh_unavailable(self):
        """
        Gets the fh_unavailable of this InlineResponse20013.
        fh_unavailable

        :return: The fh_unavailable of this InlineResponse20013.
        :rtype: bool
        """
        return self._fh_unavailable

    @fh_unavailable.setter
    def fh_unavailable(self, fh_unavailable):
        """
        Sets the fh_unavailable of this InlineResponse20013.
        fh_unavailable

        :param fh_unavailable: The fh_unavailable of this InlineResponse20013.
        :type: bool
        """

        self._fh_unavailable = fh_unavailable

    @property
    def loccountrycode(self):
        """
        Gets the loccountrycode of this InlineResponse20013.
        loccountrycode

        :return: The loccountrycode of this InlineResponse20013.
        :rtype: str
        """
        return self._loccountrycode

    @loccountrycode.setter
    def loccountrycode(self, loccountrycode):
        """
        Sets the loccountrycode of this InlineResponse20013.
        loccountrycode

        :param loccountrycode: The loccountrycode of this InlineResponse20013.
        :type: str
        """

        self._loccountrycode = loccountrycode

    @property
    def name(self):
        """
        Gets the name of this InlineResponse20013.
        name

        :return: The name of this InlineResponse20013.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InlineResponse20013.
        name

        :param name: The name of this InlineResponse20013.
        :type: str
        """

        self._name = name

    @property
    def country_code(self):
        """
        Gets the country_code of this InlineResponse20013.
        country_code

        :return: The country_code of this InlineResponse20013.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """
        Sets the country_code of this InlineResponse20013.
        country_code

        :param country_code: The country_code of this InlineResponse20013.
        :type: str
        """

        self._country_code = country_code

    @property
    def fantasy_role(self):
        """
        Gets the fantasy_role of this InlineResponse20013.
        fantasy_role

        :return: The fantasy_role of this InlineResponse20013.
        :rtype: float
        """
        return self._fantasy_role

    @fantasy_role.setter
    def fantasy_role(self, fantasy_role):
        """
        Sets the fantasy_role of this InlineResponse20013.
        fantasy_role

        :param fantasy_role: The fantasy_role of this InlineResponse20013.
        :type: float
        """

        self._fantasy_role = fantasy_role

    @property
    def team_id(self):
        """
        Gets the team_id of this InlineResponse20013.
        team_id

        :return: The team_id of this InlineResponse20013.
        :rtype: float
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """
        Sets the team_id of this InlineResponse20013.
        team_id

        :param team_id: The team_id of this InlineResponse20013.
        :type: float
        """

        self._team_id = team_id

    @property
    def team_name(self):
        """
        Gets the team_name of this InlineResponse20013.
        team_name

        :return: The team_name of this InlineResponse20013.
        :rtype: str
        """
        return self._team_name

    @team_name.setter
    def team_name(self, team_name):
        """
        Sets the team_name of this InlineResponse20013.
        team_name

        :param team_name: The team_name of this InlineResponse20013.
        :type: str
        """

        self._team_name = team_name

    @property
    def team_tag(self):
        """
        Gets the team_tag of this InlineResponse20013.
        team_tag

        :return: The team_tag of this InlineResponse20013.
        :rtype: str
        """
        return self._team_tag

    @team_tag.setter
    def team_tag(self, team_tag):
        """
        Sets the team_tag of this InlineResponse20013.
        team_tag

        :param team_tag: The team_tag of this InlineResponse20013.
        :type: str
        """

        self._team_tag = team_tag

    @property
    def is_locked(self):
        """
        Gets the is_locked of this InlineResponse20013.
        is_locked

        :return: The is_locked of this InlineResponse20013.
        :rtype: bool
        """
        return self._is_locked

    @is_locked.setter
    def is_locked(self, is_locked):
        """
        Sets the is_locked of this InlineResponse20013.
        is_locked

        :param is_locked: The is_locked of this InlineResponse20013.
        :type: bool
        """

        self._is_locked = is_locked

    @property
    def is_pro(self):
        """
        Gets the is_pro of this InlineResponse20013.
        is_pro

        :return: The is_pro of this InlineResponse20013.
        :rtype: bool
        """
        return self._is_pro

    @is_pro.setter
    def is_pro(self, is_pro):
        """
        Sets the is_pro of this InlineResponse20013.
        is_pro

        :param is_pro: The is_pro of this InlineResponse20013.
        :type: bool
        """

        self._is_pro = is_pro

    @property
    def locked_until(self):
        """
        Gets the locked_until of this InlineResponse20013.
        locked_until

        :return: The locked_until of this InlineResponse20013.
        :rtype: float
        """
        return self._locked_until

    @locked_until.setter
    def locked_until(self, locked_until):
        """
        Sets the locked_until of this InlineResponse20013.
        locked_until

        :param locked_until: The locked_until of this InlineResponse20013.
        :type: float
        """

        self._locked_until = locked_until

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
        if not isinstance(other, InlineResponse20013):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
