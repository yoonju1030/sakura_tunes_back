import pymysql as my
import dotenv
import os

dotenv.load_dotenv()

class DBUtils():
    def __init__(self):
        self.connection = my.connect(
            host = os.getenv("DB_HOST"), 
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),  
            database = os.getenv("DB_DATABASE"),
            cursorclass = my.cursors.DictCursor 
        )
        self.cursor = self.connection.cursor()
    
    def query(self, sql, params):
        try:
            self.cursor.execute(sql, params)
            row = self.cursor.fetchone()
            return row
        except Exception as e:
            print(e)

