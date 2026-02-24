import streamlit as st
import joblib
import pandas as pd

model = joblib.load("car_pipeline.pkl")
st.title("🚗 Ford Car Price Predictor")

year = st.number_input("Year (e.g. 2019)")
mileage = st.number_input("Mileage (e.g. 42000 km)")
engineSize = st.number_input("Engine Size (e.g. 1.5L)")
tax = st.number_input("Tax (e.g. 150(in pounds))")
mpg = st.number_input("MPG (e.g. 55)")

model_name = st.selectbox("Model", [" Fiesta"," Focus"," Kuga"," EcoSport"])
transmission = st.selectbox("Transmission", ["Manual","Automatic"])
fuel = st.selectbox("Fuel Type", ["Petrol","Diesel"])

if st.button("Predict"):

    input_df = pd.DataFrame([{
        "year": year,
        "mileage": mileage,
        "engineSize": engineSize,
        "tax": tax,
        "mpg": mpg,
        "model": model_name,
        "transmission": transmission,
        "fuelType": fuel
    }])

    price = model.predict(input_df)

    st.success(f"Predicted Price: ₹ {price[0]:,.0f} pounds")