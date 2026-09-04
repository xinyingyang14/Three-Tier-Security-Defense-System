from flask import Flask, request
from auth.totp import verify_totp_token
from database.sqli_test import authenticate_user
from crypto.rsa_test import rsa_decrypt

app=Flask(__name__)

MY_SECRET="JocelynsSuperSecretKey123"

failed_attempts={}
MAX_ATTEMPTS=3

@app.route('/', methods=['GET'])

def home():
    with open('index.html', 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/login', methods=['POST'])

def login():
    username=request.form.get('username')
    password=request.form.get('password')
    otp_code=request.form.get('otp_code')
    user_failed_count=failed_attempts.get(username, 0)
    if user_failed_count>=MAX_ATTEMPTS:
        print(f"\033[91m[Log] Blocked login attempt for {username} (Exceeded max attempts)\033[0m")
        return "Account temporarily locked due to too many failed attempts.", 403
    decrypted_password=password
    print(f"[Debug] Using password directly")
    is_otp_correct=verify_totp_token(MY_SECRET, otp_code, window=2)
    print(f"[Log] Try to login-user:{username}, Input OTP:{otp_code}, Server Valid OTP:{is_otp_correct}")
    db_results=authenticate_user(username, decrypted_password)
    is_pwd_correct=bool(db_results)
    if not (is_pwd_correct and is_otp_correct):
        failed_attempts[username]=user_failed_count+1
        print(f"[Log] Failed login for {username}. Total failures: {failed_attempts[username]}")
        return "Wrong password, username or OTP code!", 403
    failed_attempts[username]=0
    print(f"[Log] Successful login for {username}")
    return f"<h1> Welcome!{username} </h1>"
    
if __name__=='__main__':
    app.run(port=5000, debug=True)
