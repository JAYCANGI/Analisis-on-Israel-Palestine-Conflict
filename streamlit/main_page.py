import streamlit as st

import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def app(df):
    st.header('ANALISIS DEL CONFLICTO ENTRE ISRAEL Y PALESTINA')
    st.subheader('PRACTICA FINAL')

    # WordCloud
    st.subheader('Word Cloud')
    cloud_of_words = ' '.join(df['notes'].dropna().astype(str))

    # Generamos el Word Cloud
    facecolor = 'white'
    wordcloud = WordCloud(
        width=1000, height=800,background_color=facecolor,
        min_font_size=10, max_font_size=200
    ).generate(cloud_of_words)

    # Exponemos el Word Cloud
    plt.figure(figsize=(12,6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title('Palabras clave de la base de datos', color='coral', weight='bold', fontsize=10, pad=15)
    st.pyplot(plt)