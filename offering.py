import streamlit as st
import pandas as pd
from functions import weekly_reported_offering
from datetime import datetime


#---Input page information for adding offerings ---#
def show_offering():
    #--add standard header--#

    col1, col2 = st.columns([2, 1], vertical_alignment='top')
    with col1:
        st.markdown('<b><h1>Methodist Suite of Finances</b></h1>', unsafe_allow_html=True)
        st.header("Weekly Offerings.")
        current_date = datetime.now().strftime("%d-%m-%y")
        st.markdown(f"<b><h5>{current_date}</b></h5>", unsafe_allow_html=True)
    with col2:
        st.image('images/Briggswath_Logo.png')
    st.markdown('<hr></hr>', unsafe_allow_html=True)

    st.title("Offerings, collections and standing orders :")
    st.write("Please input the financial information for the weekly offering :")

    # ---Custom CSS to increase the font size of number inputs---#
    col3, col4, col5 = st.columns([2,2,1], vertical_alignment="top")

    with col3:
        st.markdown(f"<b><h4> Sunday Collection : </b></h4>", unsafe_allow_html=True)
        st.markdown(f"<b><h4> Standing Orders : </b></h4>", unsafe_allow_html=True)
        st.markdown(f"<b><h4> Other Reason :</b></h4>", unsafe_allow_html=True)
        st.markdown(f"<b><h4> Gift Aid :</b></h4>", unsafe_allow_html=True)


    with col4:
        sc = st.text_input('Amount for Sunday Collection',
                            placeholder="Enter Sunday Collection amount:", key='SC') or 0
        so = st.text_input('Amount for Standing Orders',
                               placeholder="Enter Standing Orders amount:", key='SO') or 0
        other = st.text_input('Amount for Other Reason',
                                  placeholder="Enter Other Reason amount:", key='Other') or 0
        gift_aid=st.text_input('Annual Gift aid',placeholder= 'annual gift aid return:',key='GIFT_AID') or 0

        sc_float=round(float(sc),2)
        so_float=round(float(so),2)
        other_float=round(float(other),2)
        gift_aid_float=round(float(gift_aid),2)
        total=round((sc_float+so_float+other_float+gift_aid_float),2)




    with col5:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        reason=st.text_input("Reason for Offering:",placeholder="enter reason:")

    st.markdown(f"<hr></hr>",unsafe_allow_html=True)

    col6,col7,col8 =st.columns([2,2,2])
    with col6:
        st.markdown(f"<h4><b> Total offering : </b></h4>", unsafe_allow_html=True)

    with col7:
        st.write(f"<h4><b>{total}</b></h4>", unsafe_allow_html=True)

    col8,col9,col10,col11 = st.columns([2,2,2,2],vertical_alignment='top')

    with col8:
        st.write("")

    with col9:

        if st.button("Submit"):
            current_date = datetime.now().strftime("%d-%m-%Y")


    #---Create a date frame to store user input---#

    # step 1 : Prepare the data to save
            Sunday_Off = pd.Series({'date': current_date,'reason':"Sunday Collection",'amount':sc_float })
            Stand_ord =pd.Series({'date': current_date,'reason':"Standing Orders",'amount':so_float })
            other_col =pd.Series({'date': current_date,'reason':reason,'amount':other_float })
            gift_aid = pd.Series({'date':current_date, 'reason':"ANNUAL GIFT AID",'amount':gift_aid_float})
            user_df=pd.DataFrame([Sunday_Off,Stand_ord,other_col, gift_aid])
            data_copy1=user_df.copy()
            data_copy2=user_df.copy()
            st.dataframe(data_copy1)


    with col10:
        if st.button("Confirm"):
            current_date = datetime.now().strftime("%Y-%m-%d")
        #---open user_df again---#
            Sunday_Off = pd.Series({'date': current_date, 'reason': "Sunday Collection", 'amount': sc_float})
            Stand_ord = pd.Series({'date': current_date, 'reason': "Standing Orders", 'amount': so_float})
            other_col = pd.Series({'date': current_date, 'reason': reason, 'amount': other_float})
            gift_aid = pd.Series({'date': current_date, 'reason': "ANNUAL GIFT AID", 'amount': gift_aid_float})
            user_df = pd.DataFrame([Sunday_Off, Stand_ord, other_col, gift_aid])

            data_copy1 = user_df.copy()
            data_copy2 = user_df.copy()
            st.dataframe(data_copy2)
        # ---open offering.csv from data---#
            df = pd.read_csv("data\offering.csv")
            df = pd.concat([df,pd.DataFrame(data_copy1)])
            filtered_df=df[df['amount'] !=0]
            filtered_df.to_csv("data\offering.csv", index=False)

            # Calculate the running total
            filtered_df['Running Total'] = filtered_df['amount'].cumsum()

            filtered_df.to_csv("data/offering.csv", index=False)

    with col11:
        st.write("")



