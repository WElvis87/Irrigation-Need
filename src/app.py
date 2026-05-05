import joblib
import streamlit as st
from pathlib import Path
import pandas as pd

# Load Model
model = joblib.load("../models/model.pkl")
le = joblib.load("../models/label_encoder.pkl")

st.set_page_config(page_title="Irrigation Need")
st.write("ENTER DETAILS FOR IRRIGATION NEED")

# Input Form

with st.form("Prediction Form"):
    Soil_pH = st.number_input("Soil pH", 0.0, 14.0, 6.5)
    Soil_Moisture = st.number_input("Soil Moisture", 0.0, 100.0, 30.0)
    Organic_Carbon = st.number_input("Organic Carbon", 0.0, 10.0, 1.0)
    Electrical_Conductivity = st.number_input("Electrical Conductivity", 0.0, 10.0, 1.0)
    Temperature_C = st.number_input("Temperature C", 0.0, 50.0, 25.0)
    Humidity = st.number_input("Humidity", 0.0, 100.0, 60.0)
    Rainfall_mm = st.number_input("Rainfall(mm)", 0.0, 500.0, 100.0)
    Sunlight_Hours = st.number_input("Sunlight Hours", 0.0, 24.0, 8.0)
    Wind_Speed_kmh = st.number_input("Wind Speed kmh", 0.0, 100.0, 10.0)
    Field_Area_hectare = st.number_input("Field Area (hectare)", 0.0, 100.0, 1.0)
    Previous_Irrigation_mm = st.number_input("Previous Irrigation(mm)", 0.0, 500.0, 50.0)
    Soil_Type = st.selectbox("Soil Type", ["Sandy", "Clay", "Loamy", "Silt"])
    Crop_Type = st.selectbox("Crop Type", ["Sugarcane", "Rice", "Cotton", "Maize", "Wheat", "Potato"])
    Crop_Growth_Stage = st.selectbox("Crop Growth Stage", ["Harvest", "Flowering", "Vegetative", "Sowing"])
    Season = st.selectbox("Season", ["Kharif", "Rabi", "Zaid"])
    Irrigation_Type = st.selectbox("Irrigation Type", ["Canal", "Sprinkler", "Rainfed", "Drip"])
    Water_Source = st.selectbox("Water Source", ["Reservoir", "River", "Groundwater", "Rainwater"])
    Mulching_Used = st.selectbox("Mulching Used", ["No", "Yes"])
    Region = st.selectbox("Region", ["South", "West", "East", "Central", "North"])

    submit = st.form_submit_button("Predict")

if submit:
    try:
        input_data = pd.DataFrame([{
            "Soil_pH": Soil_pH,
            "Soil_Moisture": Soil_Moisture,
            "Organic_Carbon": Organic_Carbon,
            "Electrical_Conductivity": Electrical_Conductivity,
            "Temperature_C": Temperature_C,
            "Humidity": Humidity,
            "Rainfall_mm": Rainfall_mm,
            "Sunlight_Hours": Sunlight_Hours,
            "Wind_Speed_kmh": Wind_Speed_kmh,
            "Field_Area_hectare": Field_Area_hectare,
            "Previous_Irrigation_mm": Previous_Irrigation_mm,
            "Soil_Type": Soil_Type,
            "Crop_Type": Crop_Type,
            "Crop_Growth_Stage": Crop_Growth_Stage,
            "Season": Season,
            "Irrigation_Type": Irrigation_Type,
            "Water_Source": Water_Source,
            "Mulching_Used": Mulching_Used,
            "Region": Region
        }])

        # Make Prediction
        prediction_encoded = model.predict(input_data)

        # Irrigation Need
        prediction = le.inverse_transform([prediction_encoded[0]])
        
        # Output
        st.success(f"Irrigation Need: {prediction[0]}")

    except Exception as e:
        st.error(f"Failed to make prediction {e}")