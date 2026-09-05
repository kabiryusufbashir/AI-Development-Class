import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [10, 20], 
    [30, 40]
])

# print(A + B) # Element-wise addition
# print(A * B) # Element-wise multiplication
print( A @ B ) # Matrix multiplication