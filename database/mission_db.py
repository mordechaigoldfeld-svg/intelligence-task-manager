from database.db_connection import DB_connection
from models.mission_model import MissionsData


class MisssionDB:
    def __init__(self,db:DB_connection):
        self.db=db
    
    def create_mission(self,data:MissionsData):
        try:
            connection=self.db.get_connection()
            cursor=self.db.connection.cursor(dictionary=True)
            cursor.execute("insert into missions(title,description,location,difficulty,importance,status) values (%s,%s,%s,%s,%s,%s);",(data.title,data.description,data.location,data.difficulty,data.importance,data.status))
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
    
    
    
    def assing_mission_by_id(self,m_id:int,a_id:int):
        connection=self.db.get_connection()
        cursor=self.db.connection.cursor(dictionary=True)
        cursor.execute("update missions set assigned_agent_id=%s where id=%s; ",(a_id,m_id))
        connection.commit()
        return cursor.rowcount
    
    
    
    def update_mission_status(self,id:int,status:str):
        connection=self.db.get_connection()
        cursor=self.db.connection.cursor(dictionary=True)
        cursor.execute("update missions set status=%s where id=%s; ",(status,id))
        connection.commit()
        return cursor.rowcount
    
    def get_open_missions_by_agent(self,id):
        pass
    
    
    
    def count_all_missions(self):
        connection=self.db.get_connection()
        cursor=self.db.connection.cursor(dictionary=True)
        cursor.execute("select count(*) as total_missions from missions;")
        return cursor.fetchone()
    
    
    
    def count_by_status(self,status:str):
        connection=self.db.get_connection()
        cursor=self.db.connection.cursor(dictionary=True)
        cursor.execute("select count(*) as total_status from missions where status=%s;",(status,))
        return cursor.fetchone()
        
    
    
    
    
    
 