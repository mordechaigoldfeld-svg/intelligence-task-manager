from database.db_connection import DB_connection
from models.agent_model import AgentData


class MisssionDB:
    def __init__(self,db:DB_connection):
        self.db=db
    
    def create_mission(self,data:AgentData):
        try:
            connection=self.db.get_connection()
            cursor=self.db.connection.cursor(dictionary=True)
            cursor.execute("insert into missions(name,specialty,agent_rank) values (%s,%s,%s);",(body.name,body.specialty,body.agent_rank))
            connection.commit()
            
            agent_id=cursor.lastrowid
            
            cursor.execute("select * from missions where id=%s;",(agent_id,))
            
            agent=cursor.fetchone()
            
            return agent
        except Exception as e:
            return {"error":f"{e}"}
        
        
        
           
    def get_all_missions(self):
        connection=self.db.get_connection()
        cursor=self.db.connection.cursor(dictionary=True)
        cursor.execute("select * from missions;")
        return cursor.fetchall()
    
    
    
    def get_mission_by_id(self,id:int):
        connection =self.db.get_connection()
        cursor=self.db.connection.cursor(dictionary=True)
        cursor.execute("select * from missions where id =%s;",(id,))
       
        return cursor.fetchone()
    
    
    
 