# function.py
FILEPATH_BANKING = "data/banking.csv"
FILEPATH_OFFERING = "data/offering.csv"
import streamlit as st
import pandas as pd


##---Defining the menu items---#
# Display the selected page
def show_home():
    st.switch_page("main.py")
def show_bookings():
    st.switch_page("bookings.py")
def show_offering():
    st.switch_page("offering.py")
def show_utilities():
    st.switch_page("utilities.py")
def show_property():
    st.switch_page("properties.py")
def show_charities():
    st.switch_page("charities.py")

#---calling Banking information ---#

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

def weekly_reported_offering(data):
    # Check if the file exists
    try:
        df = pd.read_csv('offering.csv')
    except FileNotFoundError:
        # If the file does not exist, create a new DataFrame
        df = pd.DataFrame(columns=["date", "reason", "amount"])

    # Append the new data
    df = df.append(data, ignore_index=True)
    df.to_csv('offering.csv', index=False)


