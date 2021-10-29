from typing import List

from starlette.responses import JSONResponse
from Domain.Entities.Application import Application
from Domain.Entities.Role import Role
from Startup.FastApiService import FastApiService
from Infrastructure.Services.SessionService import SessionService
from Application.Services.TokenService import TokenService
from Application.Dtos.Applications.Application import Application as ApplicationDto
from sqlalchemy.orm.exc import NoResultFound

class ApplicationsController : 

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
            "/applications/",
            endpoint=self.Create,
            methods=["POST"],
            # dependencies=[Depends(self._tokenService.VerifyRequest)]
        )

        self._fastApiService.FastAPI.add_api_route(
            "/applications/{applicationId}",
            endpoint=self.GetById,
            methods=["GET"],
            # dependencies=[Depends(self._tokenService.VerifyRequest)]
        )

        self._fastApiService.FastAPI.add_api_route(
            "/applications/",
            endpoint=self.GetAll,
            methods=["GET"],
            # dependencies=[Depends(self._tokenService.VerifyRequest)]
        )


        self._fastApiService.FastAPI.add_api_route(
            "/applications/",
            endpoint=self.Update,
            methods=["PUT"],
            # dependencies=[Depends(self._tokenService.VerifyRequest)]
        )

        self._fastApiService.FastAPI.add_api_route(
            "/applications/{applicationId}",
            endpoint=self.Delete,
            methods=["DELETE"],
            # dependencies=[Depends(self._tokenService.VerifyRequest)]
        )


    async def Create(self, applicationDto:ApplicationDto) : 

        try : 

            applicationRoles = []

            for roleCreate in applicationDto.Roles : 
                applicationRoles.append(Role(roleCreate.Id, roleCreate.Name, roleCreate.Description, roleCreate.ApplicationId))

            application = Application(applicationDto.Id, applicationDto.Name, applicationDto.URL, applicationDto.Description, applicationRoles)

            self._sessionService.DBContext.add(application)

            self._sessionService.DBContext.commit()

        except : 
 
            self._sessionService.DBContext.rollback()

    async def GetById(self, applicationId:str) :         
        return self._sessionService.DBContext.query(Application).filter(Application.Id == applicationId).one()

    async def GetAll(self) : 
        return self._sessionService.DBContext.query(Application).all()
        
    async def Update(self, applicationDto:ApplicationDto) : 

        try : 

            application:Application = self._sessionService.DBContext.query(Application).filter(Application.Id == applicationDto.Id).one()

            applicationRoles = []

            for roleCreate in applicationDto.Roles : 
                applicationRoles.append(Role(roleCreate.Id, roleCreate.Name, roleCreate.Description, roleCreate.ApplicationId))

            applicationRoles:List[Role] = []
            for applicationRole in applicationDto.Roles : 

                role:Role = Role(applicationRole.Id, applicationRole.Name, applicationRole.Description, applicationRole.ApplicationId)
                applicationRoles.append(role)


            application.Update(applicationDto.Name, applicationDto.Name, applicationDto.Description, applicationRoles)

            self._sessionService.DBContext.commit()

        except : 

            self._sessionService.DBContext.rollback()
           
    async def Delete(self, applicationId:str) : 
        
        try : 
            client = self._sessionService.DBContext.query(Application).filter(Application.Id == applicationId).one()

            self._sessionService.DBContext.delete(client)

            self._sessionService.DBContext.commit()

        except : 

            self._sessionService.DBContext.rollback()

