#RSA KeyGen
import random
def pri():
        temprim=int((random.choice(list(open('prims.txt')))))
        return temprim
def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a
def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1
def coprimes(a):
    l = []
    for x in range(2, a):
        if gcd(a, x) == 1 and modinv(x,phi) != None:
            l.append(x)
    for x in l:
        if x == modinv(x,phi):
            l.remove(x)
    return l
def encrypt_block(m):
    c = modinv(m**e, n)
    return c
def decrypt_block(c):
    m = modinv(c**d, n)
    return m
def encrypt_string(s):
    return ''.join([chr(encrypt_block(ord(x))) for x in list(s)])
def decrypt_string(s):
    return ''.join([chr(decrypt_block(ord(x))) for x in list(s)])
p=pri()
q=pri()
print("p: "+str(p)+", q: "+str(q))
phi=(p-1)*(q-1)
print("phi: "+str(phi))
n=p*q
print("n: "+str(n))
cop = coprimes(phi)
print(cop)
e=random.choice(cop)
print("e: "+str(e))
d=modinv(e,phi)
print("pub: "+str(e)+","+str(p*q))
print("prv: "+str(d)+","+str(p*q))
file = open("keys.txt","w")
file.write("""Public Key: """+str(e)+","+str(p*q)+"""
Private Key: """+str(d)+","+str(p*q))
file.close()
