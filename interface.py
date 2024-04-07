import pickle
import streamlit as st

# Load the model
pickle_in = open('forecast.pkl', 'rb')
clf = pickle.load(pickle_in)

st.header("Streamlined Wind Speed Forecasting: A Web-Based Machine Learning Approach for Wind Mill Operators with Real-Time Data Using Streamlit")
date = st.date_input(label="Enter a date")
holiday = st.selectbox(label="Select a category of holiday", options=['Holiday', 'Not Holiday', 'WorkDay', 'Additional', 'Event', 'Transfer', 'Bridge'])
locale = st.radio(label="Select a holiday type", options=['National', 'Not Holiday', 'Local', 'Regional'], horizontal=True)
transferred = st.radio(label="Select whether the holiday was transferred or not", options=["True", "False"], horizontal=True)
onpromotion = st.number_input(label="Please enter the total number of expected items to be on promotions")
