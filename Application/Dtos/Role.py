class Role() : 

    id:str
    title:str
    description:str
    programid:str

    def __init__(self, jwtPayload:str) -> None:
        
        self.id = jwtPayload['id']
        self.title = jwtPayload['title']
        self.description = jwtPayload['description']
        self.programid = jwtPayload['program-id']

