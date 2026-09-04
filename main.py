import logging
from auth.totp import get_totp_token, verify_totp_token
from crypto.rsa_test import rsa_decrypt, rsa_encrypt
from database.sqli_test import authenticate_user

logging.basicConfig(
    filename="logs/security.log",
    level=logging.WARNING,
    format="%(asctime)s-[%(levelname)s]-%(message)s",
)
logger=logging.getLogger("SecurityLogger")

def main():
    print("="*60)
    print("🛡️  Three=Tier Security Defense System")
    print("="*60)
    mfa_secret="JocelynSuperSecretKey123"
    raw_username="jocelyn_mariadb"
    sqli_attack_pwd="' OR '1'='1"
    
    print("\n[Step 1] Transport Layer: Executing RSA Asymmetric Encryption...")
    encrypted_cipher=rsa_encrypt(raw_username)
    decrypted_username=rsa_decrypt(encrypted_cipher)
    print(f"🔒 Ciphertext encrypted and transmitted...")
    print(f"🔓 Decryption successful! Restored Username: {decrypted_username}")
    print("\n[Step 2] Database Layer: Parameterized Query & SQLi Detection...")
    db_results=authenticate_user(decrypted_username, sqli_attack_pwd)

    if not db_results:
        print("❌ Authentication Failed: SQL Injection successfully mitigated! (Logged to logs/security.log)")
        print("\n[Step 3] Access Control Layer: Verifying MFA Token...")
        valid_otp=get_totp_token(mfa_secret)
        print(f"📲 Generated current OTP via Mobile App simulator: {valid_otp}")
    
    is_mfa_valid=verify_totp_token(secret_key=mfa_secret, user_otp=valid_otp)
    if is_mfa_valid:
        print("✅ MFA Token Verified Successfully!")
        print("\n🎉 All Security Checks Passed! Login Successful.")
    else:
        logger.warning(f"MFA Verification Failed for user: {decrypted_username}")
        print("❌ MFA Token Invalid or Expired.")

if __name__=="__main__":
    main()
