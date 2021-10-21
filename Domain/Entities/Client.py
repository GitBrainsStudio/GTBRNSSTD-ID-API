from Domain.Entities.Base import Base
from sqlalchemy import Column, String, Integer




class Client(Base) : 

    __tablename__ = 'clients'

    Id = Column('id', String , primary_key=True)
    Name = Column('name', String)
    URL =  Column('url', String)

    
