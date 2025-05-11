# <!-- Project 8: Create a Python Streamlit BMI Calculator Web App in Just 6 Minutes -->

import streamlit as st
import pandas as pd

st.title("BMI Calculator")
st.write("This app calculates your Body Mass Index (BMI) based on your height and weight.")

height = st.slider("Height (cm)", 100,250,175)
weight = st.slider("Weight (kg)", 40,200,70)

bmi = weight / ((height / 100) ** 2)
st.write(f"Your BMI is: {bmi:.2f}")
st.write("### BMI Categories: ###")
st.write("- Underweight: BMI < 18.5")
st.write("- Normal weight: BMI 18.5–24.9")
st.write("- Overweight: BMI 25–29.9")
st.write("- Obesity: BMI ≥ 30")
