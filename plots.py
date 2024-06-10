import streamlit as st
import plotly.express as px

def display_plots(data):
    st.title("Plots")
    
    st.header("Distribution of Age")
    fig = px.histogram(data, x=data.Age, marginal="rug")
    st.plotly_chart(fig)
    
    st.header("Distribution of Blood Pressure")
    fig = px.histogram(data, x=data.BloodPressure, marginal="rug")
    st.plotly_chart(fig)
    st.header("Box Plot of Glucose Levels by Diabetes Outcome")
    fig = px.box(data, x='Outcome', y='Glucose', color='Outcome', points='all')
    st.plotly_chart(fig)
    
    st.header("Scatter Plot of BMI vs. Age")
    fig = px.scatter(data, x='Age', y='BMI', color='Outcome')
    st.plotly_chart(fig)
    
    st.header("Correlation Heatmap")
    corr_matrix = data.corr()
    fig = px.imshow(corr_matrix, color_continuous_scale='RdBu_r')
    st.plotly_chart(fig)
    # Add more plot functions as needed
