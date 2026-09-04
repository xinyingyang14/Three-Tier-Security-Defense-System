import secrets

def elgamal_decrypt(p: int, x:int, C1:int, C2:int)->int:
    mask_inverse=pow(C1, p-1-x, p)
    M=(C2*mask_inverse)%p
    return M
if __name__=="__main__":
    p=23
    x=4
    C1=10
    C2=19
    decrypted_M=elgamal_decrypt(p, x, C1, C2)
    print(decrypted_M)
