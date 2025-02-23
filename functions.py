# function.py
FILEPATH_BANKING = "data/banking.csv"
import pandas as pd

def available_funds(filepath=FILEPATH_BANKING):
    df = pd.read_csv(filepath)
    df.columns = df.columns.str.strip()  # Strip whitespace from column names

    # Convert the 'Balance (£)' column to numeric, forcing errors to NaN
    df['Balance (£)'] = pd.to_numeric(df['Balance (£)'], errors='coerce')

    # Calculate the sum, ignoring NaN values
    sum_column_bank = df['Balance (£)'].sum()

    # Count NaN values in the 'Balance (£)' column
    num_nan = df['Balance (£)'].isna().sum()
    print(f"Number of NaN values in 'Balance (£)': {num_nan}")

    return sum_column_bank

