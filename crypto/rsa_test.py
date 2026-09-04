p=2305843009213693951
q=618970019642690137449562111
n=p*q
phi=(p-1)*(q-1)
e=65537
d=pow(e, -1, phi)

def rsa_encrypt(text_msg):
    bytes_msg=text_msg.encode('utf-8')
    int_msg=int.from_bytes(bytes_msg, 'big')
    C_int=pow(int_msg, e, n)
    return C_int

def rsa_decrypt(C_int):
    decrypted_int=pow(C_int, d, n)
    byte_len=(decrypted_int.bit_length()+7)//8
    decrypted_bytes=decrypted_int.to_bytes(byte_len, 'big')
    return decrypted_bytes.decode("utf-8")
