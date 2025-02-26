import streamlit as st
from functions import weekly_reported_offering
from datetime import datetime


#---Input page information for adding offerings ---#
def show_offering():
    st.title("Offerings, collections and standing orders :")
    st.write("Please input the financial information for the weekly offering :")

    # Custom CSS to increase the font size of number inputs
    st.markdown("""
            <style>
            .stNumberInput input {
                font-size: 20px; 
                padding: 10px;   
            }
            </style>
        """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2,2,1], vertical_alignment="center")

    with col1:
        st.markdown(f"<b><h4> Sunday Collection : </b></h4>", unsafe_allow_html=True)
        st.markdown(f"<b><h4> Standing Orders : </b></h4>", unsafe_allow_html=True)
        st.markdown(f"<b><h4> Other Reason :</b></h4>", unsafe_allow_html=True)
        st.markdown(f"<hr></hr>", unsafe_allow_html=True)
        st.markdown(f"<h4><b> Total offering : </b></h4>", unsafe_allow_html = True)

    with col2:
        sc = st.text_input('Amount for Sunday Collection',
                             placeholder="Enter Sunday Collection amount:", key='SC')

        so = st.text_input('Amount for Standing Orders', placeholder="Enter Standing Orders amount:", key='SO')
        other = st.text_input('Amount for Other Reason', placeholder="Enter Other Reason amount:", key='Other')

        total=sc+so+other

        st.write("")
        st.write("")
        st.write(f"<h4><b>{total}</b></h4>", unsafe_allow_html=True)

    # Button to save data to CSV
    if st.button("Submit"):
        current_date = datetime.now().strftime("%Y-%m-%d")

        # Prepare the data to save
        data_to_save = [
            {"date": current_date, "reason": "Sunday Collection", "amount": sc},
            {"date": current_date, "reason": "Standing Orders", "amount": so},
            {"date": current_date, "reason": "Other", "amount": other}
        ]

        # Save each entry to the CSV
        for entry in data_to_save:
            weekly_reported_offering(entry)

        st.success("Data saved successfully!")
