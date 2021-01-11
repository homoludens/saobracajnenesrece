import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
from datetime import datetime

st.title('Belgrade Traffic Accidents 2018')



#st.write("Here's our first attempt at using data to create a table:")
#st.write(pd.DataFrame({
    #'first column': [1, 2, 3, 4],
    #'second column': [10, 20, 30, 40]
#}))


#01.01.2018,14:00
df = pd.read_csv('./NEZ_OPENDATA_2018_20190125.csv')
#df['date'].to_datetime(df['date'], format='%d.%m.%Y,%H:%M', errors='ignore')

df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y,%H:%M').dt.date

#df['date'] = datetime.strptime(df['date'], '%d.%m.%Y,%H:%M')
df


st.sidebar.subheader("Inputs")


# Calculate the timerange for the slider
min_ts = min(df['date'])
max_ts = max(df['date'])

st.sidebar.subheader("Inputs")
min_selection, max_selection = st.sidebar.slider(
    "Timeline", min_value=min_ts, max_value=max_ts, value=[min_ts, max_ts]
)


df = df[
    (df["date"] >= min_selection) & (df["date"] <= max_selection)
]
st.write(f"Data Points: {len(df)}")



st.map(df)


#date = st.select_slider(
    #'Select a color of the rainbow',
     #options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
#st.write('My favorite color is', date)



#start_time = st.slider(
    #"When do you start?",
    #value=datetime(2020, 1, 1, 9, 30),
    #format="MM/DD/YY - hh:mm")

#st.write("Start time:", start_time)


#d3 = st.date_input("range, no dates", [])
#st.write(d3)
