# streamlit/app.py
import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import folium
import numpy as np

# Use the correct endpoint
st.header('PRACTICA FINAL')
response = requests.get("http://fastapi:8000/items")
data = response.json()

# Convert to pandas DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
st.write(df)

# Demographic Analysis
st.subheader('Demographic Analysis')

# Age distribution
st.subheader("Age Distribution")
plt.figure(figsize=(10,6))
sns.histplot(data=df, x='age', bins=30, kde=True)
st.pyplot(plt)

# Gender distribution
st.subheader("Gender Distribution")
gender_counts = df['gender'].value_counts()
plt.figure(figsize=(10,6))
sns.barplot(x=gender_counts.index, y=gender_counts.values, palette="rocket")
st.pyplot(plt)

# Citizenship distribution
st.subheader("Citizenship Distribution")
citizenship_counts = df['citizenship'].value_counts()
plt.figure(figsize=(10,6))
sns.barplot(x=citizenship_counts.index, y=citizenship_counts.values, palette="viridis")
st.pyplot(plt)














# Geospatial Analysis
st.subheader('Geospatial Analysis')

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






















# WordCloud
st.subheader('Word Cloud')
cloud_of_words = ' '.join(df['notes'].dropna().astype(str))

# Generate a Word Cloud
facecolor = 'white'
wordcloud = WordCloud(
    width=1000, height=800,background_color=facecolor,
    min_font_size=10, max_font_size=200
    ).generate(cloud_of_words)

# Display the World Cloud image
plt.figure(figsize=(12,6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title('Most Frequently Occuring Words in the Notes Feature of the Dataset', color='coral', weight='bold', fontsize=10, pad=15)
st.pyplot(plt)