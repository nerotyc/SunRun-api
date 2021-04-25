# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.unauthorized_response import UnauthorizedResponse  # noqa: E501
from swagger_server.models.user_ids import UserIds  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_user_id(self):
        """Test case for user_id

        Gets user_id and profile_id of currently logged in user.
        """
        response = self.client.open(
            '/api/v1//user/user-id/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
