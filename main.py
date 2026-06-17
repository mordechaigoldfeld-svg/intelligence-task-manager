from models.agent_model import AgentData
from database.agent_db import AgentDB
from database.db_connection import DB_connection

from fastapi import FastAPI


app=FastAPI()


d=DB_connection()  
repo=AgentDB(d)

di={'name':"test","specialty":"test","agent_rank":"Senior"}




# @app.put("/agents/{id}")
# def update(id:int,body:AgentData):
#     return repo.update_agent(id,body)

# @app.get("/agent")
# def get_all():
#     return repo.get_all_agents()



# @app.post("/agent")
# def create(body:AgentData):
#      return repo.create_agent(body)


# print(repo.create_agent(di))

# print(repo.get_agent_by_id(6,di))

# print(repo.get_agent_performance(1))




          