import sqlite3
import hashlib

DB_FILE = 'users.db'

# 1. 查看数据库实际内容
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
print("=== 数据库内容 ===")
for row in cursor.fetchall():
    print(f"ID: {row[0]}, 用户名: {row[1]}, 哈希: {row[2]}")

# 2. 计算 123456 的哈希
hash_123456 = hashlib.sha256('123456'.encode()).hexdigest()
print(f"\n123456 的哈希: {hash_123456}")

# 3. 手动查询
cursor.execute("SELECT * FROM users WHERE username=? AND pwd_hash=?", 
               ('jocelyn_mariadb', hash_123456))
result = cursor.fetchall()
print(f"手动查询结果: {result}")

# 4. 查看数据库中存储的哈希
cursor.execute("SELECT pwd_hash FROM users WHERE username='jocelyn_mariadb'")
stored_hash = cursor.fetchone()
print(f"数据库中存储的哈希: {stored_hash[0] if stored_hash else '无'}")

# 5. 比较
if stored_hash:
    print(f"哈希匹配: {stored_hash[0] == hash_123456}")

conn.close()
