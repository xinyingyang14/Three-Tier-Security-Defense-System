import time
import hmac
import hashlib
import struct

def get_totp_token(secret_key, custom_time=None):
    current_time = time.time() if custom_time is None else custom_time
    steps=int(current_time//30)
    key_bytes = secret_key.encode('utf-8')
    msg=struct.pack(">Q", steps)
    hmac_result=hmac.new(key_bytes, msg, hashlib.sha1).digest()
    offset=hmac_result[-1]&0x0f
    binary=((hmac_result[offset]&0x7f)<<24|(hmac_result[offset+1]&0xff)<<16|(hmac_result[offset+2]&0xff)<<8|(hmac_result[offset+3]&0xff))
    token=binary%1000000
    return f"{token:06d}"
def verify_totp_token(secret_key, user_otp, window=5):
    now=time.time()
    user_otp=str(user_otp).strip()
    for i in range(-window, window+1):
        target_time=now+(i*30)
        valid_otp=get_totp_token(secret_key, custom_time=target_time)
        if user_otp==valid_otp:
            return True
    return False
if __name__=="__main__":
    MY_SECRET="JocelynsSuperSecretKey123"
    current_token=get_totp_token(MY_SECRET)
    print("=" * 50)
    print("Jocelyn's Security OTP Generator Tool")
    print("=" * 50)
    print(f"Current OTP: {current_token}")
    print("=" * 50)
    print("Note: Run this script again after 30 seconds to see a brand new token!")
    print("=" * 50)    
