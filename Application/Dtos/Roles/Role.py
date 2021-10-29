from typing import List
from pydantic import BaseModel


class Role(BaseModel) : 

    Id:str
    Name:str
    Description:str
    ApplicationId:str