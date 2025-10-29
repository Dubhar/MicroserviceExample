# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.cv_api_base import BaseCvApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from pydantic import StrictBytes, StrictStr
from typing import Tuple, Union
from openapi_server.models.cv_post404_response import CvPost404Response
from openapi_server.models.cv_post_request import CvPostRequest


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/cv",
    responses={
        200: {"model": file, "description": "CV PDF file"},
        404: {"model": CvPost404Response, "description": "CV not found"},
    },
    tags=["cv"],
    summary="Download CV PDF",
    response_model_by_alias=True,
)
async def cv_post(
    cv_post_request: CvPostRequest = Body(None, description=""),
) -> file:
    """Returns the CV of the person matching the given first and last name as a PDF file."""
    if not BaseCvApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCvApi.subclasses[0]().cv_post(cv_post_request)
