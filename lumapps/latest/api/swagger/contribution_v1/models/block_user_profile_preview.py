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


class BlockUserProfilePreview(BaseBlock):
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
    swagger_types = {
        "user_id": "str",
        "full_name": "str",
        "picture_url": "str",
        "fields": "list[UserProfileField]",
    }
    if hasattr(BaseBlock, "swagger_types"):
        swagger_types.update(BaseBlock.swagger_types)

    attribute_map = {
        "user_id": "userId",
        "full_name": "fullName",
        "picture_url": "pictureUrl",
        "fields": "fields",
    }
    if hasattr(BaseBlock, "attribute_map"):
        attribute_map.update(BaseBlock.attribute_map)

    def __init__(
        self,
        user_id=None,
        full_name=None,
        picture_url=None,
        fields=None,
        *args,
        **kwargs
    ):  # noqa: E501
        """BlockUserProfilePreview - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._full_name = None
        self._picture_url = None
        self._fields = None
        self.discriminator = None
        self.user_id = user_id
        self.full_name = full_name
        self.picture_url = picture_url
        self.fields = fields
        BaseBlock.__init__(self, *args, **kwargs)

    @property
    def user_id(self):
        """Gets the user_id of this BlockUserProfilePreview.  # noqa: E501

        The user's id.  # noqa: E501

        :return: The user_id of this BlockUserProfilePreview.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this BlockUserProfilePreview.

        The user's id.  # noqa: E501

        :param user_id: The user_id of this BlockUserProfilePreview.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError(
                "Invalid value for `user_id`, must not be `None`"
            )  # noqa: E501

        self._user_id = user_id

    @property
    def full_name(self):
        """Gets the full_name of this BlockUserProfilePreview.  # noqa: E501

        The user's full name.  # noqa: E501

        :return: The full_name of this BlockUserProfilePreview.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this BlockUserProfilePreview.

        The user's full name.  # noqa: E501

        :param full_name: The full_name of this BlockUserProfilePreview.  # noqa: E501
        :type: str
        """
        if full_name is None:
            raise ValueError(
                "Invalid value for `full_name`, must not be `None`"
            )  # noqa: E501

        self._full_name = full_name

    @property
    def picture_url(self):
        """Gets the picture_url of this BlockUserProfilePreview.  # noqa: E501

        The url to the user's profile picture.  # noqa: E501

        :return: The picture_url of this BlockUserProfilePreview.  # noqa: E501
        :rtype: str
        """
        return self._picture_url

    @picture_url.setter
    def picture_url(self, picture_url):
        """Sets the picture_url of this BlockUserProfilePreview.

        The url to the user's profile picture.  # noqa: E501

        :param picture_url: The picture_url of this BlockUserProfilePreview.  # noqa: E501
        :type: str
        """
        if picture_url is None:
            raise ValueError(
                "Invalid value for `picture_url`, must not be `None`"
            )  # noqa: E501

        self._picture_url = picture_url

    @property
    def fields(self):
        """Gets the fields of this BlockUserProfilePreview.  # noqa: E501

        a ordered field list from the user's profile  # noqa: E501

        :return: The fields of this BlockUserProfilePreview.  # noqa: E501
        :rtype: list[UserProfileField]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this BlockUserProfilePreview.

        a ordered field list from the user's profile  # noqa: E501

        :param fields: The fields of this BlockUserProfilePreview.  # noqa: E501
        :type: list[UserProfileField]
        """
        if fields is None:
            raise ValueError(
                "Invalid value for `fields`, must not be `None`"
            )  # noqa: E501

        self._fields = fields

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
        if issubclass(BlockUserProfilePreview, dict):
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
        if not isinstance(other, BlockUserProfilePreview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
