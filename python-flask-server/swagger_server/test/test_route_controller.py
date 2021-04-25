# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.bad_request_response import BadRequestResponse  # noqa: E501
from swagger_server.models.deleted_response import DeletedResponse  # noqa: E501
from swagger_server.models.model404_response import Model404Response  # noqa: E501
from swagger_server.models.route import Route  # noqa: E501
from swagger_server.models.run import Run  # noqa: E501
from swagger_server.models.saved_response import SavedResponse  # noqa: E501
from swagger_server.models.unauthorized_response import UnauthorizedResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRouteController(BaseTestCase):
    """RouteController integration test stubs"""

    def test_create_route(self):
        """Test case for create_route

        Creates a new route
        """
        query_string = [('title', 3.4),
                        ('distance', 3.4),
                        ('elevation_gain', 3.4),
                        ('description', 'description_example'),
                        ('link', 'link_example')]
        response = self.client.open(
            '/api/v1//route/create/',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_route(self):
        """Test case for delete_route

        Deletes the run with the specified id
        """
        response = self.client.open(
            '/api/v1//route/delete/{run_id}/'.format(run_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_route_by_id(self):
        """Test case for get_route_by_id

        Find route by id
        """
        response = self.client.open(
            '/api/v1//route/{route_id}/'.format(route_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_routes(self):
        """Test case for list_routes

        
        """
        response = self.client.open(
            '/api/v1//route/user/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_routes_user(self):
        """Test case for list_routes_user

        
        """
        response = self.client.open(
            '/api/v1//route/list/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_route_update(self):
        """Test case for route_update

        Update an existing pet
        """
        query_string = [('title', 3.4),
                        ('distance', 3.4),
                        ('elevation_gain', 3.4),
                        ('description', 'description_example'),
                        ('link', 'link_example')]
        response = self.client.open(
            '/api/v1//route/edit/{route_id}/'.format(route_id=789),
            method='PUT',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
