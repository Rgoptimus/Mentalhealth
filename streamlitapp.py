import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Display title & Description
st.title("Test Spreadsheet")
st.markdown("This apps will be used for gathering data")

# Establishing a google sheet connection
conn = st.experimental_connection("gsheets", type = GSheetsConnection)

# Fetch existing vendors data
existing_data = conn.read(spreadsheet="https://docs.google.com/spreadsheets/d/1z7UPC-LoZDsNvsVbGv4cYsAM8D65wdIKci3xBXGMTqw/edit?usp=sharing", usecols=list(range(3)), ttl=1)

st.dataframe(existing_data)
