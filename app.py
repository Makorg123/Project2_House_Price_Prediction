import numpy as np
import pandas as pd
import streamlit as st
from prediction import predict

st.title('Predicting the price of a house')
st.markdown('Model to predict the price of a house based on its features')

st.header('House features')
col1, col2, col3, col4= st.columns(4)
with col1:
    area = st.number_input('Area: 1650 to 16200')
    bedrooms = st.number_input('No. of bedrooms:1 to 6')
    bathrooms = st.number_input('No. of bathrooms: 1 to 4')
with col2:
    stories = st.number_input('No. of stories: 1 to 4')
    parking = st.number_input('Parking space: 0 to 3')
    mainroad = st.number_input('Main road: 0 or 1')
with col3: 
    guestroom = st.number_input('Guest room: 0 or 1')
    basement = st.number_input('Basement: 0 or  1')
    hotwaterheating = st.number_input('Hot water heating: 0 or 1')
with col4:
    airconditioning = st.number_input('Air conditioning: 0 or 1')
    prefarea = st.number_input('Preferred area: 0 or 1')
    furnishingstatus = st.number_input('Furnishing status: 0, 1 or 2')

if st.button("Predict Price of House"):
    data = np.array([area, bedrooms	, bathrooms	, stories, parking, mainroad, guestroom, basement, hotwaterheating, airconditioning, prefarea, furnishingstatus])
    data = pd.DataFrame(data.reshape(-1, len(data)), columns=['area', 'bedrooms', 'bathrooms', 'stories', 'parking','mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea', 'furnishingstatus'])
    st.write(data)
    prediction = predict(data)
    st.header(f'Predicted price of house is {prediction[0]}')