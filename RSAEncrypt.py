#RSA Encrypt
file=open("keys.txt","r")
keys = file.readlines()
file.close()
k=keys[0]
k=k[12:]
k=k.split(",")
e=int(k[0])
n=int(k[1])
def encrypt_block(m):
    c = modinv(m**e, n)
    return c
def encrypt_string(s):
    return ''.join([chr(encrypt_block(ord(x))) for x in list(s)])
def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1
s = input("Enter a message to encrypt: ")
print("\nPlain message: " + s + "\n")
enc = encrypt_string(s)
file2 = open("encrypted.txt","wb")
file2.write(enc.encode('utf-8'))
file2.close()
print("Encrypted message: " + enc + "\n")
