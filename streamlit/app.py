# streamlit/app.py
import streamlit as st
import requests

# Use the correct endpoint
st.header('PRACTICA FINAL')
response = requests.get("http://fastapi:8000/items")
data = response.json()
print(data)
st.write(data)
