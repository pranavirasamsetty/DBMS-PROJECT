import streamlit as st
import datetime
from CarRenatlBackend import cursor, db
from Setup import DB_NAME
import pandas as pd
from Read import getAllDrivers, getAllCarCategories, getAllLocations, getAllCustomers, getCustomerByUsername, getAllCarsWithCategory, getAllLocations, getLocationByName, getAllDiscountCoupons, getAVailableDrivers, getDiscountCouponByCode, getDriverCost, getDriverByDL

def AddDriverUI():
    driverdata = {}
    with st.container():
        st.write("Add Driver Details")
        dl_numberUI, driver_dobUI = st.columns([3, 2])
        driver_nameUI, driver_experienceUI = st.columns(2)

        dl_number = dl_numberUI.text_input(
            label="Driving License Number", placeholder="Enter Driving License No.",  max_chars=16)
        driver_dob = driver_dobUI.date_input(label="Date of birth", min_value=datetime.date(
            1950, 1, 1), max_value=datetime.date.today())
        driver_name = driver_nameUI.text_input(
            label="Driver's Name", placeholder="Driver's Name")
        driver_experience = driver_experienceUI.number_input(
            "Driving Experience", min_value=2)
        driver_available = st.selectbox(
            "Availability", options=[True, False])

        driverdata["dl_number"] = dl_number
        driverdata["driver_dob"] = str(driver_dob)
        driverdata["driver_name"] = driver_name
        driverdata["driver_experience"] = driver_experience
        driverdata["driver_available"] = driver_available

        if st.button("Add Driver"):
            if driverdata["dl_number"]:
                AddDriver(driverdata=driverdata)
            else:
                st.warning("License No. is mandatory", icon="⚠️")
                return

def AddDriver(driverdata):
    cursor.execute(f"use {DB_NAME}")
    query = ("insert into driver_info values(%s, %s, %s, %s, %s)")
    cursor.execute(query, (driverdata["dl_number"], driverdata["driver_name"],
                   driverdata["driver_dob"], driverdata["driver_experience"], driverdata["driver_available"],))
    db.commit()
    st.success("Driver's data added successfully", icon="✅")

def AddDriverContactUI():
    with st.container():
        licenseNoUI, contactUI = st.columns([3, 2])
        selected_driver = licenseNoUI.selectbox("Select Driver To Add Contact", options=[driver["DL"] for driver in getAllDrivers()])
        contact = contactUI.text_input("Enter Phone Number", placeholder="Enter Phone Number", max_chars=10, )
        if st.button("Add Contact"):
            AddDriverContact({"dl_number": selected_driver, "contact_no": contact})

def AddDriverContact(driverdata):
    cursor.execute(f"use {DB_NAME}")
    query = ("insert into driver_contacts values(%s, %s)")
    cursor.execute(query, (driverdata["dl_number"], driverdata["contact_no"],))
    db.commit()
    st.success("Driver's Contact added successfully", icon="✅")


def validateRegister(userdata):
    if not userdata["firstname"]:
        st.warning("Firstname cannot be Empty", icon="⚠️")
        return
    if not userdata["lastname"]:
        st.warning("Lastname cannot be Empty", icon="⚠️")
        return
    if userdata["licenseNo"] and len(userdata["licenseNo"]) != 16:
        st.warning("License No. must be 16 characters", icon="⚠️")
        return
    if not userdata["licenseNo"]:
        userdata["licenseNo"] = None
    if not userdata["email"]:
        userdata["email"] = None
    if not userdata["dob"]:
        st.warning("Date of birth cannot be Empty", icon="⚠️")
        return
    if not userdata["username"]:
        st.warning("Username cannot be Empty", icon="⚠️")
        return
    if userdata["password"] != userdata['confirmPassword'] and len(userdata["password"]) > 3:
        st.warning("Both passwords must match and password length > 3", icon="⚠️")
        return
    if not userdata["state"]:
        st.warning("State cannot be Empty", icon="⚠️")
        return
    if not userdata["city"]:
        st.warning("City cannot be Empty", icon="⚠️")
        return
    if not userdata["street"]:
        st.warning("Street cannot be Empty", icon="⚠️")
        return
    if not userdata["zipcode"]:
        st.warning("Street cannot be Empty", icon="⚠️")
        return
    # st.write(userdata)
    RegisterUser(userdata)
    # st.success('Registered Successfully!', icon="✅")
    return
    # st.info("Please Login with username and password!", icon="ℹ️")

def AddCustomerUI():
    registerContainer = st.container()
    with registerContainer:
        firstnameUI, lastnameUI = st.columns(2)
        licenseNoUI, dobUI = st.columns([3, 2])
        usernameUI, phoneNoUI = st.columns(2)
        passwordUI, confirmPasswordUI = st.columns(2)
        stateUI, cityUI = st.columns(2)
        zipcodeUI, streetUI = st.columns(2)

        userdata = {}

        userdata["firstname"] = firstnameUI.text_input(
            label="Firstname", placeholder="Enter Firstname")
        userdata["lastname"] = lastnameUI.text_input(
            label="Lastname", placeholder="Enter Lastname")
        userdata["licenseNo"] = licenseNoUI.text_input(
            label="Driving License Number", placeholder="Enter Driving License No.",  max_chars=16)
        userdata["dob"] = dobUI.date_input(label="Date of birth", min_value=datetime.date(
            1950, 1, 1), max_value=datetime.date.today())
        userdata["dob"] = str(userdata["dob"])
        userdata["username"] = usernameUI.text_input(
            label="Username", placeholder="Enter Username")
        userdata["phoneNo"] = phoneNoUI.text_input(
            label="Mobile No", placeholder="Enter Mobile No", max_chars=10)
        userdata["password"] = passwordUI.text_input(
            label="Password", type="password")
        userdata["confirmPassword"] = confirmPasswordUI.text_input(
            label="Confirm Password", type="password")
        userdata["email"] = st.text_input(
            label="Email", placeholder="Enter Email")
        userdata["state"] = stateUI.text_input(
            label="State", placeholder="Enter State")
        userdata["city"] = cityUI.text_input(
            label="City", placeholder="Enter City")
        userdata["street"] = streetUI.text_input(
            label="Street", placeholder="Enter Street")
        userdata["zipcode"] = zipcodeUI.text_input(
            label="Zipcode", max_chars=5, placeholder="Enter Zipcode")
        if st.button("Register"):
            if validateRegister(userdata):
                RegisterUser(userdata)


def RegisterUser(userdata):
    cursor.execute(f"use {DB_NAME}")
    query = (
        "insert into customer_info("
        "dl_number, firstname, lastname, phone_no, username, password, dob, email, state, city, street, zipcode"
        ")"
        "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    )

    cursor.execute(query, (
        userdata["licenseNo"],
        userdata["firstname"],
        userdata["lastname"],
        userdata["phoneNo"],
        userdata["username"],
        userdata["password"],
        userdata["dob"],
        userdata["email"],
        userdata["state"],
        userdata["city"],
        userdata["street"],
        userdata["zipcode"],
    ))
    db.commit()
    st.success('Registered Successfully!', icon="✅")

# ------------------------------------------------------------------------------------------------------------------
# Locations
# ------------------------------------------------------------------------------------------------------------------

def AddLocationUI():
    location_name = st.text_input("Location Name", placeholder="Enter Location Name")
    stateUI, zipcodeUI, cityUI = st.columns([3, 1, 1])
    state = stateUI.text_input("State", placeholder="State")
    zipcode = zipcodeUI.text_input("Zipcode", placeholder="Zipcode", max_chars=5)
    city = cityUI.text_input("City", placeholder="City")
    street = st.text_input("Street", placeholder="Street")

    location = {
        "location_name": location_name,
        "state": state,
        "zipcode": zipcode,
        "street": street,
        "city": city
    }

    if st.button("Add Location"):
        # st.write(location)
        AddLocation(location)
    
def AddLocation(location):
    cursor.execute(f"use {DB_NAME}")
    query = (
        "insert into locations("
        "location_name, state, city, street, zipcode"
        ")"
        "values(%s, %s, %s, %s, %s)"
    )
    cursor.execute(query, (location["location_name"], location["state"], location["city"], location["street"], location["zipcode"]))
    db.commit()
    st.success('Location Added Successfully!', icon="✅")

# -------------------------------------------------------------------------------------------------------------------------------------------
# Car Category
# -------------------------------------------------------------------------------------------------------------------------------------------
def AddCarCategoryUI():
    with st.container():
        categoryNameUI, noOfPersonUI = st.columns([2,1])
        costPerDayUI, lateFeePerDayUI = st.columns(2)

        category_name = categoryNameUI.text_input("Category Name", placeholder="Category Name")
        noOfPerson = noOfPersonUI.number_input("No Of Persons.", min_value=2)
        costPerDay = costPerDayUI.number_input("Cost Per Day", min_value=400)
        lateFeePerDay = lateFeePerDayUI.number_input("Late Fee Per Day", min_value=50)
        category = {
            "category_name": category_name,
            "noOfPerson": noOfPerson,
            "costPerDay": costPerDay,
            "lateFeePerDay": lateFeePerDay
        }
        if st.button("Add Car Category"):
            # st.write(category)
            AddCarCategory(category= category)

def AddCarCategory(category):
    cursor.execute(f"use {DB_NAME}")
    query = (
        "insert into car_category("
        "category_name, no_persons, cost_per_day, late_fee_per_hour"
        ")"
        "values(%s, %s, %s, %s)"
    )
    cursor.execute(query, (category["category_name"], category["noOfPerson"], category["costPerDay"], category["lateFeePerDay"],))
    db.commit()
    st.success('Car Category Added Successfully!', icon="✅")

# ------------------------------------------------------------------------------------------------------------------------------------
# Car Details
# ------------------------------------------------------------------------------------------------------------------------------------
def AddCarUI():
    with st.container():
        registration_noUI, model_nameUI = st.columns(2)
        makeUI, model_yearUI = st.columns(2)
        mileageUI, availableUI = st.columns(2)
        categoryUI, car_locationUI = st.columns(2)
        
        registration_no = registration_noUI.text_input("Car Registration No.", max_chars= 6, placeholder="Car Registration No.")
        model_name = model_nameUI.text_input("Model Name", placeholder="Model Name")
        make = makeUI.text_input("Make", placeholder="Make")
        mileage = mileageUI.number_input("Mileage", min_value= 2)
        model_year = model_yearUI.text_input("Model Year")
        available = availableUI.selectbox("Available", options=[True, False], index = 0)
        category = categoryUI.selectbox("Car Category", options=[category["Name"] for category in getAllCarCategories()])
        location = car_locationUI.selectbox("Car Location", options=[location["Location Name"] for location in getAllLocations()])

        car_details = {}
        car_details["registration_no"] = registration_no
        car_details["model_name"] = model_name
        car_details["make"] = make
        car_details["mileage"] = mileage
        car_details["model_year"] = model_year
        car_details["available"] = available
        car_details["category"] = category
        car_details["location"] = location


        if st.button("Add Car"):
            # st.write(category)
            AddCar(car_details= car_details)

def AddCar(car_details):
    # st.write(car_details)
    cursor.execute(f"use {DB_NAME}")
    query = (
        "insert into car_details("
        "registration_no, model_name, make, model_year, mileage, available, category, car_location"
        ")"
        "values(%s, %s, %s, %s, %s, %s, %s, %s)"
    )
    locationId = None
    for location in getAllLocations():
        if location["Location Name"] == car_details["location"]:
            locationId = location["Location Id"]
    cursor.execute(query, (car_details["registration_no"], car_details["model_name"], car_details["make"], car_details["model_year"], car_details["mileage"], car_details["available"], car_details["category"], locationId,))
    db.commit()
    st.success('Car Added Successfully!', icon="✅")


# ---------------------------------------------------------------------------------------------------------------------------------------------
# Discount
# ---------------------------------------------------------------------------------------------------------------------------------------------

def AddDiscountCouponUI():
    with st.container():
        coupon_codeUI, coupon_nameUI = st.columns(2)
        discount_percentageUI, expiry_dateUI = st.columns(2)

        coupon_name = coupon_nameUI.text_input("Coupon Name", placeholder="Coupon Name")
        coupon_code = coupon_codeUI.text_input("Coupon Code", placeholder="Coupon Code", max_chars=4)
        discount_percentage = discount_percentageUI.number_input("Discount %")
        expiry_date = expiry_dateUI.date_input("Expiry Date")

        discount = {
            "coupon_name": coupon_name,
            "coupon_code": coupon_code,
            "discount_percentage": discount_percentage,
            "expiry_date": str(expiry_date)
        }

        if st.button("Add Coupon"):
            AddDiscountCoupon(discount)

def AddDiscountCoupon(discount_data):
    cursor.execute(f"use {DB_NAME}")
    query = (
        "insert into discount("
        "coupon_code, coupon_name, discount_percentage, expiry_date"
        ")"
        "values(%s, %s, %s, %s)"
    )
    cursor.execute(query, (discount_data["coupon_code"], discount_data["coupon_name"], discount_data["discount_percentage"], discount_data["expiry_date"]))
    db.commit()
    st.success('Discount Coupon Added Successfully!', icon="✅")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Booking Details
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
def NoOfDays(fromDate, toDate):
    fromDate = datetime.datetime.strptime(fromDate, "%Y-%m-%d")
    toDate = datetime.datetime.strptime(toDate, "%Y-%m-%d")
    delta = toDate - fromDate
    # print("No of days: ",delta)
    return float(delta.days + 1)

def getCarFare(cars, regNo, fromDate, toDate, discount):

     for car in cars:
        if car["RegistrationNo"] == regNo:
            cost = NoOfDays(fromDate, toDate) * car["CostPerDay"]
            return cost - cost * (discount/100)

def AddBookingDetailsUI():
    
    user_selected = st.selectbox("Select User", options = [user["Username"] for user in getAllCustomers()])
    all_locations = getAllLocations()
    available_cars = getAllCarsWithCategory()
    with st.expander("Available cars"):
        st.table(pd.DataFrame(available_cars))
    fromDateUI, toDateUI = st.columns(2)
    couponUI, carRegNoUI = st.columns(2)
    pickUpUI, dropUI = st.columns(2)
    fromDate = fromDateUI.date_input(
                label="From",
                min_value=datetime.date.today(),
            )
    toDate = toDateUI.date_input(
                label="To",
                min_value=datetime.date.today(),
            )
    coupon = couponUI.selectbox("Discount Coupons", [coupon["coupon_code"] for coupon in getAllDiscountCoupons()])
    carRegNo = carRegNoUI.selectbox("Select Car Reg No.", [car["RegistrationNo"] for car in available_cars])
    pickUp = pickUpUI.selectbox("Pick Up Location", options=[location["Location Name"] for location in all_locations])
    drop = dropUI.selectbox("Drop Location", options=[location["Location Name"] for location in all_locations])
    with_driver = st.checkbox("Do you want Driver", value=False)
    booking_data = {}
    if with_driver:
        st.info("Additional amount will be charged for driver per day", icon="ℹ️")
        available_drivers = getAVailableDrivers()
        with st.expander("Available Drivers"):
            st.table(pd.DataFrame(available_drivers))
        selected_driver = st.selectbox("Available Drivers", options=[driver["DL"] for driver in available_drivers])
        booking_data["driver_dl"] = selected_driver
        

    
    booking_data["user_id"] = getCustomerByUsername(user_selected)[0]["Customer ID"]
    booking_data["from"] = str(fromDate)
    booking_data["to"] = str(toDate)
    booking_data["coupon"] = coupon
    booking_data["with_driver"] = with_driver
    booking_data["reg_no"] = carRegNo
    booking_data["discount"] = getDiscountCouponByCode(coupon)[0]["discount_percentage"]
    booking_data["pickUp"] = getLocationByName(pickUp)[0]["Location Id"]
    booking_data["drop"] = getLocationByName(drop)[0]["Location Id"]
    booking_data["basic_fare"] = getCarFare(available_cars, carRegNo, str(fromDate), str(toDate), booking_data["discount"])
    # st.write(booking_data)
    if booking_data["basic_fare"]:
        driverCost = (0,)
        if booking_data["with_driver"]:
            driverCost = getDriverCost(getDriverByDL(booking_data["driver_dl"])[0]["Experience"])
        # st.write(driverCost)
        # st.write(booking_data["basic_fare"])
        # st.write(NoOfDays(booking_data["from"], booking_data["to"]))

        st.info(f'Basic Fare ₹{booking_data["basic_fare"] + NoOfDays(booking_data["from"], booking_data["to"])*driverCost[0]}', icon="ℹ️")

    if st.button("Confirm Booking"):
        # st.write(booking_data)
        AddBookingDetails(booking_data)

def AddBookingDetails(booking_data):
    cursor.execute(f"use {DB_NAME}")
    query = (
        "insert into booking_details("
        "from_date, return_date, with_driver, booking_status, pickup_location, drop_location, coupon_code, car_reg_no, customer_id, basic_fare, discount_percentage"
        ")"
        "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    )
    cursor.execute(query, (booking_data["from"], booking_data["to"], booking_data["with_driver"], True, booking_data["pickUp"], booking_data["drop"], booking_data["coupon"], booking_data["reg_no"], booking_data["user_id"], booking_data["basic_fare"], booking_data["discount"]))
    booking_id = cursor.lastrowid
    db.commit()
    if booking_data["with_driver"]:
        query = ("insert into booking_with_driver(driver_dl, customer_id, booking_id) values(%s, %s, %s)")
        cursor.execute(query, (booking_data["driver_dl"], booking_data["user_id"], booking_id))
        db.commit()
    st.success('Booking Confirmed!', icon="✅")
    st.balloons()
 

