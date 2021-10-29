from starlette.requests import Request
from fastapi import HTTPException
import jwt
from Application.Services.ConfigurationService import ConfigurationService

class TokenService() : 
    
    _configurationService:ConfigurationService

    def __init__(self, configurationService:ConfigurationService) -> None:
        self._configurationService = configurationService

    def VerifyRequest(self, request: Request) :

        try:
            token = request.headers.get('authorization', None)
            payload = jwt.decode(token, key=self._configurationService.TokenSecretKey, algorithms=self._configurationService.TokenAlgorithm)
            """ self._userDto = User(payload['user']) """

        except Exception:
            raise  HTTPException(status_code=401)