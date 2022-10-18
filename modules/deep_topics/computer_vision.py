from pickletools import stackslice
from streamlit_option_menu import option_menu
import streamlit as st
import requests 
from streamlit_lottie import st_lottie

import webbrowser

def computer_vision():

    st.success('### Hand and Body Tracking') 
    coluna1, coluna2, coluna3 = st.columns([1,0.1,0.5])

    coluna1.write(' ')
    coluna1.write('##### The objective of this project was to measure the productivity of employees at a given stage of the process.')

    st.write('___')

    coluna3.write("""

    ##### In this project were used:
    -  Computer vision libraries.
    """ )


    # img_loss = Image.open('loss.png')
    # newsize2 = (1300,700)
    # img2_loss = img_loss.resize(newsize2)

    #     ########## JANELA LATERAL ##########

    # col2.image(img_loss, use_column_width=True)



    st.write('# How it works:')



    st.error(""" 
    - ####  Hand Tracking: """)

    col11, col22 = st.columns([0.5,1])
    video_file = open('images/cnn/hand_final.mp4', 'rb')
    
    video_bytes = video_file.read()


    col11.video(video_bytes)
    col22.write(' ')
    col22.write(' ')
    col22.write('___')
    col22.write("""
        - #####  The first step of this project was to detect and track the positions of the hands, identifying and collecting the data of the positions in space (X,Y).
        """)
    col22.write('___')




    st.error(""" 
    - ####  Body Tracking: """)

    

    col111, col222 = st.columns([0.5, 1])
    video_file2 = open('images/cnn/yo_detect_final.mp4', 'rb')
    video_bytes2 = video_file2.read()


    col111.video(video_bytes2)
    col222.write(' ')
    col222.write(' ')
    col222.write('___')
    col222.write("""
        - ##### Initial test with body tracking, locating the main points (elbows) and issuing alerts when the highlighted points exceed a certain line.
        """)
    col222.write('___')


    st.error(""" 
    - ####  Real Time Monitoring: """)

    col2, col3, col4 = st.columns([0.5,1,0.5])

    from PIL import Image

    video_file2 = open('images/cnn/pode_detector.mp4', 'rb')
    video_bytes2 = video_file2.read()
    
    col2.video(video_bytes2)
    col3.write('___')
    col3.write(""" - ##### Initial test of the program on the production line. """)
    col3.write('___')
