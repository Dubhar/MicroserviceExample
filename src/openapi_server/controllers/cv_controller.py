import connexion
import os
from flask import send_file, abort
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.cv_get404_response import CvGet404Response  # noqa: E501
from openapi_server import util


def cv_get(first_name, last_name):  # noqa: E501
    """Download CV PDF

    Returns the CV of the person matching the given first and last name as a PDF file. # noqa: E501

    :param first_name: Person&#39;s first name
    :type first_name: str
    :param last_name: Person&#39;s last name
    :type last_name: str

    :rtype: Union[file, Tuple[file, int], Tuple[file, int, Dict[str, str]]
    """
    pdf_path = os.path.join(os.path.dirname(__file__), '..', '..', 'Google.pdf')
    pdf_path = os.path.abspath(pdf_path)

    if not os.path.exists(pdf_path):
        abort(404, description="Static CV not found on server")

    # Flask's send_file handles content-type and headers automatically
    return send_file(pdf_path, mimetype='application/pdf')

