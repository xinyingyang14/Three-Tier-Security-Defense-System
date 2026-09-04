import secrets

p=23
g=5
x=secrets.randbelow(p)
y=pow(g, x, p)
print(x)
print(p, g, y)
