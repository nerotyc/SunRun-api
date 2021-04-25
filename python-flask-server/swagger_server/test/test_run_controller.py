# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.bad_request_response import BadRequestResponse  # noqa: E501
from swagger_server.models.deleted_response import DeletedResponse  # noqa: E501
from swagger_server.models.model404_response import Model404Response  # noqa: E501
from swagger_server.models.run import Run  # noqa: E501
from swagger_server.models.saved_response import SavedResponse  # noqa: E501
from swagger_server.models.unauthorized_response import UnauthorizedResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRunController(BaseTestCase):
    """RunController integration test stubs"""

    def test_delete_run(self):
        """Test case for delete_run

        Deletes the run with the specified id
        """
        response = self.client.open(
            '/api/v1//run/delete/{run_id}/'.format(run_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_run_by_id(self):
        """Test case for get_run_by_id

        Find run by id
        """
        response = self.client.open(
            '/api/v1//run/{run_id}/'.format(run_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_runs(self):
        """Test case for list_runs

        
        """
        response = self.client.open(
            '/api/v1//run/user/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_run_create(self):
        """Test case for run_create

        Creates a new run
        """
        query_string = [('distance', 3.4),
                        ('elevation_gain', 0),
                        ('type', 'type_example'),
                        ('time_start', 56),
                        ('duration', 789),
                        ('group_id', 789),
                        ('note', 'note_example')]
        response = self.client.open(
            '/api/v1//run/create/',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_run_update(self):
        """Test case for run_update

        Update an existing pet
        """
        query_string = [('route_id', 789),
                        ('distance', 3.4),
                        ('elevation_gain', 0),
                        ('type', 'type_example'),
                        ('time_start', 56),
                        ('duration', 789),
                        ('group_id', 789),
                        ('note', 'note_example')]
        response = self.client.open(
            '/api/v1//run/edit/{run_id}/'.format(run_id=789),
            method='PUT',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
