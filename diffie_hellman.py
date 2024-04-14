from factordb.factordb import FactorDB
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD

def get_phi(N):
  f = FactorDB(N)
  f.connect()
  f2 = list(f.get_factor_list())
  f_dict = {}

  phi = 1
  for u in f2:
    if u in f_dict:
      phi *= u
    else:
      f_dict[u] = 1
      phi *= u-1
  return phi

print(get_phi(get_phi(28151)))