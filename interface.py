import pickle
import streamlit as st

# Load the model
pickle_in = open('forecast.pkl', 'rb')
clf = pickle.load(pickle_in)

st.header("Streamlined Wind Speed Forecasting: A Web-Based Machine Learning Approach for Wind Mill Operators with Real-Time Data Using Streamlit")
a=st.selectbox("SELECT THE HOUR:",('8:30','17:30','5:30','11:30','14:30','20:30'))
if a=='8:30':
  a=12
elif a=='17:30':
  a=48
elif a=='5:30':
  a=0  
elif a=='11:30':
  a=24
elif a=='14:30':
  a=36
else:
  a=60  
Dry_Bulb_Temperature = st.number_input("Dry Bulb Temperature", min_value=0, max_value=100, value=0)
Wet_Bulb_Temperature = st.number_input("Wet Bulb Temperature", min_value=0, max_value=100, value=0)
Dew_point_Temperature = st.number_input("Dew point Temperature", min_value=0, max_value=100, value=0)
Relative_Humidity=st.number_input("Relative Humidity", min_value=0, max_value=100, value=0)
Vapour Pressure=st.number_input("Vapour Pressure", min_value=0, max_value=100, value=0)

