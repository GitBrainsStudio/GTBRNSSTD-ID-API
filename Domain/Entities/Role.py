import uuid
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from Domain.Entities.Base import Base
from sqlalchemy import Column, String, Integer
from Domain.Entities.Client import Client



class Role(Base) : 

    __tablename__ = 'roles'

    Id = Column('id', String , primary_key=True)
    Name = Column('name', String)
    ClientId = Column('client_id', String, ForeignKey(Client.Id))

    def __init__(
        self,
        id,
        name,
        clientId) :

        self.Id = uuid.uuid4().hex
        self.Name = name
        self.ClientId = clientId


