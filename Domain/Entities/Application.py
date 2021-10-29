from typing import List
from sqlalchemy.orm import relationship
from Domain.Entities.Base import Base
from sqlalchemy import Column, String
from Domain.Entities.Role import Role



class Application(Base) : 

    __tablename__ = 'applications'

    Id = Column('id', String , primary_key=True)
    Name = Column('name', String)
    URL =  Column('url', String)
    Description = Column('description', String)
    Roles = relationship("Role", cascade="all, delete-orphan", lazy="joined")
    

    def __init__(
        self,
        id:str,
        name:str,
        url:str,
        description:str,
        roles:List[Role]):
        
        self.Id = id
        self.Name = name
        self.URL = url
        self.Description = description
        self.Roles = roles

    def Update(
        self,
        name:str,
        url:str,
        description:str,
        roles:List[Role]) : 


        self.Name = name
        self.URL = url
        self.Description = description
        self.Roles = roles
        


    
