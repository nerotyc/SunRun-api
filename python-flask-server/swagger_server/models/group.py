# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Group(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, creator_id: int=None, name: str=None, description: str='null', score: float=0.0, run_count: int=0, num_participants: int=0, sum_duration: int=0, sum_distance_walk: float=0.0, sum_distance_run: float=0.0, sum_distance_bike: float=0.0, sum_distance_ebike: float=0.0):  # noqa: E501
        """Group - a model defined in Swagger

        :param id: The id of this Group.  # noqa: E501
        :type id: int
        :param creator_id: The creator_id of this Group.  # noqa: E501
        :type creator_id: int
        :param name: The name of this Group.  # noqa: E501
        :type name: str
        :param description: The description of this Group.  # noqa: E501
        :type description: str
        :param score: The score of this Group.  # noqa: E501
        :type score: float
        :param run_count: The run_count of this Group.  # noqa: E501
        :type run_count: int
        :param num_participants: The num_participants of this Group.  # noqa: E501
        :type num_participants: int
        :param sum_duration: The sum_duration of this Group.  # noqa: E501
        :type sum_duration: int
        :param sum_distance_walk: The sum_distance_walk of this Group.  # noqa: E501
        :type sum_distance_walk: float
        :param sum_distance_run: The sum_distance_run of this Group.  # noqa: E501
        :type sum_distance_run: float
        :param sum_distance_bike: The sum_distance_bike of this Group.  # noqa: E501
        :type sum_distance_bike: float
        :param sum_distance_ebike: The sum_distance_ebike of this Group.  # noqa: E501
        :type sum_distance_ebike: float
        """
        self.swagger_types = {
            'id': int,
            'creator_id': int,
            'name': str,
            'description': str,
            'score': float,
            'run_count': int,
            'num_participants': int,
            'sum_duration': int,
            'sum_distance_walk': float,
            'sum_distance_run': float,
            'sum_distance_bike': float,
            'sum_distance_ebike': float
        }

        self.attribute_map = {
            'id': 'id',
            'creator_id': 'creator_id',
            'name': 'name',
            'description': 'description',
            'score': 'score',
            'run_count': 'run_count',
            'num_participants': 'num_participants',
            'sum_duration': 'sum_duration',
            'sum_distance_walk': 'sum_distance_walk',
            'sum_distance_run': 'sum_distance_run',
            'sum_distance_bike': 'sum_distance_bike',
            'sum_distance_ebike': 'sum_distance_ebike'
        }

        self._id = id
        self._creator_id = creator_id
        self._name = name
        self._description = description
        self._score = score
        self._run_count = run_count
        self._num_participants = num_participants
        self._sum_duration = sum_duration
        self._sum_distance_walk = sum_distance_walk
        self._sum_distance_run = sum_distance_run
        self._sum_distance_bike = sum_distance_bike
        self._sum_distance_ebike = sum_distance_ebike

    @classmethod
    def from_dict(cls, dikt) -> 'Group':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Group of this Group.  # noqa: E501
        :rtype: Group
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Group.


        :return: The id of this Group.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Group.


        :param id: The id of this Group.
        :type id: int
        """

        self._id = id

    @property
    def creator_id(self) -> int:
        """Gets the creator_id of this Group.


        :return: The creator_id of this Group.
        :rtype: int
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id: int):
        """Sets the creator_id of this Group.


        :param creator_id: The creator_id of this Group.
        :type creator_id: int
        """

        self._creator_id = creator_id

    @property
    def name(self) -> str:
        """Gets the name of this Group.


        :return: The name of this Group.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Group.


        :param name: The name of this Group.
        :type name: str
        """

        self._name = name

    @property
    def description(self) -> str:
        """Gets the description of this Group.

        if null: fields istn't part of json object  # noqa: E501

        :return: The description of this Group.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Group.

        if null: fields istn't part of json object  # noqa: E501

        :param description: The description of this Group.
        :type description: str
        """

        self._description = description

    @property
    def score(self) -> float:
        """Gets the score of this Group.


        :return: The score of this Group.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score: float):
        """Sets the score of this Group.


        :param score: The score of this Group.
        :type score: float
        """

        self._score = score

    @property
    def run_count(self) -> int:
        """Gets the run_count of this Group.


        :return: The run_count of this Group.
        :rtype: int
        """
        return self._run_count

    @run_count.setter
    def run_count(self, run_count: int):
        """Sets the run_count of this Group.


        :param run_count: The run_count of this Group.
        :type run_count: int
        """

        self._run_count = run_count

    @property
    def num_participants(self) -> int:
        """Gets the num_participants of this Group.


        :return: The num_participants of this Group.
        :rtype: int
        """
        return self._num_participants

    @num_participants.setter
    def num_participants(self, num_participants: int):
        """Sets the num_participants of this Group.


        :param num_participants: The num_participants of this Group.
        :type num_participants: int
        """

        self._num_participants = num_participants

    @property
    def sum_duration(self) -> int:
        """Gets the sum_duration of this Group.


        :return: The sum_duration of this Group.
        :rtype: int
        """
        return self._sum_duration

    @sum_duration.setter
    def sum_duration(self, sum_duration: int):
        """Sets the sum_duration of this Group.


        :param sum_duration: The sum_duration of this Group.
        :type sum_duration: int
        """

        self._sum_duration = sum_duration

    @property
    def sum_distance_walk(self) -> float:
        """Gets the sum_distance_walk of this Group.


        :return: The sum_distance_walk of this Group.
        :rtype: float
        """
        return self._sum_distance_walk

    @sum_distance_walk.setter
    def sum_distance_walk(self, sum_distance_walk: float):
        """Sets the sum_distance_walk of this Group.


        :param sum_distance_walk: The sum_distance_walk of this Group.
        :type sum_distance_walk: float
        """

        self._sum_distance_walk = sum_distance_walk

    @property
    def sum_distance_run(self) -> float:
        """Gets the sum_distance_run of this Group.


        :return: The sum_distance_run of this Group.
        :rtype: float
        """
        return self._sum_distance_run

    @sum_distance_run.setter
    def sum_distance_run(self, sum_distance_run: float):
        """Sets the sum_distance_run of this Group.


        :param sum_distance_run: The sum_distance_run of this Group.
        :type sum_distance_run: float
        """

        self._sum_distance_run = sum_distance_run

    @property
    def sum_distance_bike(self) -> float:
        """Gets the sum_distance_bike of this Group.


        :return: The sum_distance_bike of this Group.
        :rtype: float
        """
        return self._sum_distance_bike

    @sum_distance_bike.setter
    def sum_distance_bike(self, sum_distance_bike: float):
        """Sets the sum_distance_bike of this Group.


        :param sum_distance_bike: The sum_distance_bike of this Group.
        :type sum_distance_bike: float
        """

        self._sum_distance_bike = sum_distance_bike

    @property
    def sum_distance_ebike(self) -> float:
        """Gets the sum_distance_ebike of this Group.


        :return: The sum_distance_ebike of this Group.
        :rtype: float
        """
        return self._sum_distance_ebike

    @sum_distance_ebike.setter
    def sum_distance_ebike(self, sum_distance_ebike: float):
        """Sets the sum_distance_ebike of this Group.


        :param sum_distance_ebike: The sum_distance_ebike of this Group.
        :type sum_distance_ebike: float
        """

        self._sum_distance_ebike = sum_distance_ebike
