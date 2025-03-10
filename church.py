import streamlit as st
import pandas as pd
from datetime import datetime


#---Input page information for rental properties and Church maintenance ---#
def show_church():
    #--- add standard header --#

    col1, col2 = st.columns([2, 1], vertical_alignment='top')
    with col1:
        current_date = datetime.now().strftime("%d-%m-%Y")
        st.markdown('<b><h1>Methodist Suite of Finances</b></h1>', unsafe_allow_html=True)
        st.header("Church Pages :")
        st.subheader("Transactions relating to the maintenance and expenditure of the church and worship.")
        st.markdown(f"<b><h4>{current_date}</b></h4>", unsafe_allow_html=True)
    with col2:
        st.image('images/Briggswath_Logo.png')
    st.markdown('<hr></hr>', unsafe_allow_html=True)

    col3, col4 = st.columns(([2, 2]), vertical_alignment='bottom')
    with col3:
        st.markdown(f"<b><h3><u> Building Maintenance, Purchases and Services</b></h3></u>", unsafe_allow_html=True)
    col5, col6, = st.columns(([2, 2]), vertical_alignment='bottom')
    with col5:
        st.markdown(f'<b><h3>Description of Work:</b></h3>', unsafe_allow_html=True)
        st.markdown(f'<b><h3>Name of Contractor or firm:</b></h3>', unsafe_allow_html=True)
        st.markdown(f'<b><h3>Amount Charged including VAT:</b></h3>', unsafe_allow_html=True)
    with col6:
        maintenance_building = st.text_input('Work Carried Out:', placeholder='enter description of work')
        contractor = st.text_input('contractor', placeholder=' enter firm/individual undertaking the work')
        amount_charged = st.text_input('amount charged', placeholder='enter the amount charged including VAT') or 0
        float_amount_charged = round(float(amount_charged), 2)
    st.markdown(f'<hr></hr>', unsafe_allow_html=True)
    col7, col8, col9, col10 = st.columns([2, 2, 2, 2])
    with col8:
        if st.button('Submit work done'):
            current_date = datetime.now().strftime("%d-%m-%Y")
            df_main_church = pd.Series({'date': current_date, 'work done': maintenance_building,
                                        'contractor': contractor, 'amount': float_amount_charged})
            df_user = [df_main_church]
            st.dataframe(df_user)
            st.markdown(f"<b><h5>Please Check the entry carefully, then click commit</b></hr>", unsafe_allow_html=True)
    with col9:
        if st.button('Confirm work done'):
            current_date = datetime.now().strftime("%d-%m-%Y")

            df_main_church = pd.Series({'date': current_date, 'work done': maintenance_building,
                                        'contractor': contractor, 'amount': float_amount_charged})
            df_user = [df_main_church]
            st.dataframe(df_user)

            new_data = pd.read_csv(r'data\church_maintenance.csv')
            new_data = pd.concat([new_data, pd.DataFrame(df_user)])
            filtered_new_data = new_data[new_data['amount'] != 0]
            filtered_new_data.to_csv(r"data\church_maintenance.csv", index=False)
    st.markdown(f'<hr></hr>', unsafe_allow_html=True)
