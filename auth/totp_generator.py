import time
import hmac
import hashlib

def generate_totp_token(secret_key):
    current_time=int(time.time())
    time_step=current_time//30
    counter_bytes=time_step.to_bytes(8, byteorder='big')
    key_bytes=secret_key.encode('utf-8')
    hmac_result=hmac.new(key_bytes, counter_bytes, hashlib.sha1).digest()
    last_byte=hmac_result[-1]
    offset=last_byte&0x0f
    bin_code=((hmac_result[offset]&0x7f)<<24|(hmac_result[offset+1]&0xff)<<16|(hmac_result[offset+2]&0xff)<<8|(hmac_result[offset+3]&0xff))
    token=bin_code%1000000
    return token, current_time
def main():
    SECRET="JOCELYN_SECURITY_KEY"
    print("=========================================")
    print("  🚀 TOTP Real-time Generator Running... ")
    print("  Hint: Press Ctrl + C to stop the program ")
    print("=========================================")
    try:
        while True:
            token, now=generate_totp_token(SECRET)
            time_str=time.strftime('%H:%M:%S', time.localtime(now))
            print(f"[{time_str}] Current Dynamic Password: {token:06d}")
            time.sleep(30)
    except KeyboardInterrupt:
        print("\n=== Program terminated safely. Good job! ===")
if __name__=="__main__":
    main()
