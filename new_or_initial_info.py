import streamlit as st
import pandas as pd
from datetime import datetime
from functions import available_funds
from openpyxl.styles.alignment import vertical_aligments

def collected_data():
    cola, colb = st.columns([2, 1], vertical_alignment='top')
    with cola:
        current_date = datetime.now().strftime("%d-%m-%y")
        st.markdown('<b><h1>Methodist Suite of Finances</b></h1>', unsafe_allow_html=True)
        st.header("Input New Information :")
        st.subheader("initial set up or change of general information")
        st.markdown(f"<b><h4>{current_date}</b></h4>", unsafe_allow_html=True)
    with colb:
        st.image('images/Briggswath_Logo.png')
    st.markdown('<hr></hr>', unsafe_allow_html=True)

    #popluate church_info.csv
    st.header("General Church Details.")
    col1, col2 = st.columns([2,2])
    with col1:
        church=st.text_input('Name of new Church', placeholder='church')
        circuit=st.text_input('Name of new Circuit', placeholder='circuit')
        district=st.text_input('Name of new district', placeholder='district')

    with col2:
        circuit_no = st.text_input('Circuit/District number', placeholder='circuit/district no.')
        charity = st.text_input('charity number', placeholder='charity number')
        gift_aid_no = st.text_input('Gift aid number', placeholder='gift aid number')
    st.markdown(f"<hr></hr>", unsafe_allow_html=True)


    if st.button("Submit Church Info"):
        data={
            'name':[church],
            'circuit':[circuit],
            'district':[district],
            'number':[circuit_no],
            'charity number':[charity],
            'gift aid number':[gift_aid_no]
        }
        df=pd.DataFrame(data)

        #append to csv
        df.to_csv('data/church_info.csv',mode='w',header=False,index=False)
        st.success("Church information updated !")


    st.header("Postholders")
    col3,col4=st.columns([2,2])
    with col3:
        minister=st.text_input('Name of Minister', placeholder='minister')
        steward1=st.text_input('name of steward',placeholder='steward 1')
        steward2=st.text_input('name of steward',placeholder='steward 2')
        steward3 = st.text_input('name of steward', placeholder='steward 3')
        steward4 = st.text_input('name of steward', placeholder='steward 4')
    with col4:
        steward5 = st.text_input('name of steward', placeholder='steward 5')
        steward6 = st.text_input('name of steward', placeholder='steward 6')
        steward7 = st.text_input('name of steward', placeholder='steward 7')
        treasurer=st.text_input('name of treasurer',placeholder='treasurer')

    if st.button("Submit Postholder information"):
        data={
            'minister':[minister],
            'steward1':[steward1],
            'steward2':[steward2],
            'steward3':[steward3],
            'steward4':[steward4],
            'steward5':[steward5],
            'steward6':[steward6],
            'steward7':[steward7],
            'treasurer':[treasurer]
        }
        df=pd.DataFrame(data)
        df.to_csv('data/stewards.csv',mode='w',header=True,index=False)
        st.success('Postholder information updated !')








