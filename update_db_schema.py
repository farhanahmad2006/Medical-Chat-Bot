import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# Extract connection details from DATABASE_URL or just usage defaults since we know them
# DATABASE_URL=mysql+mysqlconnector://root:@localhost/medical_chatbot_db

def add_summary_column():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            port=3307,
            user="root",
            password="",
            database="medical_chatbot_db"
        )
        mycursor = mydb.cursor()

        # Check if column exists first to avoid error
        mycursor.execute("SHOW COLUMNS FROM medical_history LIKE 'summary'")
        result = mycursor.fetchone()

        if not result:
            sql = "ALTER TABLE medical_history ADD COLUMN summary TEXT NULL"
            mycursor.execute(sql)
            mydb.commit()
            print("Column 'summary' added successfully.")
        
        mycursor.execute("SHOW COLUMNS FROM medical_history LIKE 'doctors_recommendation'")
        result_docs = mycursor.fetchone()

        if not result_docs:
            sql = "ALTER TABLE medical_history ADD COLUMN doctors_recommendation TEXT NULL"
            mycursor.execute(sql)
            mydb.commit()
            print("Column 'doctors_recommendation' added successfully.")
        else:
            print("Column 'summary' already exists.")

        mydb.close()
    except Exception as e:
        print(f"Error updating database: {e}")

if __name__ == "__main__":
    add_summary_column()
