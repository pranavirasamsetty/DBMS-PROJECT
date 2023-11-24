from CarRenatlBackend import cursor, db
from Setup import DB_NAME
import streamlit as st
from Read import getAllDrivers, getAllDriverContacts, getAllCustomers, getAllLocations, getAllCarCategories, getAllCars, getAllDiscountCoupons, AllBookingDetails
import pandas as pd

def DeleteDriverUI():
    with st.expander("Before Deleting"):
        st.table(pd.DataFrame(getAllDrivers()))
    with st.container():
        selected_drivers = st.multiselect("Select DL's to be deleted", [driver["DL"] for driver in getAllDrivers()])
        if st.button("Delete"):
            for dl in selected_drivers:
                DeleteDriver(dl)


def DeleteDriver(dl):
    cursor.execute(f"use {DB_NAME}")
    query = ("delete from driver_info where dl_number = %s")
    cursor.execute(query, (dl,))
    db.commit()
    st.success("Driver's data deleted successfully", icon="✅")
    with st.expander("After Deleting"):
        st.table(getAllDrivers())

# ---------------------------------------------------------------------------------------------------------------------------
# Driver's Contacts
# ---------------------------------------------------------------------------------------------------------------------------

def DeleteDriverContactUI():
    with st.expander("Before Deleting"):
        st.table(getAllDriverContacts())
    with st.container():
        selected_contacts = st.multiselect("Select Contact's to be deleted", [driver["Contact"] for driver in getAllDriverContacts()])
        if st.button("Delete"):
            for contact in selected_contacts:
                DeleteDriverContact(contact)

def DeleteDriverContact(contact):
    cursor.execute(f"use {DB_NAME}")
    query = ("delete from driver_contacts where phone_no = %s")
    cursor.execute(query, (contact,))
    db.commit()
    st.success("Driver's Contact deleted successfully", icon="✅")
    with st.expander("After Deleting"):
        st.table(pd.DataFrame(getAllDriverContacts()))


# ---------------------------------------------------------------------------------------------------------------------------
# Customer Details
# ---------------------------------------------------------------------------------------------------------------------------
def DeleteCustomerByUsernameUI():
    with st.expander("Before Deleting"):
        st.table(getAllCustomers())
    with st.container():
        selected_customers = st.multiselect("Select Customer's Username to be deleted", [customer["Username"] for customer in getAllCustomers()])
        if st.button("Delete"):
            for customer in selected_customers:
                DeleteCustomerByUsername(customer)

def DeleteCustomerByUsername(username):
    cursor.execute(f"use {DB_NAME}")
    query = ("delete from customer_info where username = %s")
    cursor.execute(query, (username,))
    db.commit()
    st.success("Customer details deleted successfully", icon="✅")
    with st.expander("After Deleting"):
        st.table(pd.DataFrame(getAllCustomers()))

# -----------------------------------------------------------------------------------------------------------------------------
# Location details
# -----------------------------------------------------------------------------------------------------------------------------
def DeleteLocationByNameUI():
    with st.expander("Before Deleting"):
        st.table(getAllLocations())
    with st.container():
        selected_locations = st.multiselect("Select Location Name to be deleted", [location["Location Name"] for location in getAllLocations()])
        if st.button("Delete"):
            for location in selected_locations:
                DeleteLocationByName(location)

def DeleteLocationByName(location_name):
    cursor.execute(f"use {DB_NAME}")
    query = ("delete from locations where location_name = %s")
    cursor.execute(query, (location_name,))
    db.commit()
    st.success("Location details deleted successfully", icon="✅")
    with st.expander("After Deleting"):
        st.table(pd.DataFrame(getAllLocations()))

# ---------------------------------------------------------------------------------------------------------------------------------
# Car Category
# ---------------------------------------------------------------------------------------------------------------------------------

def DeleteCarCategoryByNameUI():
    with st.expander("Before Deleting"):
        st.table(getAllCarCategories())
    with st.container():
        selected_category = st.multiselect("Select Category Name to be deleted", [category["Name"] for category in getAllCarCategories()])
        if st.button("Delete"):
            for category in selected_category:
                DeleteCarCategoryByName(category)

def DeleteCarCategoryByName(category_name):
    cursor.execute(f"use {DB_NAME}")
    query = ("delete from car_category where category_name = %s")
    cursor.execute(query, (category_name,))
    db.commit()
    st.success("Car Category details deleted successfully", icon="✅")
    with st.expander("After Deleting"):
        st.table(pd.DataFrame(getAllCarCategories()))

# -----------------------------------------------------------------------------------------------------------------------------------------------
# Car details
# -----------------------------------------------------------------------------------------------------------------------------------------------

def DeleteCarRegNoUI():
    with st.expander("Before Deleting"):
        st.table(getAllCars())
    with st.container():
        selected_regNo = st.multiselect("Select Reg No. to be deleted", options=[car["Registration No"] for car in getAllCars()])
        if st.button("Delete"):
            for reg_no in selected_regNo:
                DeleteCarRegNo(reg_no)

def DeleteCarRegNo(reg_no):
    cursor.execute(f"use {DB_NAME}")
    query = ("delete from car_details where registration_no = %s")
    cursor.execute(query, (reg_no,))
    db.commit()
    st.success("Car details deleted successfully", icon="✅")
    with st.expander("After Deleting"):
        st.table(pd.DataFrame(getAllCars()))

# -----------------------------------------------------------------------------------------------------------------------------------------------
# Cadiscountr details
# -----------------------------------------------------------------------------------------------------------------------------------------------

def DeleteDiscountCouponUI():
    with st.expander("Before Deleting"):
        st.table(getAllDiscountCoupons())
    with st.container():
        selected_coupon = st.multiselect("Select Coupon Code to be deleted", options=[coupon["coupon_code"] for coupon in getAllDiscountCoupons()])
        if st.button("Delete"):
            for code in selected_coupon:
                DeleteDiscountCoupon(code)

def DeleteDiscountCoupon(code):
    cursor.execute(f"use {DB_NAME}")
    query = ("delete from discount where coupon_code = %s")
    cursor.execute(query, (code,))
    db.commit()
    st.success("Discount Coupon details deleted successfully", icon="✅")
    with st.expander("After Deleting"):
        st.table(pd.DataFrame(getAllDiscountCoupons()))

# ----------------------------------------------------------------------------------------------------------------------------------------------------
# Booking Details
# ----------------------------------------------------------------------------------------------------------------------------------------------------
def DeleteBookingDetailsUI():
    with st.expander("Before Deleting"):
        st.table(AllBookingDetails())
    with st.container():
        selected_booking = st.multiselect("Select Booking Id to be deleted", options=[booking["Booking Id"] for booking in AllBookingDetails()])
        if st.button("Delete"):
            for booking_id in selected_booking:
                DeleteBookingDetails(booking_id)

def DeleteBookingDetails(booking_id):
    cursor.execute(f"use {DB_NAME}")
    query = ("delete from booking_details where booking_id = %s")
    cursor.execute(query, (booking_id,))
    db.commit()
    st.success("Booking details deleted successfully", icon="✅")
    with st.expander("After Deleting"):
        st.table(pd.DataFrame(AllBookingDetails()))