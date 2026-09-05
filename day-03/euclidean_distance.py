import numpy as np

a = np.array([1, 2, 3])
b = np.array([1, 2, 3])

distance = np.linalg.norm(a - b)
print("Euclidean distance:", distance)