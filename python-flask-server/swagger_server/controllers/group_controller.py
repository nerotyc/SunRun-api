import connexion
import six

from swagger_server.models.bad_request_response import BadRequestResponse  # noqa: E501
from swagger_server.models.deleted_response import DeletedResponse  # noqa: E501
from swagger_server.models.group import Group  # noqa: E501
from swagger_server.models.model404_response import Model404Response  # noqa: E501
from swagger_server.models.saved_response import SavedResponse  # noqa: E501
from swagger_server.models.unauthorized_response import UnauthorizedResponse  # noqa: E501
from swagger_server import util


def create_group(name, distance=None):  # noqa: E501
    """Creates a new group

     # noqa: E501

    :param name: name of new group
    :type name: str
    :param distance: description of new group
    :type distance: str

    :rtype: SavedResponse
    """
    return 'do some magic!'


def delete_group(group_id):  # noqa: E501
    """Deletes the group with the specified id

     # noqa: E501

    :param group_id: id of group to return
    :type group_id: int

    :rtype: DeletedResponse
    """
    return 'do some magic!'


def get_group_by_id(group_id):  # noqa: E501
    """Find group by id

    Returns a single group # noqa: E501

    :param group_id: id of group to return
    :type group_id: int

    :rtype: Group
    """
    return 'do some magic!'


def list_groups():  # noqa: E501
    """list_groups

    Returns a list with a user&#39;s groups # noqa: E501


    :rtype: List[Group]
    """
    return 'do some magic!'


def list_groups_user():  # noqa: E501
    """list_groups_user

    Returns a list with all groups # noqa: E501


    :rtype: List[Group]
    """
    return 'do some magic!'


def update_group(group_id, name, distance=None):  # noqa: E501
    """Update an existing pet

     # noqa: E501

    :param group_id: id of group to return
    :type group_id: int
    :param name: name of new group
    :type name: str
    :param distance: description of new group
    :type distance: str

    :rtype: SavedResponse
    """
    return 'do some magic!'
