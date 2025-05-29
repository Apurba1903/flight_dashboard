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
    
    
    def fetch_airline_freq(self):
        airline = []
        frequency = []
        
        self.mycursor.execute("""
            SELECT Airline, COUNT(*)
            FROM flightdb
            GROUP BY Airline;
        """)
        
        data = self.mycursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])
        
        return airline, frequency
    
    
    def busy_airport(self):
        city = []
        frequency = []
        
        self.mycursor.execute("""
        SELECT Source, COUNT(*)
            FROM (
                        SELECT Source
                        FROM flightdb
                        UNION ALL
                        SELECT Destination
                        FROM flightdb
            ) t1
            GROUP BY t1.Source
            ORDER BY COUNT(*) DESC;
        """)
        
        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency.append(item[1])
        
        return city, frequency
    
    
    def daily_frequency(self):
        date = []
        frequency = []
        
        self.mycursor.execute("""
            SELECT Date_of_Journey, COUNT(*)
            FROM flightdb
            GROUP BY Date_of_Journey
            ORDER BY Date_of_Journey;
        """)
        
        data = self.mycursor.fetchall()

        for item in data:
            date.append(item[0])
            frequency.append(item[1])
        
        return date, frequency
    
    
    
    
    
    
    