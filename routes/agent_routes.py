from fastapi import APIRouter,HTTPException
from database.agent_db import AgentDB
from models.agent_model import AgentData
from database.db_connection import DB_connection
from log_config import logger

router=APIRouter(prefix="/agents",tags=["agents"])


db=DB_connection()
repo=AgentDB(db)


@router.post("/")
def create_agent(body:AgentData):
    logger.info("trying to create a new agent")
    create=repo.create_agent(body)
    if create:
        logger.info("success created")
        return create
    logger.error("not created")
    raise HTTPException(status_code=400,detail="not created")




@router.get("/")
def get_all():
    logger.info("trying to get all")
    return repo.get_all_agents()



@router.get("/{id}")
def get_by_id(id:int):
    logger.info("trying to get by id")
    get= repo.get_agent_by_id(id)
    if not get:
        logger.error("id not found")
        raise HTTPException(status_code=404,detail=f"id:{id} not found")
    logger.info("succes get")
    return get


@router.put("/{id}")
def update_agent(id:int,body:AgentData):
    logger.info(f"trying to update id:{id}")
    update=repo.update_agent_by_id(id,body)
    if update >=1:
        logger.info(f"success updated id:{id}")
        return {"success":"updated"}
    
    logger.error("not updated")
    raise HTTPException(status_code=400,detail="not updated")






@router.put("/{id}/deactivate")
def daectivate(id:int):
    logger.info(f"trying to deactivate id:{id}")
    deact=repo.desactive_agent(id)
    if not deact:
        logger.error("id not found")
        raise HTTPException(status_code=404,detail=f"id:{id} not found or alrredy deactivate")
    logger.info(f"success deactivate {id}")
    return {"success":"decativate"}



@router.get("/{id}/performance")
def get_performance(id:int):
    logger.info("trying to get performance")
    performance=repo.get_agent_performance(id)
    if performance:
        logger.info("success get")
        return performance
    
    logger.error("id not found")
    raise HTTPException(status_code=404,detail=f"{id} not found")