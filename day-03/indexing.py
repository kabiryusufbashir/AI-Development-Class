import numpy as np

customers = np.array([
    [25, 80000,  10, 0],
    [41, 200000, 45, 1],
    [33, 150000, 22, 0],
    [29, 90000,   7, 1]
])


X = customers[:, :3] # all rows, first three columns

y = customers[:, 3] # all rows, last column

# Boolean Indexing 
amounts = np.array([
    5000,
    150000,
    12000,
    300000
])

suspicious = amounts[
    amounts > 100000
]

print(suspicious)