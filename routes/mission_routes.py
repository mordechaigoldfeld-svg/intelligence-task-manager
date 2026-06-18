from fastapi import APIRouter,HTTPException
from database.mission_db import MisssionDB
from models.mission_model import MissionsData
from database.db_connection import DB_connection
from log_config import logger


router=APIRouter(prefix="/missions",tags=["missions"])

db=DB_connection()
repo=MisssionDB(db)



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
    logger.info("succes get")
    return repo.get_all_missions()



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
def assingn_toagent():
    pass


@router.put("/{id}/start")
def start_mission(id):
    logger.info("trying to start a mission")
    


@router.put("/{id}/complete")
def completed_mission(id):
    pass


@router.put("/{id}/fail")
def failed_mission(id):
    pass

@router.put("/{id}/cancel")
def cancel(id):
    pass
