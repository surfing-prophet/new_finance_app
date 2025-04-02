import streamlit as st
import pandas as pd
import openpyxl as ox
from datetime import datetime

def show_donations():
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
    st.header('Donations Page')

    col3,col4,col5=st.columns([2,2,2])
    with col3:
        st.subheader('Charitable Organisation')
        charity=st.text_input('Name of Charity',placeholder='Enter the name of the charity', value='Charity Name')
    with col4:
        st.subheader('amount collected')
        amount_in=st.text_input('Amount Collected', placeholder='', value='0')
        float_in=round(float(amount_in),2)
    with col5:
        st.subheader('amount given out')
        amount_out=st.text_input('amount donated',placeholder='', value='0')
        float_out=round(float(amount_out),2)

    donation_df=pd.DataFrame({
        'date':[current_date],
        'charity':[charity],
        'amount in':[float_in],
        'amount out':[float_out]
    })
    st.write(donation_df)
    if st.button('Submit Charitable Donation'):
        donation_new=pd.read_csv('data/donations.csv')
        donation_new=pd.concat([donation_new,donation_df],ignore_index=True)
        st.write(donation_df)
        donation_new.to_csv('data/donations.csv',index=False)
        st.success('Donation added to file.')






