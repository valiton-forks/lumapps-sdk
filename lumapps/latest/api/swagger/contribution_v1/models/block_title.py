# coding: utf-8

"""
    CMS Contribution API

    The CMS Contribution API allows access and modification of Lumapps contents.   # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

from .base_block import BaseBlock  # noqa: F401,E501


class BlockTitle(BaseBlock):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {"text": "str", "typography": "str"}
    if hasattr(BaseBlock, "swagger_types"):
        swagger_types.update(BaseBlock.swagger_types)

    attribute_map = {"text": "text", "typography": "typography"}
    if hasattr(BaseBlock, "attribute_map"):
        attribute_map.update(BaseBlock.attribute_map)

    def __init__(self, text=None, typography=None, *args, **kwargs):  # noqa: E501
        """BlockTitle - a model defined in Swagger"""  # noqa: E501
        self._text = None
        self._typography = None
        self.discriminator = None
        self.text = text
        self.typography = typography
        BaseBlock.__init__(self, *args, **kwargs)

    @property
    def text(self):
        """Gets the text of this BlockTitle.  # noqa: E501

        The title.  # noqa: E501

        :return: The text of this BlockTitle.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this BlockTitle.

        The title.  # noqa: E501

        :param text: The text of this BlockTitle.  # noqa: E501
        :type: str
        """
        if text is None:
            raise ValueError(
                "Invalid value for `text`, must not be `None`"
            )  # noqa: E501

        self._text = text

    @property
    def typography(self):
        """Gets the typography of this BlockTitle.  # noqa: E501

        The typography to use (default: headline).  # noqa: E501

        :return: The typography of this BlockTitle.  # noqa: E501
        :rtype: str
        """
        return self._typography

    @typography.setter
    def typography(self, typography):
        """Sets the typography of this BlockTitle.

        The typography to use (default: headline).  # noqa: E501

        :param typography: The typography of this BlockTitle.  # noqa: E501
        :type: str
        """
        if typography is None:
            raise ValueError(
                "Invalid value for `typography`, must not be `None`"
            )  # noqa: E501
        allowed_values = [
            "headline",
            "title",
            "subtitle1",
            "subtitle2",
            "body1",
            "body2",
            "caption",
            "overline",
            "display1",
        ]  # noqa: E501
        if typography not in allowed_values:
            raise ValueError(
                "Invalid value for `typography` ({0}), must be one of {1}".format(  # noqa: E501
                    typography, allowed_values
                )
            )

        self._typography = typography

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(BlockTitle, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BlockTitle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
