import streamlit as st
from Create import AddDriverUI, AddDriverContactUI, AddCustomerUI, AddLocationUI, AddCarCategoryUI, AddCarUI, AddDiscountCouponUI, AddBookingDetailsUI

from Read import getAllDriversUI, getDriverByDLUI, getDriverContactByDLUI, getAllDriverContactsUI, getAllCustomersUI, getCustomerByUsernameUI, getLocationByNameUI, getAllLocationsUI, getAllCarCategoriesUI, getAllCarCategoryByNameUI, getAllCarsUI, getAllCarByModelNameUI, getAllDiscountCouponsUI, getDiscountCouponByCodeUI, AllBookingDetailsUI

from Delete import DeleteDriverUI, DeleteDriverContactUI, DeleteCustomerByUsernameUI, DeleteLocationByNameUI, DeleteDiscountCouponUI, DeleteCarCategoryByNameUI, DeleteCarRegNoUI, DeleteBookingDetailsUI

from Update import UpdateDriverUI, UpdateDriverContactUI, UpdateCustomerUI, UpdateLocationUI, UpdateCarCategoryUI, UpdateCarUI, UpdateDiscountCouponUI, UpdateBookingDetailsUI

from ManualQuery import ExecuteManualQuery

from Modification import car_booked_on_date

import pandas as pd

st.set_page_config(page_title="Imoto Rental | Home", page_icon=":car:")
st.title("Car Rental Management System")
st.subheader("PES1UG21CS478,PES1UG21CS442")

with st.container():
    AVAILABLE_TABLES = ["Driver Info", "Driver Contacts", "Customer Info", "Locations", "Car Category", "Car Details", "Discount", "Booking Details", "Manual Query", "Modification"]
    AVAILABLE_OPERATIONS = ["CREATE", "READ", "UPDATE", "DELETE"]
    choseTable = st.sidebar.selectbox("Available Tables", options = AVAILABLE_TABLES)
    # st.sidebar.button("Execute Query")
    selected_operation = st.selectbox("Select Operation", options=AVAILABLE_OPERATIONS)
    if choseTable == AVAILABLE_TABLES[0]:
        # st.write(AVAILABLE_TABLES[0])
        with st.container():
            if selected_operation == AVAILABLE_OPERATIONS[0]:
                AddDriverUI()
            elif selected_operation == AVAILABLE_OPERATIONS[1]:
                getAllDriversUI()
                getDriverByDLUI()
            elif selected_operation == AVAILABLE_OPERATIONS[2]:
                UpdateDriverUI()
            elif selected_operation == AVAILABLE_OPERATIONS[3]:
                DeleteDriverUI()
            
    elif choseTable == AVAILABLE_TABLES[1]:
        with st.container():
            if selected_operation == AVAILABLE_OPERATIONS[0]:
                AddDriverContactUI()
            elif selected_operation == AVAILABLE_OPERATIONS[1]:
                getAllDriverContactsUI()
                getDriverContactByDLUI()
            elif selected_operation == AVAILABLE_OPERATIONS[2]:
                UpdateDriverContactUI()
            elif selected_operation == AVAILABLE_OPERATIONS[3]:
                DeleteDriverContactUI()

    elif choseTable == AVAILABLE_TABLES[2]:
        with st.container():
            if selected_operation == AVAILABLE_OPERATIONS[0]:
                AddCustomerUI()
            elif selected_operation == AVAILABLE_OPERATIONS[1]:
                getAllCustomersUI()
                getCustomerByUsernameUI()
            elif selected_operation == AVAILABLE_OPERATIONS[2]:
                UpdateCustomerUI()
            elif selected_operation == AVAILABLE_OPERATIONS[3]:
                DeleteCustomerByUsernameUI()
    elif choseTable == AVAILABLE_TABLES[3]:
        with st.container():
            if selected_operation == AVAILABLE_OPERATIONS[0]:
                AddLocationUI()
            elif selected_operation == AVAILABLE_OPERATIONS[1]:
                getAllLocationsUI()
                getLocationByNameUI()
            elif selected_operation == AVAILABLE_OPERATIONS[2]:
                UpdateLocationUI()
            elif selected_operation == AVAILABLE_OPERATIONS[3]:
                DeleteLocationByNameUI()
    elif choseTable == AVAILABLE_TABLES[4]:
        with st.container():
            if selected_operation == AVAILABLE_OPERATIONS[0]:
                AddCarCategoryUI()
            elif selected_operation == AVAILABLE_OPERATIONS[1]:
                getAllCarCategoriesUI()
                getAllCarCategoryByNameUI()
            elif selected_operation == AVAILABLE_OPERATIONS[2]:
                UpdateCarCategoryUI()
            elif selected_operation == AVAILABLE_OPERATIONS[3]:
                DeleteCarCategoryByNameUI()
    elif choseTable == AVAILABLE_TABLES[5]:
        with st.container():
            if selected_operation == AVAILABLE_OPERATIONS[0]:
                AddCarUI()
            elif selected_operation == AVAILABLE_OPERATIONS[1]:
                getAllCarsUI()
                getAllCarByModelNameUI()
            elif selected_operation == AVAILABLE_OPERATIONS[2]:
                UpdateCarUI()
            elif selected_operation == AVAILABLE_OPERATIONS[3]:
                DeleteCarRegNoUI()
    elif choseTable == AVAILABLE_TABLES[6]:
        with st.container():
            if selected_operation == AVAILABLE_OPERATIONS[0]:
                AddDiscountCouponUI()
            elif selected_operation == AVAILABLE_OPERATIONS[1]:
                getAllDiscountCouponsUI()
                getDiscountCouponByCodeUI()
            elif selected_operation == AVAILABLE_OPERATIONS[2]:
                UpdateDiscountCouponUI()
            elif selected_operation == AVAILABLE_OPERATIONS[3]:
                DeleteDiscountCouponUI()
    elif choseTable == AVAILABLE_TABLES[7]:
        with st.container():
            if selected_operation == AVAILABLE_OPERATIONS[0]:
                AddBookingDetailsUI()
            elif selected_operation == AVAILABLE_OPERATIONS[1]:
                AllBookingDetailsUI()
            elif selected_operation == AVAILABLE_OPERATIONS[2]:
                UpdateBookingDetailsUI()
            elif selected_operation == AVAILABLE_OPERATIONS[3]:
                DeleteBookingDetailsUI()
    elif choseTable == AVAILABLE_TABLES[8]:
        with st.container():
            query = st.text_area("Enter MySQL Query", placeholder="MySql Query")
            if st.button("Execute Query"):
                ExecuteManualQuery(query)
    elif choseTable == AVAILABLE_TABLES[9]:
        st.subheader("Modification")
        st.write("create a prodecudre to dispalay the car booked on specific date  with driver details")
        date = st.date_input("Select Date")
        st.table(pd.DataFrame(car_booked_on_date(str(date))))
        # pd.DataFrame(res[0], columns= res[1])
