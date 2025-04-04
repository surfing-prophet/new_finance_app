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

    #circuit assessment data collection
    st.subheader('Circuit Assessment')
    assessment=st.text_input('Circuit assessment for 2024/25',placeholder='enter payment towards assessment')

    # Assign default value if input is empty
    if assessment:
        try:
            float_assessment = round(float(assessment), 2)
        except ValueError:
            st.error('Please enter a valid numeric value for the assessment.')
            float_assessment = 0.0  # or handle this differently based on your needs
    else:
        float_assessment = 0.0  # Default value if no input is provided

    assessment_df = pd.DataFrame({'date': [current_date], 'amount': [float_assessment]})


    if st.button('Submit assessment payment'):
        st.write(assessment_df)
        assess_data=pd.read_csv('data/assessment.csv')
        assess_new=pd.concat([assess_data,assessment_df], ignore_index=True)
        assess_new.to_csv('data/assessment.csv',index=False)
        st.success('information has been written to the assessment file!')
    st.markdown('<hr></hr>', unsafe_allow_html=True)
    #Church outgoings general data collection
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

            new_data = pd.read_csv(r'data/church_maintenance.csv')
            new_data = pd.concat([new_data, pd.DataFrame(df_user)])
            filtered_new_data = new_data[new_data['amount'] != 0]
            filtered_new_data.to_csv(r"data\church_maintenance.csv", index=False)
    st.markdown(f'<hr></hr>', unsafe_allow_html=True)

    st.subheader('Miscellaneous Payments')


    col10,col11 =st.columns([2,2])
    with col10:
        st.markdown(f'</b><h4> Reason for Payment :</b></h4>',unsafe_allow_html=True)
        reason=st.text_input('expenditure reason',placeholder='input reason for expenditure')
    with col11:
        st.markdown(f'<b><h4> Amount paid out</b></h4>', unsafe_allow_html=True)
        amount=st.text_input('amount paid out', placeholder='enter amount in pounds')
        # Default value for amount_float
        amount_float = 0.0
        if amount:
            try:
                amount_float = round(float(amount), 2)
            except ValueError:
                st.error('Please enter a valid numeric value for the amount.')
                amount_float = 0.0  # Default to 0 if input is invalid

    # Create a Series for miscellaneous expenses
    misc_expend = pd.DataFrame({
        'date': [current_date],
        'reason': [reason],
        'amount': [amount_float]
    })

    if st.button('Submit Miscellaneous Payment'):
        misc_df=pd.read_csv('data/misc_expend.csv')
        misc_new=pd.concat([misc_df,misc_expend], ignore_index=True)
        misc_new.to_csv('data/misc_expend.csv', index=False)
        st.dataframe(misc_expend)
        st.success('the information has been uploaded')

