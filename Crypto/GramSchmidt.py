import math
import numpy as np 

def compute_size_square(myVector):
  ans = 0
  for u in myVector:
    ans += u*u
  return ans

def multiply_vector(v1, v2):
  return np.dot(v1, v2)

def subtract(v1, v2, hs2):
  for i in range(len(v1)):
    v1[i] -= v2[i] * hs2
  return v1
v = []
v.append([4, 1, 3, -1])
v.append([2, 1, -3, 4])
v.append([1, 0, -2, 7])
v.append([6, 2, 9, -5])

u = []
u.append(v[0])
for i in range(1, 4):
  u.append(v[i])
  tmp = []
  for j in range(i):
    tmp = multiply_vector(v[i], u[j]) / compute_size_square(u[j])
    u[i] = subtract(u[i], u[j], tmp)

print(f"{u[3][1]:.5f}")

