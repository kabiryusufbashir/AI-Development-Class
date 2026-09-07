import numpy as np

transactions = np.array([
    399400, 399380, 78900, 400, 220, 340, 98990, 560000, 2030, 8900, 750, 20230, 8830, 8980, 8568, 2342, 1243, 8920, 9309
])

transactions_mean = np.mean(transactions)
transactions_median = np.median(transactions)
transactions_std = np.std(transactions)
transactions_above_mean = transactions[transactions > transactions_mean]
transactions_above_100000 = transactions[transactions > 100000]
transactions_percentage_of_high_value = (transactions_above_100000.size / transactions.size) * 100

print("Transactions:", transactions)
print("Mean of transactions:", transactions_mean)   
print("Median of transactions:", transactions_median)
print("Standard deviation of transactions:", transactions_std)
print("Transactions above mean:", transactions_above_mean)
print("Transactions above 100,000:", transactions_above_100000)
print("Percentage of transactions above 100,000:", transactions_percentage_of_high_value, "%")