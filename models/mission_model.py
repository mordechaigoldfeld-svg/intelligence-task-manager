from pydantic import BaseModel,Field
from typing import Literal



class MissionsData(BaseModel):
    title:str=Field(max_length=50)
    description:str
    location:str
    difficulty:int=Field(ge=1,le=10)
    importance:int=Field(ge=1,le=10)
    status:Literal["NEW","ASSIGGNED","IN_PROGRESS","COMPLETED","FAILED","CANCELLED"]
    