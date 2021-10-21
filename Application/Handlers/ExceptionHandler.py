from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy import exc



class ExceptionHandler() : 


    async def OnException(self, request: Request, exception: Exception):

        return JSONResponse (status_code = 400, content = {"message": "Произошла непредвиденная ошибка на сервисе подразделений" })