import secrets

def elgamal_encrypt(p, g, y, M):
    if M>=p:
        raise ValueError("M needs to smaller than p!")
    k = secrets.randbelow(p - 2) + 2
    C1 = pow(g, k, p)
    C2 = (M * pow(y, k, p)) % p
    return C1, C2;

p=23
g=5
y=4
M=10

C1, C2=elgamal_encrypt(p, g, y, M)
print(C1, C2)
