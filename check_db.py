import sqlite3
import hashlib
import os

print("=" * 60)
print("检查数据库用户")
print("=" * 60)

# 检查 users.db 是否存在
if os.path.exists('users.db'):
    print("\n找到 users.db")
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # 查看所有用户
    cursor.execute("SELECT username, pwd_hash FROM users")
    users = cursor.fetchall()
    
    if users:
        print(f"\n数据库中的用户 ({len(users)} 个):")
        for username, pwd_hash in users:
            print(f"\n  用户名: {username}")
            print(f"  哈希值: {pwd_hash}")
            
            # 尝试识别密码
            common = {
                'password123': hashlib.sha256(b'password123').hexdigest(),
                'admin123': hashlib.sha256(b'admin123').hexdigest(),
                'test123': hashlib.sha256(b'test123').hexdigest(),
            }
            for pwd, hash_val in common.items():
                if hash_val == pwd_hash:
                    print(f"  ✅ 密码是: {pwd}")
    else:
        print("\n❌ 数据库中没有用户")
else:
    print("\n❌ users.db 不存在")
    print("   因为 sqli_test.py 使用的是内存数据库 (:memory:)")
    print("   所以每次请求都会重新创建数据库")

print("\n" + "=" * 60)
