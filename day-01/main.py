from functions_custom import calculate_total

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

total = calculate_total(transactions)

print(f"Total number of transactions: {total}") 