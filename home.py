import streamlit as st
import pandas as pd
from datetime import datetime
from functions import available_funds

df = pd.read_csv('data/church_info.csv', sep=',')
db = pd.read_csv('data/banking.csv')

def show_home():

    # ---standard data from data/church_info.csv ---#
    col1, col2 = st.columns([2, 1], vertical_alignment='center')
    with col1:
        st.markdown('<b><h1>Methodist Suite of Finances</b></h1>', unsafe_allow_html=True)
        st.header("Home Page")
        current_date = datetime.now().strftime("%d-%m-%y")
        st.markdown(f"<b><h5>{current_date}</b></h5>",unsafe_allow_html=True)

    with col2:
        st.image('images/Briggswath_Logo.png')
    st.markdown('<hr></hr>', unsafe_allow_html=True)

    col3, col4, col5 = st.columns([1, 1, 0.5])
    with col3:
        for index, row in df.iterrows():
            st.markdown(f'<h3>{row["name"]}</h3>', unsafe_allow_html=True)
    with col4:
        for index, row in df.iterrows():
            st.markdown(f'<h3>{row["circuit"]} in {row["district"]}</h3>', unsafe_allow_html=True)
    with col5:
        for index, row in df.iterrows():
            st.markdown(f"<h4>{row['number']}</h4>", unsafe_allow_html=True)

    st.markdown("""<b><h5><i>Simplifying the role of treasurer within the Methodist Church </b></h5></i>""",
                unsafe_allow_html=True)
    st.markdown("<hr></hr>", unsafe_allow_html=True)

    # ---Banking data ---#
    st.title("Briggswath and Sleights Bank Account Details")

    col6, col7, col8 = st.columns([1.5, 2, 2])
    with col6:
        st.header("Bank Account")
        for index, row in db.iterrows():
            st.subheader(row['Bank'])

    with col7:
        st.header("Current Balance (£)")
        for index, row in db.iterrows():
            st.subheader(row['Balance (£)'])

    with col8:
        st.header("Annual Interest (£)")
        for index, row in db.iterrows():
            st.subheader(row["recorded annual interest"])

    st.write(f'<hr> </hr>', unsafe_allow_html=True)

    col9, col10, col11 = st.columns([1.5, 2, 2])
    with col9:
        st.header("Total Funds (£):")

    # ---This is where the sum of the columns Balance (£) will go from data/banking.csv---#
    with col10:
        sum_column_bank = available_funds()  # Call the function and store the result
    st.subheader(sum_column_bank)  # Display the result