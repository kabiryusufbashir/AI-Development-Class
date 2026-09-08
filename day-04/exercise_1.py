import pandas as pd
from pathlib import Path

# __file__ means "this current Python file".
# parent means "the folder that contains this file", which is day-04.
# This makes Python look for:
# day-04/data/transactions.csv
file_path = Path(__file__).parent / "data" / "transactions.csv"

df = pd.read_csv(file_path)

# Failed Transaction 
failed_transaction = df.loc[
    df["status"] == "failed"
]

print(f"The failed Transaction count is {len(failed_transaction)}: \n")
print(failed_transaction)

# Fund Transfer Transaction 
fund_transfer_transaction = df.loc[
    df["transaction_type"] == "Fund Transfer"
]

print(f"The Fund Transfer Transaction count is {len(fund_transfer_transaction)}: \n")
print(fund_transfer_transaction)

# All Transactions Above N50,000 
transactions_above_50000 = df.loc[
    df["amount"] > 50000
]

print(f"The Transactions above N50,000 is: {len(transactions_above_50000)}")
print(transactions_above_50000)

# Successful Transaction 
success_transaction = df.loc[
    df["status"] == "successful"
]

print(f"The successful Transaction count is {len(success_transaction)}: \n")
print(success_transaction)

#Transactions Belonging to C001
transact_belonging_c001 = df.loc[
    df["customer_id"] == "C001"
]

print(f"Transactions Belonging to C001 count is: {len(transact_belonging_c001)}")
print(transact_belonging_c001)