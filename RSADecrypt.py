#RSA Decrypt
file=open("keys.txt","r")
keys = file.readlines()
file.close()
k=keys[1]
k=k[12:]
k=k.split(",")
d=int(k[0])
n=int(k[1])
def decrypt_block(c):
    m = modinv(c**d, n)
    return m
def decrypt_string(s):
    return ''.join([chr(decrypt_block(ord(x))) for x in list(s)])
def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1
file2=open("encrypted.txt","rb")
enc = file2.read().decode('utf-8')
file2.close()
print(str(enc))
dec = decrypt_string(enc)
print("Decrypted message: " + dec + "\n")
file3=open("decrypted.txt","w")
file3.write(dec)
file3.close()
