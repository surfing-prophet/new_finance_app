import streamlit as st
import pandas as pd
import openpyxl
from datetime import datetime
from functions import total_offerings, bank_interest


def show_accounting():
    # --add standard header--#
    col1, col2 = st.columns([2, 1], vertical_alignment='top')
    with col1:
        current_date = datetime.now().strftime('%d:%m:%Y')
        st.markdown('<b><h1>Methodist Suite of Finances</b></h1>', unsafe_allow_html=True)
        st.header("Data for Standard Form of Accounts files.")
        st.markdown(f"<b><h5>{current_date}</b></h5>", unsafe_allow_html=True)
    with col2:
        st.image('images/Briggswath_Logo.png')
    st.markdown('<hr></hr>', unsafe_allow_html=True)

    st.title("Offerings, collections and standing orders :")
    st.write("Please input the financial information for the weekly offering :")

    # Load yearly offering
    col3, col4 = st.columns([2, 2])
    with col3:
        Yearly_offering = total_offerings()
        st.markdown(f'<b><h2> Yearly Offering so far (including Gift Aid) is : £{Yearly_offering:.2f}</b></h2>',
                    unsafe_allow_html=True)


    # Load the data from the Excel file
    file_path = r'data\Church-receipts-and-payments-2024.xlsx'
    data = pd.ExcelFile(file_path)

    # Function to update Excel file with data from CSV
    def update_excel_with_csv(excel_path, csv_paths, sheet_name, cell_updates_list):
        # Load the Excel file
        excel_data = pd.read_excel(excel_path, sheet_name=sheet_name)

        # Display the values to be updated
        st.subheader("Values to be Updated:")
        update_values = {}
        update_messages = set()  # Use a set to collect unique update messages

        for csv_path, cell_updates in zip(csv_paths, cell_updates_list):
            # Load the CSV file
            csv_data = pd.read_csv(csv_path)

            for cell, column_name in cell_updates.items():
                row, col = cell
                # Ensure the column name exists in the CSV
                if column_name in csv_data.columns:
                    if csv_path == 'data/banking.csv':  # Check if the current CSV is banking.csv
                        # Iterate through all rows of the banking CSV
                        for index in range(len(csv_data)):
                            balance_cell_row = 17 + index  # Start from row 17 for balances
                            interest_cell_row = 17 + index  # Start from row 17 for interests

                            if balance_cell_row < len(excel_data):  # Ensure we don't go out of bounds
                                # Update balance
                                update_values[(balance_cell_row, 2)] = csv_data['Balance (£)'].iloc[index]
                                # Collecting unique update message for balance
                                update_messages.add(
                                    f"Cell {chr(65 + 2)}{balance_cell_row + 1} will be updated with: "
                                    f"{update_values[(balance_cell_row, 2)]} (Row {index + 1})"
                                )
                                # Update interest
                                update_values[(interest_cell_row, 3)] = csv_data['recorded annual interest'].iloc[index]
                                # Collecting unique update message for interest
                                update_messages.add(
                                    f"Cell {chr(65 + 3)}{interest_cell_row + 1} will be updated with: "
                                    f"{update_values[(interest_cell_row, 3)]} (Row {index + 1})"
                                )
                    elif csv_path=='data/total_lettings.csv':
                        for index in range(len(csv_data)):
                            amount_cell_row=20 + index
                            rent_cell_row=20 + index

                            if amount_cell_row < len(excel_data):  # Ensure we don't go out of bounds
                                # Update balance
                                update_values[(amount_cell_row, 2)] = csv_data['Column'].iloc[index]
                                # Collecting unique update message for balance
                                update_messages.add(
                                    f"Cell {chr(65 + 2)}{amount_cell_row + 1} will be updated with: "
                                    f"{update_values[(amount_cell_row, 2)]} (Row {index + 1})"
                                )
                                # Update interest
                                update_values[(rent_cell_row, 3)] = csv_data['Total Sum'].iloc[index]
                                # Collecting unique update message for interest
                                update_messages.add(
                                    f"Cell {chr(65 + 3)}{rent_cell_row + 1} will be updated with: "
                                    f"{update_values[(rent_cell_row, 3)]} (Row {index + 1})"
                                )
                    else:
                        # For other CSVs, just take the first value
                        update_values[cell] = csv_data[column_name].iloc[0]
                        # Collecting unique update message for other CSVs
                        update_messages.add(
                            f"Cell {chr(65 + col)}{row + 1} will be updated with: {update_values[cell]} (Row 1)")

                else:
                    st.error(f"Column '{column_name}' not found in {csv_path}.")

        # Sort messages based on cell references with natural sorting
        sorted_messages = sorted(update_messages, key=lambda msg: (msg[5], int(''.join(filter(str.isdigit, msg[5:])))))

        # Display all unique update messages at once in sorted order
        for message in sorted_messages:
            st.write(message)  # Displaying unique collected update messages

        # Confirmation button
        if st.button("Confirm and Update"):
            # Update the specific cells in the DataFrame
            for cell, value in update_values.items():
                row, col = cell
                excel_data.at[row, excel_data.columns[col]] = value

            # Save the updated DataFrame back to the Excel file
            with pd.ExcelWriter(excel_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
                excel_data.to_excel(writer, sheet_name=sheet_name, index=False)

            st.success("Excel file updated successfully!")

    # Streamlit app
    st.title("Update Excel File with CSV Data")

    # File paths
    excel_file_path = 'data/Church-receipts-and-payments-2025.xlsx'
    csv_file_paths = ['data/church_info.csv', 'data/stewards.csv',
                      'data/offering.csv', 'data/banking.csv','data/total_lettings.csv']

    # Cells to update with corresponding CSV column names
    cells_to_update_list = [
        {
            (0, 2): 'name',  # Update cell C1 with 'name' from church_info.csv
            (1, 2): 'circuit',  # Update cell C2 with 'circuit' from church_info.csv
            (2, 2): 'district',  # Update cell C3 with 'district' from church_info.csv
            (3, 2): 'number',  # Update cell C4 with 'number' from church_info.csv
        },
        {
            (6, 2): 'minister',  # Update cell C7 with 'minister' from stewards.csv
            (7, 2): 'steward1',  # Update cell C8 with 'steward1' from stewards.csv
            (8, 2): 'steward2',  # Update cell C9 with 'steward2' from stewards.csv
            (9, 2): 'steward3',  # Update cell C10 with 'steward3' from stewards.csv
            (10, 2): 'steward4',  # Update cell C11 with 'steward4' from stewards.csv
            (11, 2): 'treasurer',  # Update cell C12 with 'treasurer' from stewards.csv
        },
        {
            (14, 2): 'Running Total',  # Update cell C15 with 'total amount including gift aid' from offerings.csv
        },
        {
            (17, 2): 'Balance (£)',  # Update cell C198 with CFB Balance from banking.csv
            (18, 2): 'Balance (£)',  # Update cell C19 with TMCP Balance from banking.csv
            (19, 2): 'Balance (£)',  # Update cell C20 with HSBC Balance from banking.csv
            (17, 3): 'recorded annual interest',  # Update cell D18 with CFB Interest
            (18, 3): 'recorded annual interest',  # Update cell D19 with interest from TMCP
            (19, 3): 'recorded annual interest',  # Update cell D20 with interest from HSBC account.
        },
        {
            (21,2): 'Total Sum',
            (22,2): 'Total Sum',
        }
    ]

    # Display the values to be updated and confirm
    update_excel_with_csv(excel_file_path, csv_file_paths, 'Data from streamlit', cells_to_update_list)

    # Display the updated Excel file
    st.subheader("Updated Excel File")
    updated_excel_data = pd.read_excel(excel_file_path, sheet_name='Data from streamlit')
    st.dataframe(updated_excel_data)