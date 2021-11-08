
from Domain.Entities.Account import Account
from Startup.FastApiService import FastApiService
from Infrastructure.Services.SessionService import SessionService
from Application.Services.TokenService import TokenService
from sqlalchemy.orm.exc import NoResultFound
from fastapi.responses import JSONResponse


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

        try :

            account:Account = self._sessionService.DBContext.query(Account).filter(
                Account.Login == login, 
                Account.Password == password
                ).one()

        except NoResultFound : 
            return JSONResponse (status_code = 400, content = {"message": "Логин или пароль не подходит" }) 

        accessRole = next((role for role in account.Roles if role.ProgramId == programId), None)

        if (accessRole is None) :
            return JSONResponse (status_code = 400, content = {"message": "Недостаточно прав для входа в приложение" }) 

        accountDto = account.AsJson(programId)
        accessToken = self._tokenService.GenerateToken(accountDto)
        
        return {
            "account" : accountDto,
            "access_token" : accessToken
        }