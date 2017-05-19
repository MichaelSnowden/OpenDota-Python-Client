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


class InlineResponse20018MmrRows(object):
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
        'bin': 'float',
        'bin_name': 'float',
        'count': 'float',
        'cumulative_sum': 'float'
    }

    attribute_map = {
        'bin': 'bin',
        'bin_name': 'bin_name',
        'count': 'count',
        'cumulative_sum': 'cumulative_sum'
    }

    def __init__(self, bin=None, bin_name=None, count=None, cumulative_sum=None):
        """
        InlineResponse20018MmrRows - a model defined in Swagger
        """

        self._bin = None
        self._bin_name = None
        self._count = None
        self._cumulative_sum = None

        if bin is not None:
          self.bin = bin
        if bin_name is not None:
          self.bin_name = bin_name
        if count is not None:
          self.count = count
        if cumulative_sum is not None:
          self.cumulative_sum = cumulative_sum

    @property
    def bin(self):
        """
        Gets the bin of this InlineResponse20018MmrRows.
        bin

        :return: The bin of this InlineResponse20018MmrRows.
        :rtype: float
        """
        return self._bin

    @bin.setter
    def bin(self, bin):
        """
        Sets the bin of this InlineResponse20018MmrRows.
        bin

        :param bin: The bin of this InlineResponse20018MmrRows.
        :type: float
        """

        self._bin = bin

    @property
    def bin_name(self):
        """
        Gets the bin_name of this InlineResponse20018MmrRows.
        bin_name

        :return: The bin_name of this InlineResponse20018MmrRows.
        :rtype: float
        """
        return self._bin_name

    @bin_name.setter
    def bin_name(self, bin_name):
        """
        Sets the bin_name of this InlineResponse20018MmrRows.
        bin_name

        :param bin_name: The bin_name of this InlineResponse20018MmrRows.
        :type: float
        """

        self._bin_name = bin_name

    @property
    def count(self):
        """
        Gets the count of this InlineResponse20018MmrRows.
        count

        :return: The count of this InlineResponse20018MmrRows.
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this InlineResponse20018MmrRows.
        count

        :param count: The count of this InlineResponse20018MmrRows.
        :type: float
        """

        self._count = count

    @property
    def cumulative_sum(self):
        """
        Gets the cumulative_sum of this InlineResponse20018MmrRows.
        cumulative_sum

        :return: The cumulative_sum of this InlineResponse20018MmrRows.
        :rtype: float
        """
        return self._cumulative_sum

    @cumulative_sum.setter
    def cumulative_sum(self, cumulative_sum):
        """
        Sets the cumulative_sum of this InlineResponse20018MmrRows.
        cumulative_sum

        :param cumulative_sum: The cumulative_sum of this InlineResponse20018MmrRows.
        :type: float
        """

        self._cumulative_sum = cumulative_sum

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
        if not isinstance(other, InlineResponse20018MmrRows):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
