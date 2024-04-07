import pickle
import streamlit as st

# Load the model
pickle_in = open('forecast.pkl', 'rb')
clf = pickle.load(pickle_in)

st.header("Streamlined Wind Speed Forecasting: A Web-Based Machine Learning Approach for Wind Mill Operators with Real-Time Data Using Streamlit")
a=st.selectbox("SELECT THE HOUR:",('8:30','17:30','5:30','11:30','14:30','20:30'))
