from typing import List

from fastapi.params import Depends
from Domain.Entities.Account import Account
from Domain.Entities.Program import Program
from Domain.Entities.Role import Role
from Startup.FastApiService import FastApiService
from Infrastructure.Services.SessionService import SessionService
from Application.Services.TokenService import TokenService
from Application.Dtos.Programs.Program import Program as ProgramDto

class ProgramsController : 

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
            "/programs/",
            endpoint=self.Create,
            methods=["POST"],
            dependencies=[Depends(self._tokenService.VerifyRequest)]
        )

        self._fastApiService.FastAPI.add_api_route(
            "/programs/{programId}",
            endpoint=self.GetById,
            methods=["GET"],
            dependencies=[Depends(self._tokenService.VerifyRequest)]
        )

        self._fastApiService.FastAPI.add_api_route(
            "/accounts/{accountId}/programs/",
            endpoint=self.GetAllByAccountId,
            methods=["GET"],
            dependencies=[Depends(self._tokenService.VerifyRequest)]
        )

        self._fastApiService.FastAPI.add_api_route(
            "/programs/",
            endpoint=self.GetAll,
            methods=["GET"],
            dependencies=[Depends(self._tokenService.VerifyRequest)]
        )

        self._fastApiService.FastAPI.add_api_route(
            "/programs/",
            endpoint=self.Update,
            methods=["PUT"],
            dependencies=[Depends(self._tokenService.VerifyRequest)]
        )

        self._fastApiService.FastAPI.add_api_route(
            "/programs/{programId}",
            endpoint=self.Delete,
            methods=["DELETE"],
            dependencies=[Depends(self._tokenService.VerifyRequest)]
        )


    async def Create(self, programDto:ProgramDto) : 

        try : 

            programRoles = []

            for roleCreate in programDto.Roles : 
                programRoles.append(Role(roleCreate.Id, roleCreate.Name, roleCreate.Description, roleCreate.ProgramId))

            program = Program(programDto.Id, programDto.URL, programDto.Description, programRoles)

            self._sessionService.DBContext.add(program)

            self._sessionService.DBContext.commit()

        except : 
 
            self._sessionService.DBContext.rollback()

    async def GetById(self, programId:str) :         
        return self._sessionService.DBContext.query(Program).filter(Program.Id == programId).one()

    async def GetAllByAccountId(self, accountId:str) : 
        
        accountPrograms = []

        account:Account = self._sessionService.DBContext.query(Account).filter(Account.Id == accountId).one()
        
        for accountRole in account.Roles : 
            accountPrograms.append(self._sessionService.DBContext.query(Program).filter(Program.Id == accountRole.ProgramId).one())

        return accountPrograms

    async def GetAll(self) : 
        return self._sessionService.DBContext.query(Program).all()
        
    async def Update(self, programDto:ProgramDto) : 

        try : 

            program:Program = self._sessionService.DBContext.query(Program).filter(Program.Id == programDto.Id).one()

            programRoles = []

            for roleCreate in programDto.Roles : 
                programRoles.append(Role(roleCreate.Id, roleCreate.Name, roleCreate.Description, roleCreate.ProgramId))

            programRoles:List[Role] = []
            for programRole in programDto.Roles : 

                role:Role = Role(programRole.Id, programRole.Name, programRole.Description, programRole.ProgramId)
                programRoles.append(role)


            program.Update(programDto.Id, programDto.URL, programDto.Description, programRoles)

            self._sessionService.DBContext.commit()

        except : 

            self._sessionService.DBContext.rollback()
           
    async def Delete(self, programId:str) : 
        
        try : 
            client = self._sessionService.DBContext.query(Program).filter(Program.Id == programId).one()

            self._sessionService.DBContext.delete(client)

            self._sessionService.DBContext.commit()

        except : 

            self._sessionService.DBContext.rollback()

