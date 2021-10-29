from typing import List
from pydantic import BaseModel
from Application.Dtos.Roles.Role import Role







class Account(BaseModel) : 

    Id:str
    Login:str
    Password:str
    Roles:List[Role]