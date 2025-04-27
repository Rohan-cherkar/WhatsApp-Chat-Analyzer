import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",         # change if needed
        password="Ron#12344567",         # your MySQL password
        database="telecom_db"
    )
