import connexion
import six

from swagger_server.models.bad_request_response import BadRequestResponse  # noqa: E501
from swagger_server.models.deleted_response import DeletedResponse  # noqa: E501
from swagger_server.models.model404_response import Model404Response  # noqa: E501
from swagger_server.models.route import Route  # noqa: E501
from swagger_server.models.run import Run  # noqa: E501
from swagger_server.models.saved_response import SavedResponse  # noqa: E501
from swagger_server.models.unauthorized_response import UnauthorizedResponse  # noqa: E501
from swagger_server import util


def create_route(title, distance, elevation_gain, description=None, link=None):  # noqa: E501
    """Creates a new route

     # noqa: E501

    :param title: route&#39;s title
    :type title: float
    :param distance: traveled distance
    :type distance: float
    :param elevation_gain: traveled height
    :type elevation_gain: float
    :param description: descirption of the route
    :type description: str
    :param link: link to route description
    :type link: str

    :rtype: SavedResponse
    """
    return 'do some magic!'


def delete_route(run_id):  # noqa: E501
    """Deletes the run with the specified id

     # noqa: E501

    :param run_id: id of run to return
    :type run_id: int

    :rtype: DeletedResponse
    """
    return 'do some magic!'


def get_route_by_id(route_id):  # noqa: E501
    """Find route by id

    Returns a single route # noqa: E501

    :param route_id: id of route to return
    :type route_id: int

    :rtype: Route
    """
    return 'do some magic!'


def list_routes():  # noqa: E501
    """list_routes

    Returns a list with a user&#39;s runs # noqa: E501


    :rtype: List[Run]
    """
    return 'do some magic!'


def list_routes_user():  # noqa: E501
    """list_routes_user

    Returns a list with a user&#39;s runs # noqa: E501


    :rtype: List[Run]
    """
    return 'do some magic!'


def route_update(route_id, title, distance, elevation_gain, description=None, link=None):  # noqa: E501
    """Update an existing pet

     # noqa: E501

    :param route_id: id of route to edit
    :type route_id: int
    :param title: route&#39;s title
    :type title: float
    :param distance: traveled distance
    :type distance: float
    :param elevation_gain: traveled height
    :type elevation_gain: float
    :param description: descirption of the route
    :type description: str
    :param link: link to route description
    :type link: str

    :rtype: SavedResponse
    """
    return 'do some magic!'
