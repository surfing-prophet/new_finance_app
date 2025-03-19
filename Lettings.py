import streamlit as st
import pandas as pd
from datetime import datetime

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

#Define the path for the new CSV file
output_csv_path='data/total_lettings.csv'
#write the DataFrame to the csv file
total_sums_df.to_csv(output_csv_path, index=False)
st.success(f"Total sums have been written to {output_csv_path}")