import streamlit as st
import pandas
from functions import (available_funds,show_home,show_bookings,show_property,
                       show_utilities,show_offering, show_charities)


#---create page homepage ---#
st.set_page_config(layout='wide')
df=pandas.read_csv('data/church_info.csv', sep=',')
db=pandas.read_csv('data/banking.csv')

#---create menu items---#
from streamlit_option_menu import option_menu

with st.sidebar:
   selected = option_menu("Main Menu", ["Home", 'Bookings', 'Offering','Utilities',
                                        'Property','IN/OUT'],
                          icons=['house', 'calendar-date','gift','lightning-charge-fill','houses','repeat'], menu_icon="cast", default_index=1)
   selected

if selected == "Home":
    show_home()
elif selected == "Bookings":
    show_bookings()
elif selected == "Offering":
    show_offering()
elif selected=="Utilities":
    show_utilities()
elif selected=="Property":
    show_property()
elif selected == "IN/OUT":
    show_charities()

# --- Display the selected page---#
st.title("Weekly and one off offerings")