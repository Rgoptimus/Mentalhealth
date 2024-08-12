# example/st_app_gsheets_using_service_account.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("Read Google Sheet as DataFrame")

conn = st.experimental_connection("gsheets", type=GSheetsConnection)
df = conn.read(spreadsheet="https://docs.google.com/spreadsheets/d/1z7UPC-LoZDsNvsVbGv4cYsAM8D65wdIKci3xBXGMTqw/edit?gid=0#gid=0", worksheet="Sheet1")

st.dataframe(df)
