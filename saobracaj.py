import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
from datetime import datetime
import altair as alt
import pydeck as pdk

#https://github.com/streamlit/demo-uber-nyc-pickups/blob/master/streamlit_app.py


def map(data, lat, lon, zoom):
    st.write(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={
            "latitude": lat,
            "longitude": lon,
            "zoom": zoom,
            "pitch": 50,
        },
        layers=[
            pdk.Layer(
                #"HeatmapLayer",
                "HexagonLayer",
                data=data,
                get_position=["lon", "lat"],
                radius=100,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
        ]
    ))
          


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

# LOADING DATA
#DATE_TIME = "date/time"
#DATA_URL = (
    #"http://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"
#)

#@st.cache(persist=True)
#def load_data(nrows):
    #data = pd.read_csv(DATA_URL, nrows=nrows)
    #lowercase = lambda x: str(x).lower()
    #data.rename(lowercase, axis="columns", inplace=True)
    #data[DATE_TIME] = pd.to_datetime(data[DATE_TIME])
    #return data

#data = load_data(100000)

#data

# CREATING FUNCTION FOR MAPS 


  
df2 = df[["lat","lon"]]

df2
st.write(f"Data Points: {len(df2)}")

midpoint = (np.average(df2["lat"]), np.average(df2["lon"]))
map(df2, midpoint[0], midpoint[1], 11)
