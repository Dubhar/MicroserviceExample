from openapi_server.apis.cv_api_base import BaseCvApi
from fastapi import Response
from openapi_server.models.cv_post_request import CvPostRequest
import os

class CvApiImpl(BaseCvApi):
    async def cv_post(self, cv_post_request: CvPostRequest) -> Response:
        filename = "Google.pdf"
        pdf_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", filename))

        if not os.path.exists(pdf_path):
            from fastapi import HTTPException
            raise HTTPException(status_code=404, detail=f"CV not found for {cv_post_request.first_name} {cv_post_request.last_name}")

        with open(pdf_path, "rb") as f:
            pdf_bytes = f.read()

        return Response(content=pdf_bytes, media_type="application/pdf")
