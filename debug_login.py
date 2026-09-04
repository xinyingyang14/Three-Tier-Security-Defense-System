# debug_login.py
from auth.totp import get_totp_token, verify_totp_token
from database.sqli_test import authenticate_user
from crypto.rsa_test import rsa_decrypt
import time

def debug_all():
    print("=" * 60)
    print("登录调试工具")
    print("=" * 60)
    
    MY_SECRET = "JocelynsSuperSecretKey123"
    
    # 1. 测试 TOTP
    print("\n[1] 测试 TOTP 生成:")
    current_otp = get_totp_token(MY_SECRET)
    print(f"    当前 OTP: {current_otp}")
    
    # 显示时间窗口内的所有 OTP
    now = time.time()
    print(f"\n[2] 时间窗口内的 OTP (window=5):")
    for i in range(-5, 6):
        target_time = now + (i * 30)
        otp = get_totp_token(MY_SECRET, custom_time=target_time)
        print(f"    {i*30:3d}秒: {otp}")
    
    # 2. 测试验证函数
    print(f"\n[3] 测试验证函数:")
    test_otp = input("    请输入要测试的 OTP: ")
    result = verify_totp_token(MY_SECRET, test_otp, window=5)
    print(f"    验证结果: {result}")
    
    # 3. 测试数据库认证
    print(f"\n[4] 测试数据库认证:")
    username = input("    请输入用户名: ")
    password = input("    请输入密码: ")
    
    try:
        # 尝试解密（如果 RSA 失败就使用原始密码）
        try:
            decrypted = rsa_decrypt(password)
            print(f"    密码解密成功: {decrypted}")
        except Exception as e:
            decrypted = password
            print(f"    密码解密失败，使用原始密码: {e}")
        
        result = authenticate_user(username, decrypted)
        print(f"    认证结果: {result}")
        print(f"    认证成功: {bool(result)}")
    except Exception as e:
        print(f"    数据库错误: {e}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    debug_all()
