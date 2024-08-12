# Import the Streamlit library
import streamlit as st

# Set the title of the app
st.title('Simple Streamlit App')

# Create a text input box
user_input = st.text_input("Enter your name:")

# Create a button that updates the app when clicked
if st.button('Submit'):
    if user_input:
        st.write(f"Hello, {user_input}!")
    else:
        st.write("Please enter your name.")
