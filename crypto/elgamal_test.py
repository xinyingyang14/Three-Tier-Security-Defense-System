import secrets

def elgamal_encrypt(p: int, g: int, y: int, M: int)->tuple[int, int]:
    if M>=p:
        raise ValueError("M needs to smaller than p!")
    k=secrets.randbelow(p-2)+2
    C1=pow(g, k, p)
    C2=(M*pow(y, k ,p))%p
    return C1, C2
def elgamal_decrypt(p: int, x: int, C1: int, C2: int)->int:
    mask_inverse=pow(C1, p-1-x, p)
    return (C2*mask_inverse)%p
if __name__=="__main__":
    p, g, x=23, 5, 4
    y=pow(g, x, p)
    original_M=10
    C1_1, C2_1=elgamal_encrypt(p, g, y, original_M)
    dec1=elgamal_decrypt(p, x, C1_1, C2_1)
    print(C1_1, C2_1)
    C1_2, C2_2=elgamal_encrypt(p, g, y, original_M)
    dec2=elgamal_decrypt(p, x, C1_2, C2_2)
    is_ciphertext_different=(C1_1, C2_1)!=(C1_2, C2_2)
    is_decrypted_correct=(dec1==original_M)and(dec2==original_M)
    print("Success" if is_ciphertext_different else "Failed")
    print("Success" if is_decrypted_correct else "Failed")
