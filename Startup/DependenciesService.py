from Application.Controllers.AccountsController import AccountsController
from Application.Controllers.RolesController import RolesController
from Application.Services.TokenService import TokenService
from Application.Services.ConfigurationService import ConfigurationService
from Startup.FastApiService import FastApiService
from Startup.UvicornService import UvicornService
from Infrastructure.Services.SessionService import SessionService
from Application.Controllers.DocumentationController import DocumentationController
from Application.Controllers.ClientsController import ClientsController

class DependenciesService() :

    _configurationService:ConfigurationService
    _fastApiService:FastApiService
    _uvicornService:UvicornService
    _sessionService:SessionService
    _tokenService:TokenService

    def __init__(self) -> None:
        self._configurationService = None
        self._sessionService = None
        self._fastApiService = None
        self._uvicornService = None
        self._tokenService = None

    @property
    def ConfigurationService(self) : 
        if not self._configurationService :
            self._configurationService = ConfigurationService()
        return self._configurationService

    @property
    def FastApiService(self) -> FastApiService : 
        if not self._fastApiService :
            self._fastApiService = FastApiService(
                self.ConfigurationService,
            )
        return self._fastApiService

    @property
    def UvicornService(self) : 
        if not self._uvicornService :
            self._uvicornService = UvicornService(
                self.ConfigurationService,
                self.FastApiService,
            )
        return self._uvicornService

    @property
    def SessionService(self) : 
        if not self._sessionService :
            self._sessionService = SessionService(
                self.ConfigurationService
            )
        return self._sessionService

    @property
    def TokenService(self) : 
        if not self._tokenService : 
            self._tokenService = TokenService(
                self.ConfigurationService
            )
        return self._tokenService


    def RegisterControllers(self) :
        DocumentationController(
            self.FastApiService
        )
        ClientsController(
            self.FastApiService,
            self.SessionService,
            self.TokenService
        ),
        AccountsController(
            self.FastApiService,
            self.SessionService,
            self.TokenService
        ),
        RolesController(
            self.FastApiService,
            self.SessionService,
            self.TokenService
        )