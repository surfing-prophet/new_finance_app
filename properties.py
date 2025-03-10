import streamlit as st
import pandas as pd
from functions import calculate_rent_and_fee
from datetime import datetime


#---Input page information for rental properties and Church maintenance ---#
def show_properties():
    #--- add standard header --#

    col1, col2 = st.columns([2, 1], vertical_alignment='top')
    with col1:
        current_date = datetime.now().strftime("%d-%m-%y")
        st.markdown('<b><h1>Methodist Suite of Finances</b></h1>', unsafe_allow_html=True)
        st.header("Property Pages :")
        st.subheader("Transactions relating to the rents "
                 "and maintenance of 2 Carr Hill Lane and 4 Carr Hill Lane")
        st.markdown(f"<b><h4>{current_date}</b></h4>", unsafe_allow_html=True)
    with col2:
        st.image('images/Briggswath_Logo.png')
    st.markdown('<hr></hr>', unsafe_allow_html=True)

    col3, col4=st.columns([2,2], vertical_alignment='top')
    RENT2=0
    RENT4=1
    with col3:
        st.header('2 Carr Hill Lane Property')
        st.markdown(f'<hr></hr>', unsafe_allow_html=True)

        col3a,col3b=st.columns([1,2], vertical_alignment='top')
        with col3a:
            st.markdown(f'<b><h3>Monthly Rent: </b></h3>', unsafe_allow_html=True)
            st.markdown(f'<b><h3>Agents Fee: </b></h3><h5>10% +VAT (@20%)', unsafe_allow_html=True)
            st.markdown(f'<b><h3>Total Rental Income: </b></h3>', unsafe_allow_html=True)

        with col3b:
            rent2=st.text_input('',placeholder='input rent recieved',key=RENT2) or 0
            rent2_float=round(float(rent2),2)
            ag_fee2 = (rent2_float * .1)
            ag_VAT_2 = round(float(ag_fee2 * .2),2)
            ag_total_fee2 = (ag_fee2 + ag_VAT_2)
            st.markdown(f'<h3></h3>', unsafe_allow_html=True)
            st.markdown(f'<b></h3>£{ag_total_fee2}</b></h3>', unsafe_allow_html=True)
            rent2_total = round(float(rent2_float - ag_total_fee2),2)
            st.markdown(f'<h3></h3>', unsafe_allow_html=True)
            st.markdown(f'<b><h3>£{rent2_total}</b></h3>', unsafe_allow_html=True)
    with col4:
        st.header('4 Carr Hill Lane Property')
        st.markdown(f'<hr></hr>', unsafe_allow_html=True)

        col4a, col4b = st.columns([1,2], vertical_alignment='top')
        with col4a:
            st.markdown(f'<b><h3>Monthly Rent: </b></h3>', unsafe_allow_html=True)
            st.markdown(f'<b><h3>Agents Fee: </b></h3><h5>10% +VAT (@20%)', unsafe_allow_html=True)
            st.markdown(f'<b><h3>Total Rental Income: </b></h3>', unsafe_allow_html=True)
        with col4b:
            rent4 = st.text_input('', placeholder='input rent recieved', key=RENT4) or 0
            rent4_float = round(float(rent4),2)
            ag_fee4 = round(float(rent4_float * .1),2)
            ag_VAT_4=round(float(ag_fee4*.2),2)
            ag_total_fee4=round(float(ag_fee4+ag_VAT_4),2)
            st.markdown(f'<h3></h3>',  unsafe_allow_html=True)
            st.markdown(f'<b></h3>£{ag_total_fee4}</b></h3>', unsafe_allow_html=True)
            rent4_total = round(float(rent4_float - ag_total_fee4),2)

            st.markdown(f'<h3></h3>',  unsafe_allow_html=True)
            st.markdown(f'<b><h3>£{rent4_total}</b></h3>', unsafe_allow_html=True)

    colsub2,colcon2,colsub4,colcon4 = st.columns([2,2,2,2])
    with colsub2:
        if st.button('submit 2 Carr Hill Lane'):
            current_date = datetime.now().strftime("%d-%m-%Y")

            #create dataset for rents 2 Carr Hill Lane
            two_CHL = pd.Series({'date':current_date,'cottage':"2 Carr Hill Lane",
                                 'rent':rent2,'fees':ag_total_fee2,'recieved rent':rent2_total})
            user_df2=[two_CHL]
            st.dataframe(user_df2)
            st.markdown(f"<b><h5>Please Check the entry carefully, then click commit</b></hr>", unsafe_allow_html=True)
    with colcon2:
        if st.button('confirm 2 Carr Hill Lane'):
            current_date = datetime.now().strftime("%d-%m-%Y")

            # create dataset for rents 2 Carr Hill Lane
            two_CHL = pd.Series({'date': current_date, 'cottage': "2 Carr Hill Lane",
                                 'rent': rent2, 'fees': ag_total_fee2, 'recieved rent': rent2_total})
            user_df2 = [two_CHL]
            st.dataframe(user_df2)

            new_data = pd.read_csv(r"data\property_rents.csv")
            new_data = pd.concat([new_data, pd.DataFrame(user_df2)])
            filtered_new_data = new_data[new_data['recieved rent'] != 0]
            filtered_new_data.to_csv(r"data\property_rents.csv", index=False)
            st.markdown(f"<b><h5>The following has been added.</b></hr>", unsafe_allow_html=True)

    with colsub4:

        if st.button('submit 4 Carr Hill Lane'):
            current_date = datetime.now().strftime("%d-%m-%Y")

                #create dataset for rents 4 Carr Hill Lane
            four_CHL = pd.Series({'date':current_date,'cottage':"4 Carr Hill Lane",
                                      'rent':rent4,'fees':ag_total_fee4,'recieved rent':rent4_total})
            user_df4=[four_CHL]
            st.dataframe(user_df4)
            st.markdown(f"<b><h5>Please Check the entry carefully, then click commit</b></hr>", unsafe_allow_html=True)
    with colcon4:
        if st.button('confirm 4 Carr Hill lane'):
            current_date = datetime.now().strftime("%d-%m-%Y")

            # create dataset for rents 4 Carr Hill Lane
            four_CHL = pd.Series({'date': current_date, 'cottage': "4 Carr Hill Lane",
                                      'rent': rent4, 'fees': ag_total_fee4, 'recieved rent': rent4_total})
            user_df4 = [four_CHL]
            st.dataframe(user_df4)

            new_data = pd.read_csv(r"data\property_rents.csv")
            new_data = pd.concat([new_data, pd.DataFrame(user_df4)])
            filtered_new_data = new_data[new_data['recieved rent'] != 0]
            filtered_new_data.to_csv(r"data\property_rents.csv", index=False)
            st.markdown(f"<b><h5>The following has been added.</b></hr>", unsafe_allow_html=True)

    st.markdown(f'<hr></hr>', unsafe_allow_html=True)
    st.markdown(f'<b><h3> Expenditure for Cottages</b></h3>', unsafe_allow_html=True)

    col5, col6= st.columns([2,2])
    with col5:
        st.header('2 Carr Hill Lane')
        col5a, col5b=st.columns([2,1])
        with col5a:
            CAR2MAINT=4
            car2_maint=st.text_input(f'reason for expenditure :', placeholder="input reason", key=CAR2MAINT) or 0
        with col5b:
            CAR2MAINTAMOUNT = 5
            car2_maint_amount=st.text_input(f'amount spent :',placeholder="input amount",key=CAR2MAINTAMOUNT) or 0
            car2_maint_float=round(float(car2_maint_amount),2)
    with col6:
        st.header('4 Carr Hill Lane')
        col6a,col6b=st.columns([2,1])
        with col6a:
            CAR4MAINT=6
            car4_maint = st.text_input(f'reason for expenditure :', placeholder="input reason", key=CAR4MAINT) or 0
        with col6b:
            CAR4MAINTAMOUNT=7
            car4_maint_amount = st.text_input(f'amount spent :', placeholder="input amount", key=CAR4MAINTAMOUNT) or 0
            car4_maint_float=round(float(car4_maint_amount),2)
    expsub2,expcon2,expsub4,expcon4 = st.columns([2,2,2,2])
    with expsub2:
        if st.button('submit expenditure for 2 Carr Hill lane'):
            current_date = datetime.now().strftime("%d-%m-%Y")
            # create dataset for expenditure 2 Carr Hill Lane
            exp2 = pd.Series({'date': current_date, 'cottage': "2 Carr Hill Lane",
                                  'reason': car2_maint, 'amount paid': car2_maint_float})
            user_df2 = [exp2]
            st.dataframe(user_df2)
            st.markdown(f"<b><h5>Please check the amount and confirm.</b></hr>", unsafe_allow_html=True)
    with expcon2:
        if st.button('Confirm expenditure 2 Carr Hill Lane'):
            current_date=datetime.now().strftime("%d-%m-%Y")
            exp2_new=pd.Series({'date':current_date,'cottage':"2 Carr Hill Lane",
                            'reason': car2_maint,'amount paid': car2_maint_float})
            new_data = pd.read_csv(r"data\property_expend.csv")
            new_data = pd.concat([new_data, pd.DataFrame([exp2_new])])
            filtered_new_data = new_data[new_data['amount paid'] != 0]
            filtered_new_data.to_csv(r"data\property_expend.csv",index=False)
            st.dataframe([exp2_new])
            st.markdown(f"<b><h5>The following has been added.</b></hr>", unsafe_allow_html=True)

    with expsub4:
        if st.button('submit expenditure for 4 Carr Hill lane'):
            current_date = datetime.now().strftime("%d-%m-%Y")
            # create dataset for expenditure 4 Carr Hill Lane
            exp4 = pd.Series({'date': current_date, 'cottage': "4 Carr Hill Lane",
                                  'reason': car4_maint, 'amount paid': car4_maint_float})
            user_df4 = [exp4]
            st.dataframe(user_df4)
            st.markdown(f"<b><h5>Please check the amount and confirm.</b></hr>", unsafe_allow_html=True)
    with expcon4:
        if st.button('Confirm expenditure 4 Carr Hill Lane'):
            current_date=datetime.now().strftime("%d-%m-%Y")
            exp4_new=pd.Series({'date':current_date,'cottage':"4 Carr Hill Lane",
                            'reason': car4_maint,'amount paid': car4_maint_float})
            new_data = pd.read_csv(r"data\property_expend.csv")
            new_data = pd.concat([new_data, pd.DataFrame([exp4_new])])
            filtered_new_data = new_data[new_data['amount paid'] != 0]
            filtered_new_data.to_csv(r"data\property_expend.csv",index=False)
            st.dataframe([exp4_new])
            st.markdown(f"<b><h5>The following has been added.</b></hr>", unsafe_allow_html=True)