from Application.Dtos.Role import Role
from typing import List

class User : 


    id: str
    email: str
    login : str
    fullname : str
    organid : str
    serviceid : str
    rankid : str
    roles : List[Role]

    def __init__(self, jwtPayload:str) -> None:
        self.roles = []
        self.id = jwtPayload['id']
        self.email = jwtPayload['email']
        self.login = jwtPayload['login']
        self.fullname = jwtPayload['fullname']
        self.organid = jwtPayload['organid']
        self.serviceid = jwtPayload['serviceid']
        self.rankid = jwtPayload['rankid']
        self.roles = [Role(role) for role in jwtPayload['roles']]