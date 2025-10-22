import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.health_get200_response import HealthGet200Response  # noqa: E501
from openapi_server import util


def health_get():  # noqa: E501
    """Public health check

     # noqa: E501


    :rtype: Union[HealthGet200Response, Tuple[HealthGet200Response, int], Tuple[HealthGet200Response, int, Dict[str, str]]
    """
    return {"status": "ok"}

