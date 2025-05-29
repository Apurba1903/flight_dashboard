import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

class DB:
    def __init__(self):
        # Connecting with Database
        self.conn = None
        self.mycursor = None
        try:
            self.conn = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
            )
            self.mycursor = self.conn.cursor()
            print('Connection Established')
        except mysql.connector.Error as err:
            print(f'Connection Error: {err}')
        except Exception as e:
            print(f'Other Error: {e}')
    
    
    def fetch_city_names(self):
        city = []
        
        self.mycursor.execute("""
                SELECT DISTINCT(Source)
                FROM flightdb
                UNION
                SELECT DISTINCT(Destination)
                FROM flightdb
                ORDER BY Source;
            """)
        data = self.mycursor.fetchall()
        
        for item in data:
            city.append(item[0])
        return city
    
    
    def fetch_all_flights(self, source, destination):
        
        try:
            self.mycursor.execute("""
                SELECT Airline, Route, Dep_Time, Duration, Total_Stops, Price
                FROM flightdb
                WHERE Source = %s 
                AND Destination = %s
            """, (source, destination))
            
            data = self.mycursor.fetchall()
            return data
            
        except mysql.connector.Error as err:
            print(f'Database Error in fetch_all_flights: {err}')
            return []
        except Exception as e:
            print(f'Other Error in fetch_all_flights: {e}')
            return []
    
    
    
