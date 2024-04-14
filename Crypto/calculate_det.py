import numpy as np

v = [[6, 2, -3], [5, 1, 4], [2, 7, 1]]
det = np.linalg.det(np.array(v))
print(abs(round(det)))