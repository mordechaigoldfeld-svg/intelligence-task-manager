from fastapi import APIRouter,HTTPException
from database.mission_db import MisssionDB
from database.agent_db import AgentDB
from models.mission_model import MissionsData
from database.db_connection import DB_connection
from log_config import logger


router=APIRouter(prefix="/missions",tags=["missions"])

db=DB_connection()
repo=MisssionDB(db)
arepo=AgentDB(db)



@router.post("/")
def create_mission(body:MissionsData):
    logger.info("trying to create a new mission")
    create=repo.create_mission(body)
    if create:
        logger.info("success created")
        return create
    logger.error("not created")
    raise HTTPException(status_code=400,detail="not created")




@router.get("/")
def get_all_missions():
    logger.info("triyng to get all missions")
    get=repo.get_all_missions()
    if get:
        logger.info("succes get")
        return get
    logger.error("failed get")
    raise HTTPException(status_code=400,detail="failed get")
    
     
    


@router.get("/{id}")
def get_mission_by_id(id:int):
    logger.info(f"trying to get id :{id}")
    get=repo.get_mission_by_id(id)
    if get:
        logger.info("success get")
        return get
    logger.error("id not found")
    raise HTTPException(status_code=404,detail=f"id:{id} not found")
    



@router.put("/{id}/assign/{agent_id}")
def assingn_to_agent(id,agent_id,status="assigned"):
    logger.info("trying to assing mission")
    agent=arepo.get_agent_by_id(agent_id)
    if not agent:
        logger.error("agent not found")
        raise HTTPException(status_code=404,detail="agent not found")


@router.put("/{id}/start")
def start_mission(id):
    logger.info("trying to start a mission")
    status=repo.get_mission_by_id(id)
    if not status:
        logger.error("mission not found")
        raise HTTPException(status_code=404,detail="mission not found")
    if status["status"]!="assigned":
        logger.error("you cant start if not assigned")
        raise HTTPException(status_code=404,detail="you cant start if not assigned")
    repo.update_mission_status(id,"in_progress")
    
    logger.info("succes start")
    return {"success"}
        
    


@router.put("/{id}/complete")
def completed_mission(id):
    logger.info("trying to complet a mission")
    status=repo.get_mission_by_id(id)
    if not status:
        logger.error("mission not found")
        raise HTTPException(status_code=404,detail="mission not found")
    if status["status"]!="in_progress":
        logger.error("you cant start if not assigned")
        raise HTTPException(status_code=404,detail="you cant complet if not in_progress")
    repo.update_mission_status(id,"completed")
    
    logger.info("succes completed")
    return {"success"}
        


@router.put("/{id}/fail")
def failed_mission(id):
    logger.info("trying to failed a mission")
    status=repo.get_mission_by_id(id)
    if not status:
        logger.error("mission not found")
        raise HTTPException(status_code=404,detail="mission not found")
    if status["status"]!="in_progress":
        logger.error("you cant failed if not assigned")
        raise HTTPException(status_code=404,detail="you cant failed if not in_progress")
    repo.update_mission_status(id,"failed")
    
    logger.info("succes failed")
    return {"success":"failed"}

@router.put("/{id}/cancel")
def cancel(id):
    logger.info("trying to cancel a mission")
    status=repo.get_mission_by_id(id)
    if not status:
        logger.error("mission not found")
        raise HTTPException(status_code=404,detail="mission not found")
    if status["status"]!="in_progress":
        logger.error("you cant canceld if not assigned")
        raise HTTPException(status_code=404,detail="you cant canceldd if not in_progress")
    repo.update_mission_status(id,"canceld")
    
    logger.info("succes canceld")
    return {"success":"canceld"}
