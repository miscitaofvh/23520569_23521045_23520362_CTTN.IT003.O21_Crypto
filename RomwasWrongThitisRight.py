from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from factordb.factordb import FactorDB
from Crypto.Util.number import inverse

with open("21.pem") as f:
    n = RSA.importKey(f.read()).n
with open("21.pem") as f:   
    e = RSA.importKey(f.read()).e

f = FactorDB(n)
f.connect()
f2 = list(f.get_factor_list())
p = f2[0]
q = f2[1]
phi = (p - 1) * (q - 1)
d = inverse(e, phi)

with open("21.ciphertext", "r") as f:
    ciphertext = f.read()

key = RSA.construct((n, e, d))
cipher = PKCS1_OAEP.new(key)
msg = cipher.decrypt(bytes.fromhex(ciphertext))

print(msg)