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
        cursor.execute("select count(*) as %s from missions where status=%s;",(f"{status}",status))
        return cursor.fetchone()
        
    
    
    def count_open_missions(self):
        connection=self.db.get_connection()
        cursor=self.db.connection.cursor(dictionary=True)
        cursor.execute("select count(*) as IN_PROGRESS from missions where status='IN_PROGRESS';")
        progress=cursor.fetchone()["IN_PROGRESS"]
        cursor.execute("select count(*) as ASSIGNED from missions where status='ASSIGNED';")
        assigned=cursor.fetchone()["ASSIGNED"]
        return {"open missions":progress+assigned}
    
    
    def count_critical_missions(self):
        connection=self.db.get_connection()
        cursor=self.db.connection.cursor(dictionary=True)
        cursor.execute("select count(*) as critical_missions from missions where risk_level='critical';")
        return cursor.fetchone()
    
    
    def get_top_agent(self):
        connection=self.db.get_connection()
        cursor=self.db.connection.cursor(dictionary=True)
        cursor.execute("select assigned_agent_id as agent_id,count(*) as completed_missions from missions group by assigned_agent_id order by completed_missions desc limit 1")
        return cursor.fetchone()
    
 
 
 
 
    
    # def create_mission(self,data:MissionsData):
    #     try:
    #         connection=self.db.get_connection()
    #         cursor=self.db.connection.cursor(dictionary=True)
            
            
    #         first_data=data.model_dump()
            
    #         difficulty=first_data["difficulty"]
    #         importance=first_data["importance"]
            
    #         risk_level_num=(difficulty*2)+importance
            
    #         # if risk_level_num>1 and risk_level<=9:
    #         #     risk_level="LOW"
    #         # elif risk_level_num >9 and risk_level_num<=17:
    #         #     risk_level="MEDIUM"
    #         # elif risk_level_num >18 and risk_level_num<=24:
    #         #     risk_level="HIGH" 
    #         # else:
    #         #     risk_level="CRITICAL"
            
    #         first_data["risk_level"]=risk_level
            
            
    #         # cursor.execute("insert into missions(title,description,location,difficulty,importance,status,risk_level) values (%s,%s,%s,%s,%s,%s,%s);",(first_data["title"],first_data["description"],first_data["location"],first_data["difficulty"],first_data["importance"],first_data["status"],first_data["risk_level"]))
    #         # connection.commit()
            
    #         # agent_id=cursor.lastrowid
            
    #         # cursor.execute("select * from missions where id=%s;",(agent_id,))
            
    #         # agent=cursor.fetchone()
            
    #         return first_data
    #     except Exception as e:
    #         return {"error":f"{e}"}
        