from db_connection import connect

def add_customer(name, phone, address):
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO customers (name, phone, address) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, phone, address))
    conn.commit()
    conn.close()
