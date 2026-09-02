transactions = [
    {
        "id": 1,
        "type": "Data",
        "amount": 5000.0,
        "status": "successful"
    },
    {
        "id": 2,
        "type": "Airtime",
        "amount": 2000.0,
        "status": "failed"
    },
    {
        "id": 3,
        "type": "Electricity",
        "amount": 10000.0,
        "status": "successful"
    },
    {
        "id": 4,
        "type": "Data",
        "amount": 3000.0,
        "status": "successful"
    },
    {
        "id": 5,
        "type": "Airtime",
        "amount": 1500.0,
        "status": "failed"
    }
]

# Total transactions 
total_transactions = len(transactions) 
print(f"Total number of transactions: {total_transactions}")

# Successful Transactions
total_successful_transactions = [
    transaction for transaction in transactions 
    if transaction["status"] == "successful"
]
print(f"Total number of successful transactions: {len(total_successful_transactions)}")

# Failed Transactions
total_failed_transactions = [
    transaction for transaction in transactions 
    if transaction["status"] == "failed"
]
print(f"Total number of failed transactions: {len(total_failed_transactions)}")

# Total Successful Amount 
total_successful_amount = sum(
    transaction["amount"] for transaction in transactions 
    if transaction["status"] == "successful"
)
print(f"Total amount of successful transactions: {total_successful_amount}")

# Average Successful Transaction Amount 
average_successful_amount = total_successful_amount / len(total_successful_transactions) if total_successful_transactions else 0
print(f"Average amount of successful transactions: {average_successful_amount}")

# Unique Transaction Types 
unique_transaction_types = set(transaction["type"] for transaction in transactions)
print(f"Unique transaction types: {unique_transaction_types}")

