from db_connection import connect
from datetime import date

def generate_bill(customer_id, call_minutes, sms_count, data_usage):
    rate_call = 0.5
    rate_sms = 0.2
    rate_data = 1.0

    total = (call_minutes * rate_call) + (sms_count * rate_sms) + (data_usage * rate_data)

    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO bills (customer_id, call_minutes, sms_count, data_usage, bill_date, amount) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (customer_id, call_minutes, sms_count, data_usage, date.today(), total))
    conn.commit()
    conn.close()
    return total

