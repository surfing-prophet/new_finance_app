# function.py
FILEPATH_BANKING = "data/banking.csv"
FILEPATH_OFFERING = "data/offering.csv"
FILEPATH_GROUPS="data/booking_groups.txt"
FILEPATH_UTILITIES="data/utility.csv"
FILEPATH_COTTAGES_RENT="data/property_rents.csv"
import streamlit as st
import pandas as pd
import datetime as datetime


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
def show_church():
    st.switch_page("Church.py")
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
        df = pd.DataFrame(columns=["date", "reason", "amount", "notes"])

    # Append the new data
    df = df.append(data, ignore_index=True)
    df.to_csv('offering.csv', index=False)
#---information for booking page---#
def get_groups(filepath=FILEPATH_GROUPS): #Calls the text file with the different groups
    #read the txt file
    with open(filepath,'r') as booked_groups:
        groups = booked_groups.readlines()
        return groups

def write_groups (groups_arg, filepath=FILEPATH_GROUPS): # Writes a new group to the .txt file
    """Writes new group item in the text file"""
    with open (filepath,'a') as file:
        file.write(groups_arg +'\n')

def group_payments(data):
    # Check if the file exists
    try:
        df = pd.read_csv('group_payments.csv')
    except FileNotFoundError:
        # If the file does not exist, create a new DataFrame
        df = pd.DataFrame(columns=["date", "group", "amount", "notes"])

    # Append the new data
    df = df.append(data, ignore_index=True)
    df.to_csv('group_payments.csv', index=False)

def calculate_rent_and_fee(rent):
    rent_float = round(float(rent), 2)
    agent_fee = rent_float * 0.1
    total_income = round(rent_float - agent_fee)
    return agent_fee, total_income

def create_rent_series(cottage, rent, fee, total_income):
    current_date = datetime.now().strftime("%d-%m-%Y")
    return pd.Series({
        'date': current_date,
        'cottage': cottage,
        'rent': rent,
        'fees': fee,
        'recieved rent': total_income
    })
def save_to_csv(data, FILEPATH_COTTAGES_RENT):
    new_data = pd.read_csv(FILEPATH_COTTAGES_RENT)
    new_data = pd.concat([new_data, pd.DataFrame(data)])
    filtered_new_data = new_data[new_data['recieved rent'] != 0]
    filtered_new_data.to_csv(FILEPATH_COTTAGES_RENT, index=False)

def create_expense_series(cottage, reason, amount):
    current_date = datetime.now().strftime("%d-%m-%Y")
    return pd.Series({
        'date': current_date,
        'cottage': cottage,
        'reason': reason,
        'amount paid': round(float(amount), 2)
    })

