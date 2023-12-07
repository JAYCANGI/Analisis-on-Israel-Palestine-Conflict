import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def app(df):
    st.subheader('Analisis Demográfico')

    # Distribución de Edad
    st.subheader("Distribución de Edad")
    plt.figure(figsize=(10,6))
    sns.histplot(data=df, x='age', bins=30, kde=True)
    st.pyplot(plt)

    # Distribución de Genero
    st.subheader("Distribución de Genero")
    gender_counts = df['gender'].value_counts()
    plt.figure(figsize=(10,6))
    sns.barplot(x=gender_counts.index, y=gender_counts.values, palette="rocket")
    st.pyplot(plt)

    # Distribución de Nacionalidad
    st.subheader("Distribución de Nacionalidad")
    citizenship_counts = df['citizenship'].value_counts()
    plt.figure(figsize=(10,6))
    sns.barplot(x=citizenship_counts.index, y=citizenship_counts.values, palette="viridis")
    st.pyplot(plt)