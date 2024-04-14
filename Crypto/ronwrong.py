from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from factordb.factordb import FactorDB
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD

with open("/keys_and_messages/21.pem", "r") as f:
    n = RSA.importKey(f.read()).n
    print(n)
# e = 65537
# c = "249d72cd1d287b1a15a3881f2bff5788bc4bf62c789f2df44d88aae805b54c9a94b8944c0ba798f70062b66160fee312b98879f1dd5d17b33095feb3c5830d28"
# f = FactorDB(n)
# f.connect()
# f2 = list(f.get_factor_list())
# p = f2[0]
# q = f2[1]

# phi = (p - 1) * (q - 1)

# d = inverse(e, phi)

# key = RSA.construct((n, e, d))
# cipher = PKCS1_OAEP.new(key)

# F = long_to_bytes(int(c, 16))
# flag = cipher.decrypt(F)
# print(flag)