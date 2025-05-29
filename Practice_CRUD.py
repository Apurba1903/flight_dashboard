import os
import mysql.connector
from dotenv import load_dotenv


load_dotenv()


# Hiding Credentials
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')


# Connecting with Database
try:
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    mycursor = conn.cursor()
    print('Connection Established')
except mysql.connector.Error as err:
    print(f'Connection Error: {err}')
except Exception as e:
    print(f'Other Error: {e}')


# Creating Database
try:
    mycursor.execute("CREATE DATABASE IF NOT EXISTS flightdb;")
    conn.commit()
    print("Database 'flightdb' created successfully or already exists")
except mysql.connector.Error as err:
    print(f"Error creating database: {err}")
    conn.rollback()
except Exception as e:
    print(f"Unexpected error: {e}")
    conn.rollback()


# Creating Table
try:
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS airport(
            airport_id INTEGER PRIMARY KEY AUTO_INCREMENT,
            code VARCHAR(10) NOT NULL UNIQUE,
            name VARCHAR(100) NOT NULL,
            city VARCHAR(100) NOT NULL,
            INDEX idx_code (code),
            INDEX idx_city (city)
        );
    """)
    conn.commit()
    print(f"In database '{DB_NAME}', table 'airport' created successfully or already exists")
except mysql.connector.Error as err:
    print(f"MySQL Error creating table: {err}")
    conn.rollback()
except Exception as e:
    print(f"Unexpected error: {e}")
    conn.rollback()


# Insert Data to the Table
try:
    mycursor.execute("""
        INSERT IGNORE INTO airport(airport_id, code, name, city)
        VALUES
        (1, 'DAC', 'Hazrat Shahjalal International Airport', 'Dhaka'), 
        (2, 'COX', "Cox's Bazar Airport", "Cox's Bazar"), 
        (3, 'SYL', 'Osmani International Airport', 'Sylhet');
    """)
    
    rows_affected = mycursor.rowcount
    conn.commit()
    
    if rows_affected > 0:
        print(f"Successfully inserted {rows_affected} new records into 'airport' table")
    else:
        print("No new records inserted (data may already exist)")
        
except mysql.connector.Error as err:
    print(f"MySQL Error inserting data: {err}")
    conn.rollback()
except Exception as e:
    print(f"Unexpected error: {e}")
    conn.rollback()


# Retrieve Data from the Table
try:
    mycursor.execute("""
        SELECT *
        FROM airport
        WHERE airport_id > 1
    """)
    data = mycursor.fetchall()
    print("All data:")
    print(data)
    
    print("\nAirport names:")
    for row in data:
        print(row[2])
        
except mysql.connector.Error as err:
    print(f"Error fetching data: {err}")
except Exception as e:
    print(f"Unexpected error: {e}")


# Update Data from the Table
try:
    mycursor.execute("""
        UPDATE airport
        SET name = 'Sylhet International Airport'
        WHERE airport_id = 3
    """)
    
    rows_affected = mycursor.rowcount
    conn.commit()
    
    if rows_affected > 0:
        print(f"Successfully updated {rows_affected} record(s)")
    else:
        print("No records were updated (airport_id = 3 might not exist)")
        
except mysql.connector.Error as err:
    print(f"MySQL Error updating data: {err}")
    conn.rollback()
except Exception as e:
    print(f"Unexpected error: {e}")
    conn.rollback()


# # Retrieve Data from the Table to check the Update
# try:
#     mycursor.execute("""
#         SELECT *
#         FROM airport
#     """)
#     data = mycursor.fetchall()
#     print("All data:")
#     print(data)
    
#     print("\nAirport names:")
#     for row in data:
#         print(row[2])
        
# except mysql.connector.Error as err:
#     print(f"Error fetching data: {err}")
# except Exception as e:
#     print(f"Unexpected error: {e}")


# Delete Data from the Table
try:
    mycursor.execute("""
        DELETE FROM airport
        WHERE airport_id = 3
    """)
    
    rows_affected = mycursor.rowcount
    conn.commit()
    
    if rows_affected > 0:
        print(f"Successfully deleted {rows_affected} record(s)")
    else:
        print("No records were deleted (airport_id = 3 might not exist)")
        
except mysql.connector.Error as err:
    print(f"MySQL Error deleting data: {err}")
    conn.rollback()
except Exception as e:
    print(f"Unexpected error: {e}")
    conn.rollback()


# # Retrieve Data from the Table to check the Delete
# try:
#     mycursor.execute("""
#         SELECT *
#         FROM airport
#     """)
#     data = mycursor.fetchall()
#     print("All data:")
#     print(data)
    
#     print("\nAirport names:")
#     for row in data:
#         print(row[2])
        
# except mysql.connector.Error as err:
#     print(f"Error fetching data: {err}")
# except Exception as e:
#     print(f"Unexpected error: {e}")
    
    