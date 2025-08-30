import streamlit as st

st.title("Unit Convertor App")
st.markdown("### Converts Length, Weight and Time")
st.write("Welcome! Select a category, enter a value and get the converted result in real-time.")

category = st.selectbox("Choose a category", ["Length", "Width", "Time"])

def convert_units(category, value , unit):
    if category == "Length":
        if unit == "Kilometers to miles":
             return value * 0.621371
        elif category =="Miles to kilometers":
            return value / 0.621371
        
    elif category == "Width":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif  unit == "Pounds to Kilogram":
            return value / 2.20462
        
    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60 
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24
    return 0

if category == "Length":
    unit = st.selectbox("Select Conversation ", ["Kilometers to miles", "Miles to kilometers"])

elif category == "Width":
    unit = st.selectbox("Slect Conversation ", ["Kilograms to Pounds", "Pounds to Kilogram" ])

elif category == "Time":
    unit = st.selectbox("Selct Conversation", ["Seconds to Minutes","Minutes to Seconds", "Minutes to Hours","Hours to Minutes", "Hours to Days", "Days to Hours" ])

value = st.number_input("Enter The Value To Convert")

if st.button("Convert"):
    result = convert_units(category ,  value, unit)
    st.success(f"The result is {result:.2f}")