import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

# Establecer la configuración de la página al inicio de tu script principal
st.set_page_config(page_title="Análisis del Conflicto")

def app(df):

    # CSS para personalizar el banner
    banner_css = """
    <style>
    .banner {
    background-color: #3F3F4C;
    padding: 10px;
    border-radius: 10px;
    }
    .banner h1 {
    color: white;
    text-align: center;
    }
    
    </style>
    """
    st.markdown(banner_css, unsafe_allow_html=True)

    banner_html = """
    <div class="banner">
    <h1>🇮🇱 Análisis del conflicto entre Israel y Palestina 🇵🇸</h1>
    </div>
    """
    st.markdown(banner_html, unsafe_allow_html=True)

    
    st.markdown("&nbsp;", unsafe_allow_html=True)

    # Centrar el encabezado y el markdown
    st.markdown("""
    <div style="text-align: center">
        <h2>PRACTICA FINAL ~ Jay Shankar Cangi</h2>
    </div>
    """, unsafe_allow_html=True)

   
    st.markdown("&nbsp;", unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center">
    En esta practica final de la asignatura de Programación II he realizado el analisis de los datos recogidos por WILLIAN OLIVEIRA GIBIN, de funetes de televisión y redes sociales. El objetivo de este analisis es exponer la verdad sobre los sucesos ocurridos en el estado de Palestina.
    </div>
    """, unsafe_allow_html=True)

    
    st.markdown("&nbsp;", unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center">
        <a href="https://www.kaggle.com/datasets/willianoliveiragibin/fatalities-in-the-israeli-palestinian">IR A KAGGLE</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("&nbsp;", unsafe_allow_html=True)

    tab1,tab2 = st.tabs(['Video explicativo sobre el conflicto','Word Cloud sobre el Database'])

    with tab1:
        # Mostrar el video de YouTube
        st.video('https://www.youtube.com/watch?v=qSAiXOJdFNA')  

    with tab2:
        # WordCloud
        cloud_of_words = ' '.join(df['notes'].dropna().astype(str))
        wordcloud = WordCloud(width=800, height=400, background_color='#464E5F').generate(cloud_of_words)

        # Mostrar el word cloud
        st.subheader("Word Cloud")
        st.markdown('Este Word Cloud indica las palabras recogidas en las notas del autor de esta base de datos. Resaltando las más comunes mediante el tamaño de la palabra.')
        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)