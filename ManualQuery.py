import streamlit as st
from CarRenatlBackend import cursor, db
from Setup import DB_NAME
import pandas as pd

def ExecuteManualQuery(query):
    cursor.execute(f'use {DB_NAME}')
    str(query).replace(";", '')
    if "select" in str(query).lower():
        cursor.execute(query)
        res = cursor.fetchall()
        # st.write(cursor.description)
        st.table(pd.DataFrame(res, columns=[col[0] for col in cursor.description]))

    elif "insert" in str(query).lower():
        cursor.execute(query)
        res = cursor.fetchall()
        db.commit()
        st.success(f'inserted successfully with id {cursor.lastrowid}', icon="✅")
        # st.table(pd.DataFrame(res, columns=[col[0] for col in cursor.description]))

    elif "update" in str(query).lower():
        cursor.execute(query)
        res = cursor.fetchall()
        st.success(f'updated successfully', icon="✅")
        db.commit()
        # st.table(pd.DataFrame(res, columns=[col[0] for col in cursor.description]))

    elif "delete" in str(query).lower():
        cursor.execute(query)
        res = cursor.fetchall()
        db.commit()
        st.success(f'deleted successfully', icon="✅")
        # st.table(pd.DataFrame(res, columns=[col[0] for col in cursor.description]))