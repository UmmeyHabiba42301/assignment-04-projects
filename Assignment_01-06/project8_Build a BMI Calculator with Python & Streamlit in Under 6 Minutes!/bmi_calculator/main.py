import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="🧮", layout="centered")

st.title("🧮 BMI Calculator")
st.markdown("Calculate your Body Mass Index (BMI) instantly.")

# Input fields
height = st.number_input("Enter your height (in cm):", min_value=50.0, max_value=300.0, value=170.0)
weight = st.number_input("Enter your weight (in kg):", min_value=10.0, max_value=300.0, value=70.0)

if st.button("Calculate BMI"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    
    st.subheader(f"Your BMI is: **{bmi:.2f}**")
    
    if bmi < 18.5:
        st.info("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")
