import streamlit as st
import requests
import json
import pandas as pd
import pydeck as pdk
import time

@st.cache
def load_data1():
    astro = requests.get("http://api.open-notify.org/astros.json")
    astro_json = json.loads(astro.text)
    return astro_json

df_astro = load_data1()

@st.cache
def load_data2():
    iss = requests.get("http://api.open-notify.org/iss-now.json")
    iss_json = json.loads(iss.text)
    return iss_json

df_iss = load_data2()



st.title("Current People in Space")
st.markdown("This app displays current people in space. In the following the number of astronauts, their names and if possible their location will be available.")

list_names= []
for value in range(0,df_astro['number']):
    list_names.append(df_astro['people'][value]['name'])
st.write("Number of people currently in space: ", df_astro['number'], " |  Names of people currently in space: ", list_names)


st.markdown("### Current position of the ISS:")
st.write("Longitude: ", df_iss['iss_position']['longitude']," |   Latitude: ", df_iss['iss_position']['latitude'], " | Latest update: ", time.ctime(int(df_iss['timestamp']))) 


### plot for ISS
def load_pandas():
    df = pd.read_json("http://api.open-notify.org/iss-now.json")
    return df
iss_pd = load_pandas()

st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=pdk.ViewState(
         latitude=iss_pd['iss_position'][0],
         longitude=iss_pd['iss_position'][1],
         zoom=11,
         pitch=50,
        ),
     layers=
            pdk.Layer(
                'ScatterplotLayer',
                data=iss_pd,
                get_position=[iss_pd['iss_position'][1], iss_pd['iss_position'][0]],
                get_color='[200, 30, 0, 160]',
                get_radius=200,
                filled=True,
                opacity=0.8,
                pickable=True
            
        ),
 )) 

st.markdown("Description of Map: Shown is the the current position of the ISS. Since the position changes rather quickly the timestamp shows when the information was retrieved.")


