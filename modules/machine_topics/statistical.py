from pickletools import stackslice
from streamlit_option_menu import option_menu
import streamlit as st
import requests 
from streamlit_lottie import st_lottie

import webbrowser

def statistical():

    st.success('# Confidence Interval') 
    st.write("""
    - ##### The objective of this project was to monitor the process control of 3 different products, measuring them in terms of productivity, analyzing whether in each portion of processed products the process would be within the normal limits found and to instigate investigation in cases of drop in rhythm or presence of outliers.
    - The project brings real-time information on daily, monthly and hourly productivity.
    """)
    st.write('___')

    coluna1, coluna2 = st.columns([0.5,1])
    coluna1.write("""
    
    #### In this project were used:
    - Concepts on Statistical Quality Control.
    - Removal of outliers so as not to affect the default limits and averages of each group:
        - Boxplot and Z-Score were the strategies used.
    - Query json data via api and SQL database.
    - Plotly and Streamlit to deploy. """ )


    video_file = open('images/cnn/produtividade_ph.mp4', 'rb')
    video_bytes = video_file.read()
    
    coluna2.video(video_bytes)