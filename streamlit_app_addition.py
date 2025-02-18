import streamlit as st

st.title("Simple Addition App")

# Input fields for two numbers
number1 = st.number_input("Enter the first number", value=0.0)
number2 = st.number_input("Enter the second number", value=0.0)

# Button to perform the addition
if st.button("Add"):
    result = number1 + number2
    st.write("Result:", result)