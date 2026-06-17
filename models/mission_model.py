from pydantic import BaseModel,Field



class MissionsData(BaseModel):
    title:str=Field(max_length=50)
    description:str
    location:str
    dificulty:int=Field(ge=1,le=10)
    importance:int=Field(ge=1,le=10)
    status:str
    