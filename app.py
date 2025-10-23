import streamlit as st
import numpy as np
import pickle

with open('rainfall_model.pkl', 'rb') as f:
    model_data = pickle.load(f)

model = model_data.get('model') if isinstance(model_data, dict) else model_data

st.title("Rainfall Prediction")

pressure = st.number_input("Pressure (hPa)", 900, 1050, 1015)
dewpoint = st.number_input("Dew Point (°C)", -10, 40, 20)
humidity = st.slider("Humidity (%)", 0, 100, 70)
cloud = st.slider("Cloud Coverage (%)", 0, 100, 50)
sunshine = st.slider("Sunshine Hours", 0, 24, 5)
winddirection = st.slider("Wind Direction (°)", 0, 360, 90)
windspeed = st.number_input("Wind Speed (km/h)", 0, 200, 10)

input_data = np.array([[pressure, dewpoint, humidity, cloud, sunshine, winddirection, windspeed]])

if st.button("Predict Rainfall"):
    prediction = model.predict(input_data)
    result = "Rainfall" if prediction[0] == 1 else "No Rainfall"
    st.write(f"Prediction: {result}")