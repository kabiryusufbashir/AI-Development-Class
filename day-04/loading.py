import pandas as pd
from pathlib import Path

# __file__ means "this current Python file".
# parent means "the folder that contains this file", which is day-04.
# This makes Python look for:
# day-04/data/transactions.csv
file_path = Path(__file__).parent / "data" / "transactions.csv"

df = pd.read_csv(file_path)

# print(df.head())  # Print the first 5 rows of the DataFrame
# print(df.tail())  # Print the last 5 rows of the DataFrame
# print(df.shape) # Print the number of rows and columns in the DataFrame
# print(df.columns)  # Print the column names of the DataFrame
# print(df.dtypes)  # Print the data types of each column
# print(df.info())  # Print a concise summary of the DataFrame   
# print(df.describe())  # Print summary statistics for numerical columns 
print(df)