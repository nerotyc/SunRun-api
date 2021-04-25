import connexion
import six

from swagger_server.models.unauthorized_response import UnauthorizedResponse  # noqa: E501
from swagger_server.models.user_ids import UserIds  # noqa: E501
from swagger_server import util


def user_id():  # noqa: E501
    """Gets user_id and profile_id of currently logged in user.

     # noqa: E501


    :rtype: UserIds
    """
    return 'do some magic!'
