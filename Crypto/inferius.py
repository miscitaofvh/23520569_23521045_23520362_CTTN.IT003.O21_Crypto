n = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373

from factordb.factordb import FactorDB
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD
f = FactorDB(n)
f.connect()
f2 = list(f.get_factor_list())

phi = (f2[0]-1)*(f2[1]-1)
d = inverse(e, phi)
# ct = pt^e mod n -> ct ^ d = pt mod n
intFLAG = pow(ct, d, n)
print(intFLAG)
print(long_to_bytes(intFLAG))