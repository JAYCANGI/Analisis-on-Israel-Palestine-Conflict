import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

# Establecer la configuración de la página al inicio de tu script principal
st.set_page_config(page_title="Análisis del Conflicto",page_icon="🚀",layout='wide')

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
    <h1>Análisis del conflicto entre Israel y Palestina</h1>
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
    <style>
    div, h2, h3, strong {
        text-align: center; 
    }
    </style>

    <div>
        <p>Este proyecto es una aplicación web desarrollada con el objetivo de analizar y visualizar las incidencias ocurridas en el conflicto entre Israel y Palestina desde el 2004 hasta 2023.</p>
        <h2><strong>Objetivo</strong></h2>
        <p>El prop&oacute;sito principal de esta práctica final es proporcionar un entendimiento profundo de las repercusiones del conflicto, analizando los datos desde perspectivas demográficas y geográficas.</p>
        <h2><strong>Secciones</strong></h2>
        <h3>Análisis Demográfico</h3>
        <p>En esta sección, la aplicación examina varios aspectos demográficos relacionados con las incidencias: - Distribución de edad entre los afectados. - Comparativa porcentual entre hombres y mujeres afectados. - Clasificación por nacionalidades de los afectados. Esta parte del análisis permite comprender mejor qui&eacute;nes han sido los más impactados por el conflicto y de qu&eacute; manera.</p>
        <h3>Análisis Geográfico</h3>
        <p>La segunda parte se enfoca en el análisis geográfico: - Representación en un mapa interactivo de los conflictos por distrito. - Visualización evolutiva por región a lo largo de los. Esta visualización interactiva facilita la comprensión de la distribución y evolución geográfica del conflicto.</p>
        <h2><strong>Tecnolog&iacute;as Utilizadas</strong></h2>
        <p><strong>SQLalchemy:</strong> Utilizado para la gestión y consulta de la base de datos.</p>
        <p><strong>FastAPI:</strong> Empleado para crear una API robusta y eficiente.</p>
        <p><strong>Streamlit:</strong> Usado para desarrollar la interfaz de usuario interactiva.</p>
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