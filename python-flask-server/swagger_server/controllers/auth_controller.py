import connexion
import six

from swagger_server.models.bad_login_response import BadLoginResponse  # noqa: E501
from swagger_server.models.login_response import LoginResponse  # noqa: E501
from swagger_server.models.unauthorized_response import UnauthorizedResponse  # noqa: E501
from swagger_server import util


def auth_login(username, password):  # noqa: E501
    """Fetching an access_token by username &amp; password request

     # noqa: E501

    :param username: The username for login
    :type username: str
    :param password: The password for login in clear text
    :type password: str

    :rtype: LoginResponse
    """
    return 'do some magic!'


def test_token():  # noqa: E501
    """Test if access_token is valid

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'
