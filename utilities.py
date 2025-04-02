import streamlit as st
import pandas as pd
from datetime import datetime


def show_utilities():
    # ---standard data from data/church_info.csv ---#
    col1, col2 = st.columns([2, 1], vertical_alignment='center')
    with col1:
        st.markdown('<b><h1>Methodist Suite of Finances</b></h1>', unsafe_allow_html=True)
        st.header("Utilities: ")
        current_date = datetime.now().strftime("%d-%m-%y")
        st.markdown(f"<b><h5>{current_date}</b></h5>",unsafe_allow_html=True)

    with col2:
        st.image('images/Briggswath_Logo.png')
    st.markdown('<hr></hr>', unsafe_allow_html=True)

    col3,col4,col5,col6=st.columns([2,2,2,1])


    with col3:
        st.markdown(f"<b><h4>Utility:</b></h4>", unsafe_allow_html=True)
        st.markdown(f"<b><h4> Water Rates:</b></h4>", unsafe_allow_html = True)
        st.markdown(f"<b><h4> Gas and Electric (SSE):</b></h4>", unsafe_allow_html=True)
        st.markdown(f"<b><h4> Telephone:</b></h4>", unsafe_allow_html=True)
        st.markdown(f"<b><h4> Other: </b></h4>",unsafe_allow_html=True)

    with col4:

        WATER=0
        ENERGY=1
        TEL=3
        OTHER=4
        st.markdown(f"<b><h3> Bill Amount :</b></h3>", unsafe_allow_html=True)
        water=st.text_input("Please enter bill amount", placeholder="Bill Amount", key=WATER) or 0
        energy=st.text_input("Please enter bill amount", placeholder="Bill Amount",key = ENERGY) or 0
        tel=st.text_input("Please enter bill amount", placeholder="Bill Amount",key=TEL) or 0
        other=st.text_input("Please enter bill amount", placeholder="Bill Amount", key=OTHER) or 0

        water_float=round(float(water),2)
        energy_float=round(float(energy),2)
        tel_float=round(float(tel),2)
        other_float=round(float(other),2)

    with col5:
        REF=5
        st.markdown(f"<b><h3>Paid to :</b></h3>", unsafe_allow_html=True)
        st.markdown(f"<h1></h1>", unsafe_allow_html=True)
        st.markdown(f"<h2></h2>", unsafe_allow_html=True)
        st.markdown(f"<h2></h2>", unsafe_allow_html=True)
        ref=st.text_input("Please enter a reference", placeholder="Payment Reference", key=REF)

    col7,col8,col9, col10 = st.columns([2,2,2,2])

    with col8:
        if st.button("Submit"):
            current_date = datetime.now().strftime("%d-%m-%Y")
            water_dat=pd.Series({'date': current_date,'reason':"Water Rates",'amount':water_float })
            energy_dat = pd.Series({'date': current_date, 'reason': "Electric Bill", 'amount':energy_float})
            tel_dat = pd.Series({'date': current_date, 'reason': "Telephone Bill", 'amount': tel_float})
            other_dat = pd.Series({'date': current_date, 'reason': ref, 'amount': other_float})

            #---Create a data frame to store user input---#
            user_df = pd.DataFrame([water_dat, energy_dat,tel_dat,other_dat])
            data_util1 = user_df.copy()
            st.dataframe(data_util1)
            st.markdown(f"<b><h5>Please Check the entry carefully, then click commit</b></hr>", unsafe_allow_html=True)


        with col9:
            if st.button("Confirm"):

                current_date = datetime.now().strftime("%d-%m-%Y")

                water_dat = pd.Series({'date': current_date, 'reason': "Water Rates", 'amount': water_float})
                energy_dat = pd.Series({'date': current_date, 'reason': "Energy Bill", 'amount': energy_float})
                tel_dat = pd.Series({'date': current_date, 'reason': "Telephone Bill", 'amount': tel_float})
                other_dat = pd.Series({'date': current_date, 'reason': ref, 'amount': other_float})

                # ---Create a date frame to store user input---#
                user_df = pd.DataFrame([water_dat, energy_dat,tel_dat,other_dat])
                data_util2 = user_df.copy()
                st.dataframe(data_util2)
                st.markdown(f"<b><h5>This data has been sent to file</b></hr>",
                            unsafe_allow_html=True)


                new_data = pd.read_csv(r"data\utility.csv")
                new_data = pd.concat([new_data, pd.DataFrame(data_util2)])
                filtered_new_data = new_data[new_data['amount'] != 0]
                filtered_new_data.to_csv(r"data\utility.csv", index=False)








