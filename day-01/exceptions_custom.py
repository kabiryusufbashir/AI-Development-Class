def validate_transaction(amount: float, transaction_type: str) -> None:
    """Validate the transaction amount and type."""
    if amount <= 0:
        raise ValueError("Transaction amount must be greater than zero.")
    if transaction_type not in ["Data", "Airtime", "Electricity"]:
        raise ValueError("Invalid transaction type. Must be 'Data', 'Airtime', or 'Electricity'.")

print(validate_transaction(5000.0, "Datann"))  