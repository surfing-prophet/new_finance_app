# function.py
from PIL.ImImagePlugin import number
FILEPATH_BANKING = "data/banking.csv"
FILEPATH_OFFERING = "data/offering.csv"
FILEPATH_GROUPS="data/booking_groups.txt"
FILEPATH_UTILITIES="data/utility.csv"
FILEPATH_COTTAGES_RENT="data/property_rents.csv"
import streamlit as st
import pandas as pd
import datetime as datetime
from pdfrw import PdfReader as PdfReaderW, PdfWriter as PdfWriterW
import os
import openpyxl
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

#Final Outputs for Standard forms of accounts

def offering_summation():
    df2 = pd.read_csv(r'data\offering.csv')
    total = df2['amount'].sum()
    return total

def read_to_columns(filepath):
    with open(filepath, 'r') as file:
        lines=file.readlines()
        data = [line.strip() for line in lines]
    df=pd.DataFrame([data],columns=['church Name','circuit','district','id_number'])
    return df

def stewards_info(filepath):
    with open (filepath,'r') as file:
        lines=file.readlines()
        data=[line.strip() for line in lines]
    df=pd.DataFrame([data],columns=['minister','steward1','steward2','steward3','steward4','treasurer'])
    return df

def extract_fields_from_excel(file):
    # Read the Excel file (assuming the first sheet contains the form fields)
    df = pd.read_excel(file, sheet_name=0)  # Read the first sheet
    fields = df.columns.tolist()  # Get the headers as field names
    return fields


def stewards_data_excel(filepath):
    # Load the data from the text file
    df = pd.read_csv(filepath)  # or pd.read_table depending on your file format
    # Check if the required columns exist
    required_columns = ['minister', 'steward1', 'steward2', 'steward3', 'steward4', 'treasurer']
    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing column: {column}")

    # Extract the necessary information
    minister = df['minister'].iloc[0]
    steward1 = df['steward1'].iloc[0]
    steward2 = df['steward2'].iloc[0]
    steward3 = df['steward3'].iloc[0]
    steward4 = df['steward4'].iloc[0]
    treasurer = df['treasurer'].iloc[0]

    # Return all values as a dictionary
    return {
        "minister": minister,
        "steward1": steward1,
        "steward2": steward2,
        "steward3": steward3,
        "steward4": steward4,
        "treasurer": treasurer,
    }
#sum of yearly offerings for standard forms of accounts
def total_offerings ():
    df_offering = pd.read_csv(r'data\offering.csv')
    df_offering_total =df_offering['amount'].sum()
    return df_offering_total

def lettings_sum(csv_paths, date_column, start_date, end_date, columns_to_sum):
    total_sums ={col:0 for col in columns_to_sum} #initiate sums for the specified columns

    for csv_path in csv_paths:

        # Load the csv files
        df = pd.read_csv(csv_path)


        # Convert the date column to datetime
        df[date_column] = pd.to_datetime(df[date_column], format='%d-%m-%Y')

        #filter the DataFrame by date range
        filtered_df = df[(df[date_column]>= start_date) & (df[date_column] <=end_date)]


        #sum the specified columns
        for col in columns_to_sum:
            if col in filtered_df.columns:
                total_sums[col] += filtered_df[col].sum()
            else:
                print(f"Warning: Column '{col}' not found in '{csv_path}'.")
    return total_sums


    csv_paths = ['data/group_payments.csv', 'data/property_rents.csv']
    date_column = 'date'
    start_date = '2024-09-01'
    end_date = '2025-08-31'
    columns_to_sum = ['amount','recieved rent']

    results =lettings_sum(csv_paths, date_column, start_date, end_date, columns_to_sum)

    # Display the total sums in Streamlit
    st.subheader('Total Sums')
    for column, total in results.items():
        st.write(f"{column}: {total}")

    #Create a new DataFrame to hold the total sums
    total_sums_df=pd.DataFrame(results.items(),columns=['Column', 'Total Sum'])

#   Define the path for the new CSV file
    output_csv_path='data/total_lettings.csv'
    #write the DataFrame to the csv file
    total_sums_df.to_csv(output_csv_path, index=False)
    st.success(f"Total sums have been written to {output_csv_path}")

#banking information interest for standard form of accounts
def bank_interest():
    # Load the data from the text file
    df = pd.read_csv('data/banking.csv')  # or pd.read_table depending on your file format
    # Check if the required columns exist
    required_columns = ['Bank','Balance (£)','recorded annual interest']
    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing column: {column}")

    # Extract the necessary information
    CFB_Balance = df['Balance (£)'].iloc[0]
    TMCP_Balance = df['Balance (£)'].iloc[1]
    HSBC_Balance = df['Balance (£)'].iloc[2]
    CFB_Interest = df['interest'].iloc[0]
    TMCP_Interest = df['interest'].iloc[1]
    HSBC_Interest = df['interest'].iloc[2]

    # Return all values as a dictionary
    return {
        "CFB Balance": CFB_Balance,
        "TMCP Balance": TMCP_Balance,
        "HSBC Balance": HSBC_Balance,
        "CFB interest": CFB_Interest,
        "TMCP interest": TMCP_Interest,
        "HSBC interest": HSBC_Interest,
    }


