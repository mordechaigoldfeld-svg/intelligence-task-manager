from models.agent_model import AgentData
from database.agent_db import AgentDB
from database.db_connection import DB_connection
from database.mission_db import MisssionDB
from models.mission_model import MissionsData
from fastapi import FastAPI
from routes.agent_routes import router as agent_router
from routes.mission_routes import router as mission_router
from routes.report_routes import router as reports_router








app=FastAPI()


app.include_router(agent_router)
app.include_router(mission_router)
app.include_router(reports_router)


d=DB_connection()  
repo=AgentDB(d)
mrepo=MisssionDB(d)

# di={'name':"test","specialty":"test","agent_rank":"Senior"}


# @app.post("/missions")
# def create(data:MissionsData):
#     return mrepo.create_mission(data)

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


# print(mrepo.get_mission_by_id(1))

# mrepo.assing_mission_by_id(3,3)
# mrepo.assing_mission_by_id(2,1)

# print(mrepo.get_top_agent())

# print(mrepo.count_by_status("assigned"))



