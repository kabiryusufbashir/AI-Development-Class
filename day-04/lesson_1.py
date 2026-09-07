import pandas as pd 

amounts = pd.Series([
    5000,
    10000,
    15000,
    7000
])

data = {
    "customers": ["Yusuf", "Aisha", "Ali", "Fatima"],
    "amounts": amounts,
    "status": ["active", "inactive", "active", "inactive"]
}

df = pd.DataFrame(data)

print(df)