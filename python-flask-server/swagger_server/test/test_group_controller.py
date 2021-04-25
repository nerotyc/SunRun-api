# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.bad_request_response import BadRequestResponse  # noqa: E501
from swagger_server.models.deleted_response import DeletedResponse  # noqa: E501
from swagger_server.models.group import Group  # noqa: E501
from swagger_server.models.model404_response import Model404Response  # noqa: E501
from swagger_server.models.saved_response import SavedResponse  # noqa: E501
from swagger_server.models.unauthorized_response import UnauthorizedResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGroupController(BaseTestCase):
    """GroupController integration test stubs"""

    def test_create_group(self):
        """Test case for create_group

        Creates a new group
        """
        query_string = [('name', 'name_example'),
                        ('distance', 'distance_example')]
        response = self.client.open(
            '/api/v1//group/create/',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_group(self):
        """Test case for delete_group

        Deletes the group with the specified id
        """
        response = self.client.open(
            '/api/v1//group/delete/{group_id}/'.format(group_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_group_by_id(self):
        """Test case for get_group_by_id

        Find group by id
        """
        response = self.client.open(
            '/api/v1//group/{group_id}/'.format(group_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_groups(self):
        """Test case for list_groups

        
        """
        response = self.client.open(
            '/api/v1//group/user/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_groups_user(self):
        """Test case for list_groups_user

        
        """
        response = self.client.open(
            '/api/v1//group/list/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_group(self):
        """Test case for update_group

        Update an existing pet
        """
        query_string = [('name', 'name_example'),
                        ('distance', 'distance_example')]
        response = self.client.open(
            '/api/v1//group/edit/{group_id}/'.format(group_id=789),
            method='PUT',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
