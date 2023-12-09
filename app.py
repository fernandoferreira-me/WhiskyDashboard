import pandas as pd

import folium
from folium.plugins import HeatMap

import streamlit as st
from streamlit_folium import folium_static, st_folium

st.write("""
Cacao Map
""")

data = pd.read_csv('data/cacao.csv')
map = folium.Map(location=[0, 0], zoom_start=3, tiles='cartodbdark_matter')
lat, lng = data['maker_location_latitude'], data['maker_location_longitude']
heatmap = HeatMap(list(zip(lat, lng)))
heatmap.add_to(map)
st_folium(map, width=1200, height=600)