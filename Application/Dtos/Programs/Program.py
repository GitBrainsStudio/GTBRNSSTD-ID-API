from typing import List
from pydantic import BaseModel
from Application.Dtos.Roles.Role import Role



class Program(BaseModel) : 

    Id:str
    URL:str
    Description:str 
    Roles:List[Role]