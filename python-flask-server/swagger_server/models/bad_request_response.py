# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class BadRequestResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, status: str=None, detail: str=None):  # noqa: E501
        """BadRequestResponse - a model defined in Swagger

        :param code: The code of this BadRequestResponse.  # noqa: E501
        :type code: str
        :param status: The status of this BadRequestResponse.  # noqa: E501
        :type status: str
        :param detail: The detail of this BadRequestResponse.  # noqa: E501
        :type detail: str
        """
        self.swagger_types = {
            'code': str,
            'status': str,
            'detail': str
        }

        self.attribute_map = {
            'code': 'code',
            'status': 'status',
            'detail': 'detail'
        }

        self._code = code
        self._status = status
        self._detail = detail

    @classmethod
    def from_dict(cls, dikt) -> 'BadRequestResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BadRequestResponse of this BadRequestResponse.  # noqa: E501
        :rtype: BadRequestResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> str:
        """Gets the code of this BadRequestResponse.


        :return: The code of this BadRequestResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this BadRequestResponse.


        :param code: The code of this BadRequestResponse.
        :type code: str
        """

        self._code = code

    @property
    def status(self) -> str:
        """Gets the status of this BadRequestResponse.


        :return: The status of this BadRequestResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this BadRequestResponse.


        :param status: The status of this BadRequestResponse.
        :type status: str
        """

        self._status = status

    @property
    def detail(self) -> str:
        """Gets the detail of this BadRequestResponse.


        :return: The detail of this BadRequestResponse.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail: str):
        """Sets the detail of this BadRequestResponse.


        :param detail: The detail of this BadRequestResponse.
        :type detail: str
        """

        self._detail = detail
