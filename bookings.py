import streamlit as st

def show_bookings():
    st.title("Bookings Page")
    st.write("This is where you can manage your bookings.")
    # Add more content and functionality here

#---create menu items---#
#from streamlit_option_menu import option_menu
#
#with st.sidebar:
#   selected = option_menu("Main Menu", ["Home", 'Bookings', 'Offering','Utilities',
#                                        'Property','IN/OUT'],
#                          icons=['house', 'calendar-date','gift','lightning-charge-fill','houses','repeat'], menu_icon="cast", default_index=1)
#
#
#if selected == "Home":
#    show_home()
#elif selected == "Bookings":
#    show_bookings()
#elif selected == "Offering":
#    show_offering()
#elif selected=="Utilities":
#    show_utilities()
#elif selected=="Property":
#    show_property()
#elif selected == "IN/OUT":
#    show_charities()

