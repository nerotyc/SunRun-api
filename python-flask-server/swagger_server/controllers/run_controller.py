import connexion
import six

from swagger_server.models.bad_request_response import BadRequestResponse  # noqa: E501
from swagger_server.models.deleted_response import DeletedResponse  # noqa: E501
from swagger_server.models.model404_response import Model404Response  # noqa: E501
from swagger_server.models.run import Run  # noqa: E501
from swagger_server.models.saved_response import SavedResponse  # noqa: E501
from swagger_server.models.unauthorized_response import UnauthorizedResponse  # noqa: E501
from swagger_server import util


def delete_run(run_id):  # noqa: E501
    """Deletes the run with the specified id

     # noqa: E501

    :param run_id: id of run to return
    :type run_id: int

    :rtype: DeletedResponse
    """
    return 'do some magic!'


def get_run_by_id(run_id):  # noqa: E501
    """Find run by id

    Returns a single run # noqa: E501

    :param run_id: id of run to return
    :type run_id: int

    :rtype: Run
    """
    return 'do some magic!'


def list_runs():  # noqa: E501
    """list_runs

    Returns a list with a user&#39;s runs # noqa: E501


    :rtype: List[Run]
    """
    return 'do some magic!'


def run_create(distance, type, duration, elevation_gain=None, time_start=None, group_id=None, note=None):  # noqa: E501
    """Creates a new run

     # noqa: E501

    :param distance: traveled distance (when route specified route.distance will be used)
    :type distance: float
    :param type: activitiy type
    :type type: str
    :param duration: id of run&#39;s route
    :type duration: int
    :param elevation_gain: traveled acceleration (when route specified route.elevation_gain will be used)
    :type elevation_gain: float
    :param time_start: time when the run started
    :type time_start: int
    :param group_id: id of run&#39;s route
    :type group_id: int
    :param note: id of run&#39;s route
    :type note: str

    :rtype: SavedResponse
    """
    return 'do some magic!'


def run_update(run_id, distance, type, duration, route_id=None, elevation_gain=None, time_start=None, group_id=None, note=None):  # noqa: E501
    """Update an existing pet

     # noqa: E501

    :param run_id: id of run to edit
    :type run_id: int
    :param distance: traveled distance (when route specified route.distance will be used)
    :type distance: float
    :param type: activitiy type
    :type type: str
    :param duration: id of run&#39;s route
    :type duration: int
    :param route_id: id of run&#39;s route
    :type route_id: int
    :param elevation_gain: traveled acceleration (when route specified route.elevation_gain will be used)
    :type elevation_gain: float
    :param time_start: time when the run started
    :type time_start: int
    :param group_id: id of run&#39;s route
    :type group_id: int
    :param note: id of run&#39;s route
    :type note: str

    :rtype: SavedResponse
    """
    return 'do some magic!'
