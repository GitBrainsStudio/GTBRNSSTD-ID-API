from typing import List
from pydantic import BaseModel


class Role(BaseModel) : 

    Id:str
    Name:str
    Description:str
    ProgramId:str

    @property
    def AsJson(self) : 
        return {
            "id" : self.Id,
            "name" : self.Name,
            "descriptiption" : self.Description,
            "programId" : self.ProgramId
        }