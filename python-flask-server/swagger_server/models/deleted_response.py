# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class DeletedResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code: int=None, status: str=None):  # noqa: E501
        """DeletedResponse - a model defined in Swagger

        :param code: The code of this DeletedResponse.  # noqa: E501
        :type code: int
        :param status: The status of this DeletedResponse.  # noqa: E501
        :type status: str
        """
        self.swagger_types = {
            'code': int,
            'status': str
        }

        self.attribute_map = {
            'code': 'code',
            'status': 'status'
        }

        self._code = code
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'DeletedResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DeletedResponse of this DeletedResponse.  # noqa: E501
        :rtype: DeletedResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> int:
        """Gets the code of this DeletedResponse.


        :return: The code of this DeletedResponse.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """Sets the code of this DeletedResponse.


        :param code: The code of this DeletedResponse.
        :type code: int
        """

        self._code = code

    @property
    def status(self) -> str:
        """Gets the status of this DeletedResponse.


        :return: The status of this DeletedResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this DeletedResponse.


        :param status: The status of this DeletedResponse.
        :type status: str
        """

        self._status = status
