import unittest

from flask import json

from openapi_server.models.cv_get404_response import CvGet404Response  # noqa: E501
from openapi_server.test import BaseTestCase


class TestCvController(BaseTestCase):
    """CvController integration test stubs"""

    def test_cv_get(self):
        """Test case for cv_get

        Download CV PDF
        """
        query_string = [('firstName', 'first_name_example'),
                        ('lastName', 'last_name_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/cv',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
