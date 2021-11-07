from sqlalchemy.sql.schema import ForeignKey
from Domain.Entities.Base import Base
from sqlalchemy import Column, String, Integer



class Role(Base) : 

    __tablename__ = 'roles'

    Id = Column('id', String , primary_key=True)
    Name = Column('name', String)
    Description = Column('description', String)
    ProgramId = Column('program_id', String, ForeignKey('programs.id'))

    def __init__(
        self,
        id,
        name,
        description,
        programId) :

        self.Id = id
        self.Name = name
        self.Description = description
        self.ProgramId = programId

    def AsJson(self) : 

        return {
            "id" : self.Id,
            "name" : self.Name,
            "description" : self.Description,
            "programId" : self.ProgramId
        }

