from Startup.FastApiService import FastApiService
from Application.Services.ConfigurationService import ConfigurationService
import uvicorn

class UvicornService() : 

    _configurationService:ConfigurationService
    _fastApiService:FastApiService

    def __init__(self, 
    configurationService:ConfigurationService,
    fastApiService:FastApiService) :

        self._configurationService = configurationService
        self._fastApiService = fastApiService

    def RunApi(self) : 
        uvicorn.run(
            app = self._fastApiService.GetFastApiWithCORS(), 
            host=self._configurationService.UvicornHost, 
            port=self._configurationService.UvicornPort)
