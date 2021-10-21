from Domain.Entities.Client import Client
from Startup.FastApiService import FastApiService
from Infrastructure.Services.SessionService import SessionService
from Application.Services.TokenService import TokenService

class ClientsController : 

    _fastApiService:FastApiService
    _sessionService:SessionService
    _tokenService:TokenService

    def __init__(self, 
    fastApiService:FastApiService,
    sessionService:SessionService,
    tokenService:TokenService
    ) :
        self._tokenService = tokenService
        self._sessionService = sessionService
        self._fastApiService = fastApiService

        self._fastApiService.FastAPI.add_api_route(
            "/clients/",
            endpoint=self.GetAll,
            methods=["GET"],
            # dependencies=[Depends(self._tokenService.VerifyRequest)]
        )


    async def GetAll(self) : 
        return self._sessionService.DBContext.query(Client).all()
