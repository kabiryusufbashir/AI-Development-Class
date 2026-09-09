import pandas as pd
from pathlib import Path

# __file__ means "this current Python file".
# parent means "the folder that contains this file", which is day-04.
# This makes Python look for:
# day-04/data/transactions.csv
file_path = Path(__file__).parent / "data" / "transactions.csv"

df = pd.read_csv(file_path)

print(df.dtypes)

df["date"] = pd.to_datetime(df["date"])

print(df.dtypes)