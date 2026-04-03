import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (no database selected)
        mydb = mysql.connector.connect(
            host="localhost",
            port=3307,
            user="root",
            password=""
        )
        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE IF NOT EXISTS medical_chatbot_db")
        print("Database 'medical_chatbot_db' created or already exists.")
        
        mydb.close()
    except Exception as e:
        print(f"Error creating database: {e}")

if __name__ == "__main__":
    create_database()
