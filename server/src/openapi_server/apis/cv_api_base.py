# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import StrictBytes, StrictStr
from typing import Tuple, Union
from openapi_server.models.cv_post404_response import CvPost404Response
from openapi_server.models.cv_post_request import CvPostRequest


class BaseCvApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseCvApi.subclasses = BaseCvApi.subclasses + (cls,)
    async def cv_post(
        self,
        cv_post_request: CvPostRequest,
    ) -> file:
        """Returns the CV of the person matching the given first and last name as a PDF file."""
        ...
