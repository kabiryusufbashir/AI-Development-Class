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
def calculate_total(transactions: list) -> int:
    """Calculate the total number of transactions."""
    return len(transactions)

print(f"Total number of transactions: {calculate_total(transactions)}")

# Success Rate 
def calculate_success_rate(transactions: list) -> float:
    """Calculate the success rate of transactions."""
    total_transactions = len(transactions)
    successful_transactions = [
        transaction 
        for transaction in transactions 
        if transaction["status"] == "successful"
    ]
    return len(successful_transactions) / total_transactions * 100 if total_transactions else 0

print(f"Success rate: {calculate_success_rate(transactions):.2f}")

# Filter Transaction 
def filter_transactions(transactions: list, status: str) -> list:
    """Filter transactions based on their status."""
    return [
        transaction 
        for transaction in transactions 
        if transaction["status"] == status
    ]

print(f"Successful transactions: {len(filter_transactions(transactions, 'successful'))}")
print(f"Failed transactions: {len(filter_transactions(transactions, 'failed'))}")

# Average Transaction Amount 
def calculate_average_amount(transactions: list) -> float:
    """Calculate the average amount of transactions."""
    total_amount = sum(transaction["amount"] for transaction in transactions)
    return total_amount / len(transactions) if transactions else 0

print(f"Average transaction amount: {calculate_average_amount(transactions):.2f}")

# Transaction Type 
def group_transactions_by_type(transactions: list) -> dict:
    """Group transactions by their type."""
    grouped_transactions = {}
    for transaction in transactions:
        transaction_type = transaction["type"]
        if transaction_type not in grouped_transactions:
            grouped_transactions[transaction_type] = []
        grouped_transactions[transaction_type].append(transaction)
    return grouped_transactions

print(f"Transactions grouped by type: {group_transactions_by_type(transactions)}")