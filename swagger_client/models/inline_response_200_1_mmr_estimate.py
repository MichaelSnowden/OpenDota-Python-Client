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


class InlineResponse2001MmrEstimate(object):
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
        'estimate': 'float',
        'std_dev': 'float',
        'n': 'float'
    }

    attribute_map = {
        'estimate': 'estimate',
        'std_dev': 'stdDev',
        'n': 'n'
    }

    def __init__(self, estimate=None, std_dev=None, n=None):
        """
        InlineResponse2001MmrEstimate - a model defined in Swagger
        """

        self._estimate = None
        self._std_dev = None
        self._n = None

        if estimate is not None:
          self.estimate = estimate
        if std_dev is not None:
          self.std_dev = std_dev
        if n is not None:
          self.n = n

    @property
    def estimate(self):
        """
        Gets the estimate of this InlineResponse2001MmrEstimate.
        estimate

        :return: The estimate of this InlineResponse2001MmrEstimate.
        :rtype: float
        """
        return self._estimate

    @estimate.setter
    def estimate(self, estimate):
        """
        Sets the estimate of this InlineResponse2001MmrEstimate.
        estimate

        :param estimate: The estimate of this InlineResponse2001MmrEstimate.
        :type: float
        """

        self._estimate = estimate

    @property
    def std_dev(self):
        """
        Gets the std_dev of this InlineResponse2001MmrEstimate.
        stdDev

        :return: The std_dev of this InlineResponse2001MmrEstimate.
        :rtype: float
        """
        return self._std_dev

    @std_dev.setter
    def std_dev(self, std_dev):
        """
        Sets the std_dev of this InlineResponse2001MmrEstimate.
        stdDev

        :param std_dev: The std_dev of this InlineResponse2001MmrEstimate.
        :type: float
        """

        self._std_dev = std_dev

    @property
    def n(self):
        """
        Gets the n of this InlineResponse2001MmrEstimate.
        n

        :return: The n of this InlineResponse2001MmrEstimate.
        :rtype: float
        """
        return self._n

    @n.setter
    def n(self, n):
        """
        Sets the n of this InlineResponse2001MmrEstimate.
        n

        :param n: The n of this InlineResponse2001MmrEstimate.
        :type: float
        """

        self._n = n

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
        if not isinstance(other, InlineResponse2001MmrEstimate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
