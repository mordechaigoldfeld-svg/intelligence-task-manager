from fastapi import APIRouter,HTTPException
from log_config import logger
from database.agent_db import AgentDB
from database.mission_db import MisssionDB
from database.db_connection import DB_connection


db=DB_connection()

a_repo=AgentDB(db)
m_repo=MisssionDB(db)


router=APIRouter(prefix="/reports",tags=["reports"])

@router.get("/summary")
def get_sumary():
    pass


@router.get("/missions-by-status")
def get_missions_status():
    logger.info("trying to get status")
    lis=m_repo.count_by_status("open"),m_repo.count_by_status("in_progress"),m_repo.count_by_status("completed"),m_repo.count_by_status("failed"),m_repo.count_by_status("assigned ")
    if lis:
        logger.info("success get")
        return lis
    logger.error("failed get")
    raise HTTPException(status_code=422,detail="ceck your sintax")
    




@router.get("/top-agent")
def get_top_agent():
    logger.info("try to get top agent")
    get=m_repo.get_top_agent()
    if get:
        logger.info("succes get")
        return get
    logger.error("failed to get")
    
    raise HTTPException(status_code=422,detail="check your sintax")


