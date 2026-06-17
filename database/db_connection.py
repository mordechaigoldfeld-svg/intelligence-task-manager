import mysql.connector



class DB_connection():
    def __init__(self):
        self.config={"host":"127.0.0.1",
                     "user":"root",
                     "password":"1234",
                     "database":"Intelligence_db"}
        self.connection=None
        
        
    def get_connection(self):
        if self.connection:
            return self.connection
        
        self.connection=mysql.connector.connect(**self.config)
        
        return self.connection
    
    
    
    def create_database(self):
        connection=self.get_connection()
        cursor=self.connection.cursor(dictionary=True)
        cursor.execute("create database if not exists Intelligence_db;")
        return {"database created or alrredy exists"}
    
    
    
    def create_tables(self):
        connection=self.get_connection()
        cursor=self.connection.cursor(dictionary=True)
        cursor.execute("""create table if not exists agents(
            id int auto_increment primary key,
            name varchar(50) not null,
            specialty varchar(100) not null,
            is_active boolean default True,
            completed_missions int default 0,
            failed_missions int default 0,
            agent_rank enum('Junior','Senior','Commander'));""")
        
        cursor.execute("""create table if not exists missions(
            id int auto_increment primary key,
            title varchar(100) not null,
            description text not null,
            difficulty int not null,
            importance int not null,
            status varchar(50) default 'NEW',
            risk_level varchar(50),
            assigned_agent_id int default 0);""")
        
        
        return {"tables agents and missions are created or alrredy exists"}
    
    
    
    


    