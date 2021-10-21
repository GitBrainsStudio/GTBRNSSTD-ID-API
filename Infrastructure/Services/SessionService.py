from Application.Services.ConfigurationService import ConfigurationService
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker





class SessionService() : 

        _dbContext:Session
        _sessionMaker:sessionmaker
        _engine:Engine
        _configurationService:ConfigurationService

        def __init__(self, configurationService:ConfigurationService) -> None:
            self._dbContext = None
            self._configurationService = configurationService
            self._engine = create_engine(self._configurationService.SQLiteConnectionString)
            self._sessionMaker = sessionmaker(bind=self._engine)

        @property
        def DBContext(self) -> Session :
            if not self._dbContext :
                self._dbContext = self._sessionMaker()
            return self._dbContext