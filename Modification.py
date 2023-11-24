from CarRenatlBackend import cursor, db
from Setup import DB_NAME
import streamlit as st

def formatData(data):
    result = []
    for i in data:
        format1 = {}
        format1["Car RegNo"] = i[0]
        format1["DL No."] = i[1]
        format1["Driver Name"] = i[2]
        format1["DOB"] = i[3]
        format1["Experience"] = i[4]
        format1["Available"] = i[5]
        format1["Booking Date"] = i[6]
        result.append(format1)

    return result

def car_booked_on_date(date):
    cursor.execute(f"use {DB_NAME}")
    query = f'CALL car_rental.car_booked_on_date({date});'

    cursor.execute(query)
    #cursor.callproc("car_booked_on_date", args=(date,))
    data = []
    for result in cursor.stored_results():
        data.append(result.fetchall())
    results = data[0]
    # st.write(cursor.description)
    # st.write(results)
    return formatData(results)
    
    # columns=[col[0] for col in cursor.description]
    # return (data, columns)