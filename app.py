import os
import sqlite3

# 1. Security issue: hardcoded password & string-interpolated query (SQL injection vulnerability)
DB_PASSWORD = "super_secret_password_123"

def process_user_data(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)
    return cursor.fetchone()

# 2. Performance issue: Database/IO queries executing in a loop (N+1 query problem)
def fetch_batch_details(user_ids):
    details = []
    for uid in user_ids:
        # Query in loop is high latency
        details.append(process_user_data(uid))
    return details

# 3. Test Coverage gap: this helper function has no tests
def untested_helper_method(x):
    return x * 10
