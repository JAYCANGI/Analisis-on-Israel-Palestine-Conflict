import streamlit as st
import folium
import numpy as np

def app(df):
        # Analisis Geoespacial
    st.subheader('Analisis Geoespacial')

    def get_color(fatalities):
        if fatalities > 500:
            return 'darkred'
        elif fatalities > 100:
            return 'red'
        elif fatalities > 50:
            return 'orange'
        else:
            return 'green'


    # Geospatial Analysis
    st.subheader('Geospatial Analysis')

    # Create a base map centered around the region
    district_coords = {
        'Gaza': [31.5, 34.466667],
        'Hebron': [31.532569, 35.095388],
        'Jenin': [32.457336, 35.286865],
        'Nablus': [32.221481, 35.254417],
        'Ramallah': [31.902922, 35.206209],
        'Bethlehem': [31.705791, 35.200657],
        'Tulkarm': [32.308628, 35.028537],
        'Jericho': [31.857163, 35.444362],
        'Rafah': [31.296866, 34.245536],
        'Khan Yunis': [31.346201, 34.306286]
    }

    district_fatalities = df.groupby('event_location_district').size()

    # Create a base map centered around the region
    my_map = folium.Map(location=[31.5, 34.75], zoom_start=8, tiles='OpenStreetMap')

    # Add markers and circles for districts
    for district, coords in district_coords.items():
        fatalities = district_fatalities.get(district, 0)
        folium.Marker(
            location=coords,
            tooltip=f'{district}: {fatalities} fatalities',
            icon=None
        ).add_to(my_map)
        folium.Circle(
            location=coords,
            radius=np.sqrt(fatalities) * 100,  # scale radius for better visualization
            color=get_color(fatalities),  # Assuming get_color is defined elsewhere
            fill=True,
            fill_color=get_color(fatalities),
            fill_opacity=0.6,
        ).add_to(my_map)

    # Convert Folium map to HTML
    map_html = my_map._repr_html_()

    # Use Streamlit to display the map
    st.components.v1.html(map_html, width=800, height=400, scrolling=True)