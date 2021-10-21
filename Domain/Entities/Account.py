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
    Roles:Role = relationship(
        'Role',
        secondary=AccountsRoles,
        lazy='joined')

    def __init__(
        self,
        id,
        login,
        password,
        roles) :
    
        self.Id = uuid.uuid4().hex
        self.Login = login
        self.Password = password
        self.Roles = roles

    
