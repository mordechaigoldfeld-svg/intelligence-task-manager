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
            create=cursor.rowcount
            if create>=1:
                agent_id=cursor.lastrowid
                
                cursor.execute("select * from agents where id=%s;",(agent_id,))
                
                agent=cursor.fetchone()
            
                return agent
            return None
            
        except Exception as e:
            return {"error":f"{e}"}
        
        
        
           
    def get_all_agents(self):
        try:
            connection=self.db.get_connection()
            cursor=self.db.connection.cursor(dictionary=True)
            cursor.execute("select * from agents;")
            return cursor.fetchall()
        except Exception as e:
            return {"error":f"{e}"},0
    
    
    
    def get_agent_by_id(self,id:int):
        connection =self.db.get_connection()
        cursor=self.db.connection.cursor(dictionary=True)
        cursor.execute("select * from agents where id =%s;",(id,))
       
        return cursor.fetchone()
    
    
    
    def update_agent_by_id(self,id,body:AgentData):
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
        if perform[0]:
            return perform
        return None
        
        
    
    def count_active_agents(self):
        connection=self.db.get_connection()
        cursor=self.db.connection.cursor(dictionary=True)
        cursor.execute("select count(*) as total_active from agents where is_active=1; ")
        return cursor.fetchone()
    
    
    
    def get_agent_performance(self,id:int):
        connection=self.db.get_connection()
        cursor=self.db.connection.cursor(dictionary=True)
        cursor.execute("select failed_missions,completed_missions from agents where id=%s;",(id,))
        first_data = cursor.fetchone()
        
        # cursor.execute("select failed_missions+completed_missions as total_missions from agents where id=%s;",(id,))
        # perform.append(cursor.fetchone())
        return first_data
        # if perform[0]:
        #     return perform
        # return None
        
    

    


            

















# d=DB_connection()  

# print(AgentDB.create_agent({"name":"test","specialty":"test","agent_rank":"Junior"}))          