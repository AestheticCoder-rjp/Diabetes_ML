import streamlit as st
from PIL import Image

def display_eda(data):
    st.markdown("### Exploratory Data Analysis (EDA)")
    img = Image.open("d.webp")
    st.image(img)
    
    st.subheader("Sample Data")
    st.dataframe(data.head(5))
    
    st.subheader("Data Summary")
    st.write(data.describe())
    
    st.write("Shape of Data:", data.shape)
    st.write("Size of Data:", data.size)
    st.write("Checking Null Values:", data.isnull().sum())
