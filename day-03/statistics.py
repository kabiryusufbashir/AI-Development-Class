import numpy as np

transactions = np.array([
    5000,
    7000,
    8000,
    6000,
    9000,
    250000
])

print("Mean:", np.mean(transactions))
print("Median:", np.median(transactions))   
print("Standard Deviation:", np.std(transactions))
print("Variance:", np.var(transactions))