import streamlit as st
from streamlit_option_menu import option_menu
from streamlit.components.v1 import custom_component as _components
import pandas as pd
from eda import display_eda
from plots import display_plots
from predict import make_predictions

def main():
    st.markdown("# Diabetes Detection")
    
    data = pd.read_csv("diabetes.csv")
    
    # Sidebar navigation
    selected = option_menu( 
                menu_title=None, 
                options = ["EDA", "Plots", "Predictions"],
                icons= ["activity","bar-chart","brilliance"] ,menu_icon="cast",
                        default_index=0,
                        orientation="horizontal" )
    
    
    # Display selected section
    if selected == "EDA":
        display_eda(data)
    elif selected == "Plots":
        display_plots(data)
    elif selected == "Predictions":
        make_predictions(data)


if __name__ == "__main__":
    main()
