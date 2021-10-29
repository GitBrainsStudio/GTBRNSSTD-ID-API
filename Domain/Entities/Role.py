from sqlalchemy.sql.schema import ForeignKey
from Domain.Entities.Base import Base
from sqlalchemy import Column, String, Integer



class Role(Base) : 

    __tablename__ = 'roles'

    Id = Column('id', String , primary_key=True)
    Name = Column('name', String)
    Description = Column('description', String)
    ApplicationId = Column('application_id', String, ForeignKey('applications.id'))

    def __init__(
        self,
        id,
        name,
        description,
        applicationId) :

        self.Id = id
        self.Name = name
        self.Description = description
        self.ApplicationId = applicationId


