# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Route(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, creator_id: int=None, route_id: int=None, distance: float=None, elevation_gain: float=None, type: str=None, time_start: datetime=None, duration: int=None, note: str=None, group_id: int=None):  # noqa: E501
        """Route - a model defined in Swagger

        :param id: The id of this Route.  # noqa: E501
        :type id: int
        :param creator_id: The creator_id of this Route.  # noqa: E501
        :type creator_id: int
        :param route_id: The route_id of this Route.  # noqa: E501
        :type route_id: int
        :param distance: The distance of this Route.  # noqa: E501
        :type distance: float
        :param elevation_gain: The elevation_gain of this Route.  # noqa: E501
        :type elevation_gain: float
        :param type: The type of this Route.  # noqa: E501
        :type type: str
        :param time_start: The time_start of this Route.  # noqa: E501
        :type time_start: datetime
        :param duration: The duration of this Route.  # noqa: E501
        :type duration: int
        :param note: The note of this Route.  # noqa: E501
        :type note: str
        :param group_id: The group_id of this Route.  # noqa: E501
        :type group_id: int
        """
        self.swagger_types = {
            'id': int,
            'creator_id': int,
            'route_id': int,
            'distance': float,
            'elevation_gain': float,
            'type': str,
            'time_start': datetime,
            'duration': int,
            'note': str,
            'group_id': int
        }

        self.attribute_map = {
            'id': 'id',
            'creator_id': 'creator_id',
            'route_id': 'route_id',
            'distance': 'distance',
            'elevation_gain': 'elevation_gain',
            'type': 'type',
            'time_start': 'time_start',
            'duration': 'duration',
            'note': 'note',
            'group_id': 'group_id'
        }

        self._id = id
        self._creator_id = creator_id
        self._route_id = route_id
        self._distance = distance
        self._elevation_gain = elevation_gain
        self._type = type
        self._time_start = time_start
        self._duration = duration
        self._note = note
        self._group_id = group_id

    @classmethod
    def from_dict(cls, dikt) -> 'Route':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Route of this Route.  # noqa: E501
        :rtype: Route
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Route.


        :return: The id of this Route.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Route.


        :param id: The id of this Route.
        :type id: int
        """

        self._id = id

    @property
    def creator_id(self) -> int:
        """Gets the creator_id of this Route.


        :return: The creator_id of this Route.
        :rtype: int
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id: int):
        """Sets the creator_id of this Route.


        :param creator_id: The creator_id of this Route.
        :type creator_id: int
        """

        self._creator_id = creator_id

    @property
    def route_id(self) -> int:
        """Gets the route_id of this Route.

        if null: fields istn't part of json object  # noqa: E501

        :return: The route_id of this Route.
        :rtype: int
        """
        return self._route_id

    @route_id.setter
    def route_id(self, route_id: int):
        """Sets the route_id of this Route.

        if null: fields istn't part of json object  # noqa: E501

        :param route_id: The route_id of this Route.
        :type route_id: int
        """

        self._route_id = route_id

    @property
    def distance(self) -> float:
        """Gets the distance of this Route.


        :return: The distance of this Route.
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance: float):
        """Sets the distance of this Route.


        :param distance: The distance of this Route.
        :type distance: float
        """

        self._distance = distance

    @property
    def elevation_gain(self) -> float:
        """Gets the elevation_gain of this Route.


        :return: The elevation_gain of this Route.
        :rtype: float
        """
        return self._elevation_gain

    @elevation_gain.setter
    def elevation_gain(self, elevation_gain: float):
        """Sets the elevation_gain of this Route.


        :param elevation_gain: The elevation_gain of this Route.
        :type elevation_gain: float
        """

        self._elevation_gain = elevation_gain

    @property
    def type(self) -> str:
        """Gets the type of this Route.

        Activity Type (not just run)  # noqa: E501

        :return: The type of this Route.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this Route.

        Activity Type (not just run)  # noqa: E501

        :param type: The type of this Route.
        :type type: str
        """
        allowed_values = ["WALK", "RUN", "BIKE", "E-BIKE"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def time_start(self) -> datetime:
        """Gets the time_start of this Route.


        :return: The time_start of this Route.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start: datetime):
        """Sets the time_start of this Route.


        :param time_start: The time_start of this Route.
        :type time_start: datetime
        """

        self._time_start = time_start

    @property
    def duration(self) -> int:
        """Gets the duration of this Route.


        :return: The duration of this Route.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration: int):
        """Sets the duration of this Route.


        :param duration: The duration of this Route.
        :type duration: int
        """

        self._duration = duration

    @property
    def note(self) -> str:
        """Gets the note of this Route.

        if null: fields istn't part of json object  # noqa: E501

        :return: The note of this Route.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note: str):
        """Sets the note of this Route.

        if null: fields istn't part of json object  # noqa: E501

        :param note: The note of this Route.
        :type note: str
        """

        self._note = note

    @property
    def group_id(self) -> int:
        """Gets the group_id of this Route.

        if null: fields istn't part of json object  # noqa: E501

        :return: The group_id of this Route.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id: int):
        """Sets the group_id of this Route.

        if null: fields istn't part of json object  # noqa: E501

        :param group_id: The group_id of this Route.
        :type group_id: int
        """

        self._group_id = group_id
