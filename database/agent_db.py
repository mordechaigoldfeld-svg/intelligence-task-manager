from database.db_connection import DB_connection
from models.agent_model import AgentData


class AgentDB:
    def __init__(self,db:DB_connection):
        self.db=db
    
    def create_agent(self,body:AgentData):
        try:
            connection=self.db.get_connection()
            cursor=self.db.connection.cursor(dictionary=True)
            cursor.execute("insert into agents(name,specialty,agent_rank) values (%s,%s,%s);",(body.name,body.specialty,body.agent_rank))
            connection.commit()
            
            agent_id=cursor.lastrowid
            
            cursor.execute("select * from agents where id=%s;",(agent_id,))
            
            agent=cursor.fetchone()
            
            return agent
        except Exception as e:
            return {"error":f"{e}"}
        
        
        
           
    def get_all_agents(self):
        connection=self.db.get_connection()
        cursor=self.db.connection.cursor(dictionary=True)
        cursor.execute("select * from agents;")
        return cursor.fetchall()
    
    
    
    def get_agent_by_id(self,id:int):
        connection =self.db.get_connection()
        cursor=self.db.connection.cursor(dictionary=True)
        cursor.execute("select * from agents where id =%s;",(id,))
       
        return cursor.fetchone()
    
    
    
    def update_agent(self,id,body:AgentData):
        connection =self.db.get_connection()
        cursor=self.db.connection.cursor(dictionary=True)
        cursor.execute("update agents set name=%s, specialty=%s , agent_rank=%s ,is_active=False where id=%s;",(body.name,body.specialty,body.agent_rank,id))
        connection.commit()
        return cursor.rowcount
    
    
    
    
    def desactive_agent(self,id:int):
        connection = self.db.get_connection()
        cursor=self.db.connection.cursor(dictionary=True)
        cursor.execute("update agents set is_active=False where id=%s;",(id,))
        connection.commit()
        return cursor.rowcount
    
    
    
    
    def increment_completed(self,id:int):
        connection=self.db.get_connection()
        cursor=self.db.connection.cursor(dictionary=True)
        cursor.execute("update agents set completed_missions=completed_missions+1 where id=%s;",(id,))
        connection.commit()
        return cursor.rowcount
    
    
    
    def increment_failed(self,id:int):
        connection=self.db.get_connection()
        cursor=self.db.connection.cursor(dictionary=True)
        cursor.execute("update agents set failed_missions=failed_missions+1 where id=%s;",(id,))
        connection.commit()
        return cursor.rowcount
    
    
    
    def get_agent_performance(self,id:int):
        connection=self.db.get_connection()
        cursor=self.db.connection.cursor(dictionary=True)
        cursor.execute("select failed_missions,completed_missions from agents where id=%s;",(id,))
        perform = cursor.fetchall()
        cursor.execute("select failed_missions+completed_missions as total_missions from agents where id=%s;",(id,))
        perform.append(cursor.fetchone())
        # return milon
        return perform
        
        
    
    def count_active_agents(self):
        connection=self.db.get_connection()
        cursor=self.db.connection.cursor(dictionary=True)
        cursor.execute("select count(*) as total_active from agents where is_active=1; ")
        return cursor.fetchone()

    


            



# d=DB_connection()  

# print(AgentDB.create_agent({"name":"test","specialty":"test","agent_rank":"Junior"}))          