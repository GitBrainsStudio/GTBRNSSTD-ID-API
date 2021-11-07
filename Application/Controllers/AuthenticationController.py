from sqlalchemy import func
from Domain.Entities.Account import Account
from Startup.FastApiService import FastApiService
from Infrastructure.Services.SessionService import SessionService
from Application.Services.TokenService import TokenService
from Domain.Entities.Role import Role

class AuthenticationController : 

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
            "/authenticate",
            endpoint=self.Authenticate,
            methods=["GET"],
        )
        


    def Authenticate(self, login:str, password:str, programId:str) : 

        account:Account = self._sessionService.DBContext.query(Account).filter(
            Account.Login == login, 
            Account.Password == password, 
            Account.Roles.any(func.lower(Role.ProgramId) == func.lower(programId))
            ).one()

        accountDto = account.AsJson(programId)
        accessToken = self._tokenService.GenerateToken(accountDto)
        
        return {
            "account" : accountDto,
            "access_token" : accessToken
        }