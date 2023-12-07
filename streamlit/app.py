# streamlit/app.py
import streamlit as st
import requests
import pandas as pd
import main_page, demographics, geospatial

PAGES = {
    "Main": main_page,
    "Demographic Analysis": demographics,
    "Geospatial Analysis": geospatial,
    }

def main():
    st.sidebar.title('Navigation')
    response = requests.get("http://fastapi:8000/items")
    data = response.json()
    df = pd.DataFrame(data)

    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page.app(df)

if __name__ == "__main__":
    main()
