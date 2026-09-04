import logging
import sqlite3

logger=logging.getLogger("SecurityLoggger")

def authenticate_user(user_input_name, user_input_pwd):
    conn=sqlite3.connect(":memory:")
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE users (id INT, username TEXT, pwd_hash TEXT);")
    cursor.execute("INSERT INTO users VALUES (1, 'jocelyn_mariadb', '2149c41b7f0342bb80e8a14f1d3c2ce6dac53fff7032962ac3882da006bf782b');")
    illegal_chars=["'", "--", ";", "OR", "SELECT"]
    has_injection_attempt=any(
        char in user_input_pwd or char in user_input_name for char in illegal_chars
    )
    if has_injection_attempt:
        logger.warning(f"SQL Injection Attempt Detected! User: {user_input_name}, Input: {user_input_pwd}"f"SQL Injection Attempt Detected! User: {user_input_name}, Input: {user_input_pwd}")
    query="SELECT*FROM users WHERE username=? AND pwd_hash=?"
    cursor.execute(query, (user_input_name, user_input_pwd))
    results=cursor.fetchall()

    conn.close()
    return results
