import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load('house_model.pkl')

st.title("🇪🇬 Egyptian Housing Price Predictor")

# Define the inputs
rooms = st.number_input("Number of Rooms", min_value=1, max_value=10, value=3)
baths = st.number_input("Number of Bathrooms", min_value=1, max_value=5, value=2)
area = st.number_input("Area (m²)", min_value=30, max_value=1000, value=120)
floor = st.number_input("Floor Level", min_value=0, max_value=20, value=1)
finishing = st.selectbox("Finishing Type", [ "سوبر لوكس","نصف تشطيب","اكسترا سوبر لوكس","بدون تشطيب","لوكس"])
governate = st.selectbox("Governate", ["العين السخنة","الساحل الشمالي","الاسكندرية","الجيزة","القاهرة الكبرى","الدقهلية","البحر الأحمر",
    "الشرقية",
    "التوسعات السياحية الشمالية",
    "دمياط",
    "مرسى مطروح",
    "السويس",
    "بور سعيد",
    "المنيا",
    "الاسماعيلية",
    "القليوبية",
    "المنوفية"]) 

# Prediction Button
if st.button("Predict Price"):
    input_df = pd.DataFrame([{
        'Rooms': rooms,
        'Baths': baths,
        'Area': area,
        'Lat': 30.0, 
        'Lon': 31.0,
        'Floor': floor,
        'Finishing': finishing,
        'Governate': governate
    }])
    
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Price: EGP {prediction:,.2f}")