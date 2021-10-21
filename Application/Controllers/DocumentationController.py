from Startup.FastApiService import FastApiService
from fastapi.openapi.docs import (
    get_swagger_ui_html
)
import os


class DocumentationController : 

    _fastApiService:FastApiService

    def __init__(self, fastApiService:FastApiService) -> None:
        self._fastApiService = fastApiService
        self._fastApiService.FastAPI.add_api_route(
            "/documentation",
            endpoint=self.GetSwaggerDocumentationFromStaticFiles,
            methods=["GET"]
        )


    async def GetSwaggerDocumentationFromStaticFiles(self):
        return get_swagger_ui_html(
            openapi_url= self._fastApiService.FastAPI.openapi_url,
            title= self._fastApiService.FastAPI.title,
            oauth2_redirect_url= self._fastApiService.FastAPI.swagger_ui_oauth2_redirect_url,
            swagger_js_url= os.path.join("static", "api-documentation", "swagger-ui-bundle.js"),
            swagger_css_url= os.path.join("static", "api-documentation", "swagger-ui.css"),
        )