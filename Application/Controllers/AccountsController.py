from Domain.Entities.Account import Account
from Startup.FastApiService import FastApiService
from Infrastructure.Services.SessionService import SessionService
from Application.Services.TokenService import TokenService
from Domain.Entities.Role import Role
from Application.Dtos.Accounts.Account import Account as AccountDto

class AccountsController : 

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
            "/accounts/",
            endpoint=self.Create,
            methods=["POST"],
            # dependencies=[Depends(self._tokenService.VerifyRequest)]
        )
        
        self._fastApiService.FastAPI.add_api_route(
            "/accounts/{accountId}",
            endpoint=self.GetById,
            methods=["GET"],
            # dependencies=[Depends(self._tokenService.VerifyRequest)]
        )

        self._fastApiService.FastAPI.add_api_route(
            "/accounts/",
            endpoint=self.GetAll,
            methods=["GET"],
            # dependencies=[Depends(self._tokenService.VerifyRequest)]
        )

        self._fastApiService.FastAPI.add_api_route(
            "/accounts/",
            endpoint=self.Update,
            methods=["PUT"],
            # dependencies=[Depends(self._tokenService.VerifyRequest)]
        )

        self._fastApiService.FastAPI.add_api_route(
            "/accounts/{accountId}",
            endpoint=self.Delete,
            methods=["DELETE"],
            # dependencies=[Depends(self._tokenService.VerifyRequest)]
        )



    async def Create(self, accountDto:AccountDto) : 

        try : 

            accountRoles = []

            for role in accountDto.Roles : 

                accountRoles.append(self._sessionService.DBContext.query(Role).filter(Role.Id == role.Id).one())

            
            account = Account(accountDto.Id, accountDto.Login, accountDto.Password, accountRoles)

            self._sessionService.DBContext.add(account)

            self._sessionService.DBContext.commit()

        except :

            self._sessionService.DBContext.rollback()

    async def GetById(self, accountId:str) :         
        return self._sessionService.DBContext.query(Account).filter(Account.Id == accountId).one()

    async def GetAll(self) : 
        return self._sessionService.DBContext.query(Account).all()

    async def Update(self, accountDto:AccountDto) : 

        try : 

            account:Account = self._sessionService.DBContext.query(Account).filter(Account.Id == accountDto.Id).one()

            accountRoles = []

            for role in accountDto.Roles : 

                accountRoles.append(self._sessionService.DBContext.query(Role).filter(Role.Id == role.Id).one())


            account.Update(accountDto.Login, accountDto.Password, accountRoles)

            self._sessionService.DBContext.commit()

        except : 

            self._sessionService.DBContext.rollback()

    async def Delete(self, accountId:str) : 
        
        try : 
            account = self._sessionService.DBContext.query(Account).filter(Account.Id == accountId).one()

            self._sessionService.DBContext.delete(account)

            self._sessionService.DBContext.commit()

        except : 

            self._sessionService.DBContext.rollback()
