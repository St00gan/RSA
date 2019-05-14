#RSA DESTROYER!!!!!!!
file=open("keys.txt","r")
keys = file.readlines()
file.close()
k=keys[0]
k=k[12:]
k=k.split(",")
e=int(k[0])
n=int(k[1])
file2=open("encrypted.txt","rb")
enc = file2.read().decode('utf-8')
file2.close()
#Quest to find d ;)
#d=modinv(e,phi)
#phi=(p-1)*(q-1)
file = open("prims.txt")
primes = file.readlines()
def crackpq():
    l=[]
    for i in primes:
        for x in primes:
            if int(i)*int(x) == n:
                l.append(i[:-1])
                l.append(x[:-1])
                return l
ck = (crackpq())
p=int(ck[0])
q=int(ck[1])
def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1
phi=(p-1)*(q-1)
d=modinv(e,phi)
def decrypt_block(c):
    m = modinv(c**d, n)
    return m
def decrypt_string(s):
    return ''.join([chr(decrypt_block(ord(x))) for x in list(s)])
dec = decrypt_string(enc)

print("Decrypted message: " + dec + "\n")
