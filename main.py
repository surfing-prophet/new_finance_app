#---import libraries ---#
import streamlit as st
import pandas as pd
from bookings import show_bookings
from home import show_home
from offering import show_offering
from utilities import show_utilities
from properties import show_properties
from church import show_church
from accounting import show_accounting

#---create page homepage ---#
st.set_page_config(layout='wide')
st.markdown("""
            <style>
                .st-dd, .stTextInput > div > div > input, .stButton > button, .stSlider > div st.write >div {
                    vertical-align: bottom !important;
                    font-family: 'Inter';
                    font-size: 18px;
                    font-weight: 500;
                }
                .stTextInput > div > div > input {
                    margin-bottom: 5px !important;
                }
            </style>
            """, unsafe_allow_html=True)
df = pd.read_csv('data/church_info.csv', sep=',')
db = pd.read_csv('data/banking.csv')

#---create menu items---#
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Offering', 'Bookings', 'Utilities',
                                          'Property', 'Church','IN/OUT','Accounting'],
                           icons=['bank', 'currency-pound', 'calendar-date', 'fire',
                                  'houses', 'hospital', 'gift','clipboard-data'],
                           menu_icon="cast", default_index=0)

if selected == "Home":
    show_home()
elif selected == "Bookings":
    show_bookings()
elif selected == "Offering":
    show_offering()
elif selected=="Utilities":
    show_utilities()
elif selected=="Property":
    show_properties()
elif selected=='Church':
    show_church()
elif selected == "IN/OUT":
    show_charities()
elif selected=="Accounting":
    show_accounting()