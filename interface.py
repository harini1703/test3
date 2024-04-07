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
Vapour_Pressure=st.number_input("Vapour Pressure", min_value=0, max_value=100, value=0)
b=st.selectbox("SELECT THE Wind Direction:",('Calm','NNW','NE','NW','WNW','NNE','ENE','N','Variable','E','SE','W','SW','S','ESE','SSE','WSW'))
if b=='Calm':
  b=0
elif b=='NNW':
  b=34
elif b=='NE':
  a=5
elif b=='NW':
  b=32
elif b=='WNW':
  b=29
elif b=='NNE':
  b=2
elif b=='ENE':
  b=7 
elif b=='N':
  b=36
elif b=='Variable':
  b=99
elif b=='E':
  b=9
elif b=='SE':
  b=14
elif b=='W':
  b=27
elif b=='SW':
  b=23
elif b=='S':
  b=18
elif b=='ESE':
  b=11
elif b=='SSE':
  b=16
else:
  a=25
C=st.selectbox("SELECT THE Visiblity:",('10,000 Meters','4000 Meters','2000 Meters','500 Meters','1000 Meters','20,000 Meters',"50 Meters","50,000 Meters"))
if c=='10,000 Meters':
  c=97
elif c=='4000 Meters':
  c=96
elif c=='2000 Meters':
  c=95  
elif c=='500 Meters':
  c=93
elif c=='1000 Meters':
  c=94
elif c=='20,000 Meters':
  c=98
elif c=='50 Meters':
  c=90
else:
  c=99 

