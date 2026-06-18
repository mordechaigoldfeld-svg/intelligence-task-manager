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
    get= repo.get_all_agents()
    if get:
        logger.info("get success")
        return get
    
    logger.error("failed get")
    raise HTTPException(status_code=400,detail="error by get")



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
    if update ==1:
        logger.info(f"success updated id:{id}")
        return {"success":"updated"}
    elif update==2:
        logger.error("id not found")
        raise HTTPException(status_code=404,detail="id not found")
        

    logger.error("not updated")
    raise HTTPException(status_code=400,detail="not updated")






@router.put("/{id}/deactivate")
def daectivate(id:int):
    logger.info(f"trying to deactivate id:{id}")
    agent=repo.get_agent_by_id(id)
    if not agent:
        logger.error("agent not found")
        raise HTTPException(status_code=404,detail="agent not found")
    deact=repo.desactive_agent(id)
    if not deact:
        logger.error("agent alrredy deactivate")
        raise HTTPException(status_code=400,detail=f"id:{id} alrredy deactivate")
    logger.info(f"success deactivate {id}")
    return {"success":"decativate=False"}



@router.get("/{id}/performance")
def get_performance(id:int):
    logger.info("trying to get performance")
    agent=repo.get_agent_by_id(id)
    if not agent:
        logger.error(f"agent :{id} not found")
        raise HTTPException(status_code=404,detail="id not found")
    
    performance=repo.get_agent_performance(id)
    if performance:
        logger.info("success get")
        return performance
    
    logger.error("divide by zero")
    raise HTTPException(status_code=422,detail=f"not missions")