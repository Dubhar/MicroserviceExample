# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import StrictBytes, StrictStr  # noqa: F401
from typing import Tuple, Union  # noqa: F401
from openapi_server.models.cv_post404_response import CvPost404Response  # noqa: F401
from openapi_server.models.cv_post_request import CvPostRequest  # noqa: F401


def test_cv_post(client: TestClient):
    """Test case for cv_post

    Download CV PDF
    """
    cv_post_request = openapi_server.CvPostRequest()

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/cv",
    #    headers=headers,
    #    json=cv_post_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

