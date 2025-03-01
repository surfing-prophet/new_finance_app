import streamlit as st
import pandas as pd
import os
import csv
from datetime import datetime
from functions import get_groups, group_payments, write_groups


def show_bookings():
    # --add standard header--#

    col1, col2 = st.columns([2, 1], vertical_alignment='top')
    with col1:
        st.markdown('<b><h1>Methodist Suite of Finances</b></h1>', unsafe_allow_html=True)
        st.header("Bookings Page")
        st.write("This is where you can manage your bookings.")
        # Add more content and functionality here

    with col2:
        st.image('images/Briggswath_Logo.png')
        get_groups()

        if 'new_group' not in st.session_state:
            st.session_state.new_group = ''

        new_group = st.text_input("Input the name of a new group and click add new group.",
                                   placeholder="Add new group" if not st.session_state.new_group else "",
                                   value=None, key='emp_state')

        if st.button("Add new Group"):
            write_groups(new_group)  # Write the new group to the file
            st.success(f"Group '{new_group}' added successfully!")
            st.session_state.new_group = ""

    st.markdown(f"<hr></hr>", unsafe_allow_html=True)

    col3, col4, col5 = st.columns([2, 2, 2])
    with col3:
        st.markdown(f"<b><h5>Select the group to enter data from</b></h5>", unsafe_allow_html=True)
        groups = get_groups()
        option = st.selectbox("Groups on record", groups)
        st.markdown(f"<b><h5>Currently Selected Group = {option}</b></h5>", unsafe_allow_html=True)
    with col4:
        st.markdown(f"<b><h5>Please input the fee recieved from the selected group</b></h5>", unsafe_allow_html=True)
        fees = st.text_input("fee received :") or 0
        float_fees = round(float(fees), 2)

    with col5:
        st.write("")

    st.markdown('<hr></hr>', unsafe_allow_html=True)

    col6, col7, col8, col9 = st.columns([2, 2, 2, 2])
    with col6:
        st.write("")
    with col7:
        if st.button("Submit"):
            current_date = datetime.now().strftime("%Y-%m-%d")

            #---Create a date frame to store user input---#
            user_df = pd.DataFrame({'date': [current_date], 'group': [option], 'amount': [float_fees]})
            data_copy1 = user_df.copy()
            data_copy2 = user_df.copy()
            st.dataframe(data_copy1)
            st.markdown(f"<b><h5>Please Check the entry carefully, then click commit</b></hr>", unsafe_allow_html=True)

    with col8:
        if st.button("Confirm"):
            current_date = datetime.now().strftime("%d-%m-%Y")
            user_df = pd.DataFrame({'date': [current_date], 'group': [option], 'amount': [float_fees]})
            data_copy1 = user_df.copy()
            data_copy2 = user_df.copy()
            st.dataframe(data_copy1)

            # ---open offering.csv from data---#

            df = pd.read_csv(r"data\group_payments.csv")
            df = pd.concat([df, pd.DataFrame(data_copy1)])
            filtered_df = df[df['amount'] != 0]
            filtered_df.to_csv(r"data\group_payments.csv", index=False)
            st.markdown(f"<b><h5>Information transfered to records. "
                        f"£{float_fees} paid by {option} on {current_date}</b></h5>", unsafe_allow_html=True)

