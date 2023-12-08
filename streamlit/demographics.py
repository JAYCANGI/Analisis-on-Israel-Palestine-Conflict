import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd
import numpy as np

def app(df):
    
    # Set a subheader
    st.title('Analisis Demográfico')

    # Create a select box for the tabs
    tab = st.selectbox('Seleccione una Distribución', ['Distribución de Edad', 'Distribución de Género', 'Distribución de Nacionalidad'])

    if tab == 'Distribución de Edad':
        # Distribución de Edad
        st.subheader("Distribución de Edad")
        bins = np.arange(df['age'].min(), df['age'].max() + 5, 5)
        hist, edges = np.histogram(df['age'], bins=bins)
        age_counts = pd.DataFrame({'age': edges[:-1], 'count': hist})
        max_age = age_counts['age'].max()
        age_counts['color_scale'] = age_counts['age'] / max_age
        fig = px.bar(age_counts, x='age', y='count', color='color_scale', color_continuous_scale=["#aec6cf", "#ff6961"])
        fig.layout.coloraxis.showscale = False

        st.plotly_chart(fig)

        st.write("""
        Este gráfico representa la distribución de edades en intervalos de 5 años. 
        El color de cada barra indica la edad, con un gradiente de azul pastel a rojo pastel.
        """)

      

            
    
    
    elif tab == 'Distribución de Género':
            
            # Distribución de Género
            st.subheader("Distribución de Género")

            gender_counts = df['gender'].value_counts().reset_index()

            gender_counts.columns = ['gender', 'count']
            
            color_discrete_map = {'M': '#c5d0f6', 'F': '#f6c6f4'}

            fig = px.bar(gender_counts, x='gender', y='count', color='gender', color_discrete_map=color_discrete_map) 
            
            st.plotly_chart(fig)

            st.write("""
            Este gráfico representa la distribución de género. 
            Las barras azules representan al género masculino, mientras que las barras rosadas representan al género femenino.
            """)
            # Calculate the percentages for each citizenship
            gender_counts['percentage'] = (gender_counts['count'] / gender_counts['count'].sum()) * 100

            # Create a DataFrame with the percentages for each nationality
            results = gender_counts[['gender', 'percentage']]

            # Display the results as an st.info and separate them by columns
            cols = st.columns(len(results))
            for i in range(len(results)):
                with cols[i]:
                    cols[i].subheader(f"Porcentaje {results.iloc[i, 0]}")
                    st.info(f"{results.iloc[i, 1]:.2f}%.")
                
    
    
    elif tab == 'Distribución de Nacionalidad':
        # Distribución de Nacionalidad
        st.subheader("Distribución de Nacionalidad")
        citizenship_counts = df['citizenship'].value_counts().reset_index()
        citizenship_counts.columns = ['citizenship', 'count']

        # Define the color for each citizenship
        color_discrete_map = {'Palestinian': '#e6685b', 'Israel': '#74a5ea', 'America': '#feffff', 'Jordan': '#90ee9f'} 

        fig = px.bar(citizenship_counts, x='citizenship', y='count', color='citizenship', color_discrete_map=color_discrete_map) 
        st.plotly_chart(fig)

        st.write("""
        Este gráfico representa la distribución de nacionalidades. 
        Cada nacionalidad se representa con un color único.
        """)

        # Calculate the percentages for each citizenship
        citizenship_counts['percentage'] = (citizenship_counts['count'] / citizenship_counts['count'].sum()) * 100

        # Create a DataFrame with the percentages for each nationality
        results = citizenship_counts[['citizenship', 'percentage']]

        # Display the results as an st.info and separate them by columns
        cols = st.columns(len(results))
        for i in range(len(results)):
            with cols[i]:
                cols[i].subheader(f"Porcentaje {results.iloc[i, 0]}")
                st.info(f"{results.iloc[i, 1]:.2f}%.")