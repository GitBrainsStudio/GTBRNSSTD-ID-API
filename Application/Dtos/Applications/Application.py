from typing import List
from pydantic import BaseModel
from Application.Dtos.Roles.Role import Role



class Application(BaseModel) : 

    Id:str
    Name:str
    URL:str
    Description:str 
    Roles:List[Role]