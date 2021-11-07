from logging import log
import logging
from typing import List
from sqlalchemy.orm import relationship
from Domain.Entities.Base import Base, AccountsRoles
from sqlalchemy import Column, String, Integer
from Domain.Entities.Role import Role
import uuid


class Account(Base) : 

    __tablename__ = 'accounts'

    Id = Column('id', String , primary_key=True)
    Login = Column('login', String)
    Password =  Column('password', String)
    Roles:List[Role] = relationship(
        'Role',
        secondary=AccountsRoles,
        lazy='joined')

    def __init__(
        self,
        id,
        login,
        password,
        roles) :
    
        self.Id = id
        self.Login = login
        self.Password = password
        self.Roles = roles

    def Update(
        self,
        login,
        password,
        roles
    ) :
        self.Login = login
        self.Password = password
        self.Roles = roles


    def AsJson(self, programId) : 

        roles = []

        for role in self.Roles : 
            if (role.ProgramId.lower() == programId.lower()) :
                roles.append(role.AsJson())

        return {
            "id" : self.Id,
            "login" : self.Login,
            "roles" : roles
        }


    
