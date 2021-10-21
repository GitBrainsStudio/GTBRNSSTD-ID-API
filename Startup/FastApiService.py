from Application.Handlers.ExceptionHandler import ExceptionHandler
from Application.Services.ConfigurationService import ConfigurationService
from fastapi.applications import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

class FastApiService : 

    _fastApi:FastAPI
    _configurationService:ConfigurationService

    @property
    def FastAPI(self) -> FastAPI : 
        return self._fastApi
    

    def __init__(
        self, 
        configurationService:ConfigurationService) :
        self._configurationService = configurationService

        self.CreateFastAPI()
        self.ActivateStaticFiles()
        self.AddExceptionHandlers()


    def CreateFastAPI(self) : 
        self._fastApi = FastAPI(
                            title=self._configurationService.FastApiTitle, 
                            version=self._configurationService.FastApiVersion, 
                            description=self._configurationService.FastApiDescription,
                            docs_url=None, 
                            redoc_url=None)
        
    def ActivateStaticFiles(self) :
        self._fastApi.mount("/static/api-documentation", StaticFiles(directory="Static/ApiDocumentation"), name="/static/api-documentation")

    def AddExceptionHandlers(self) : 
        self._fastApi.add_exception_handler(Exception, ExceptionHandler().OnException)

    def GetFastApiWithCORS(self) : 
        return CORSMiddleware(
        self._fastApi,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )