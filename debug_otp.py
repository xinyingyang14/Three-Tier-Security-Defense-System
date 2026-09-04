from auth.totp import get_totp_token, verify_totp_token
import time

MY_SECRET = "JocelynsSuperSecretKey123"

print("=" * 60)
print("TOTP 调试信息")
print("=" * 60)

# 当前 OTP
current = get_totp_token(MY_SECRET)
print(f"\n当前服务器 OTP: {current}")

# 显示时间窗口内的所有 OTP
now = time.time()
print(f"\n时间窗口内的所有 OTP (window=5):")
print("-" * 40)
for i in range(-5, 6):
    target_time = now + (i * 30)
    otp = get_totp_token(MY_SECRET, custom_time=target_time)
    print(f"  {i*30:3d}秒: {otp}")

# 测试您输入的 OTP
print(f"\n您输入的 OTP: 944001")
result = verify_totp_token(MY_SECRET, "944001", window=5)
print(f"验证结果: {result}")

# 检查是否在某个时间窗口匹配
print(f"\n检查 944001 在哪个时间窗口:")
for i in range(-5, 6):
    target_time = now + (i * 30)
    otp = get_totp_token(MY_SECRET, custom_time=target_time)
    if otp == "944001":
        print(f"  ✅ 匹配! 时间偏移: {i*30}秒")
        break
else:
    print(f"  ❌ 没有匹配")
