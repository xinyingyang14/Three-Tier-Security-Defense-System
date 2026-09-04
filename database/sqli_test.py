import logging
import sqlite3
import hashlib
import os

logger = logging.getLogger("SecurityLoggger")

DB_FILE = 'users.db'

def authenticate_user(user_input_name, user_input_pwd):
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE users (id INT, username TEXT, pwd_hash TEXT);")
        pwd_hash = hashlib.sha256('123456'.encode()).hexdigest()
        cursor.execute("INSERT INTO users VALUES (1, 'jocelyn_mariadb', ?);", (pwd_hash,))
        cursor.execute("INSERT INTO users VALUES (2, 'admin', ?);", (hashlib.sha256('admin123'.encode()).hexdigest(),))
        conn.commit()
        conn.close()
        print(f"[DB] Database initialized: {DB_FILE}")
    
    illegal_chars = ["'", "--", ";", "OR", "SELECT"]
    has_injection_attempt = any(
        char in user_input_pwd or char in user_input_name for char in illegal_chars
    )
    if has_injection_attempt:
        logger.warning(f"SQL Injection Attempt Detected! User: {user_input_name}")
        return []
    
    pwd_hash = hashlib.sha256(user_input_pwd.encode()).hexdigest()
    
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username=? AND pwd_hash=?"
    cursor.execute(query, (user_input_name, pwd_hash))
    results = cursor.fetchall()
    conn.close()
    return results
