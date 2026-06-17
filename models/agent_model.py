from pydantic import BaseModel,Field
from typing import Literal



class AgentData(BaseModel):
    name:str=Field(max_length=50)
    specialty:str=Field(max_length=100)
    agent_rank:Literal['Junior','Senior','Commander']
    