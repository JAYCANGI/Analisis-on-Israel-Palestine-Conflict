
import streamlit as st
import requests
import pandas as pd
import main_page, demografico, geografico,formulario

PAGES = {
    "Inicio 🏠 ": main_page,
    "Análisis Demográfico 🫂": demografico,
    "Análisis Geográfico 🌍": geografico,
    "Formulario 🧾": formulario,
    }

def main():
    st.sidebar.title('Navegación')
    response = requests.get("http://fastapi:8000/items")
    data = response.json()
    df = pd.DataFrame(data)

    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page.app(df)

if __name__ == "__main__":
    main()
