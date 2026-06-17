from models.agent_model import AgentData
from database.agent_db import AgentDB
from database.db_connection import DB_connection
from database.mission_db import MisssionDB
from models.mission_model import MissionsData

# print(repo.create_agent(di))

# print(repo.get_agent_by_id(6,di))

# print(repo.get_agent_performance(1))


# print(mrepo.get_mission_by_id(1))


print(mrepo.count_by_status("test"))

          