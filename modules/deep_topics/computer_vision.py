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
    coluna1.write('##### The objective of this project was to meansuring the produtivicty of the people in a process.')

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

    col11, col22 = st.columns(2)
    video_file = open('images/cnn/hand_detector.mp4', 'rb')
    video_bytes = video_file.read()


    col11.video(video_bytes)
    col22.write(' ')
    col22.write(' ')
    col22.write('___')
    col22.write("""
        - #####  The first step of the propject was detect and mensring the hand positions in space.
        """)
    col22.write('___')




    st.error(""" 
    - ####  Body Tracking: """)

    

    col111, col222 = st.columns(2)
    video_file2 = open('images/cnn/yo_detection.mp4', 'rb')
    video_bytes2 = video_file2.read()


    col111.video(video_bytes2)
    col222.write(' ')
    col222.write(' ')
    col222.write('___')
    col222.write("""
        - ##### Initial teste, localizando como pontos princiapis os cotovelos e avaliando a capacidade de detectar as posições e emitir alertas quando os pontos destacados ultrapassam uma determinada linha.
        """)
    col222.write('___')


    st.error(""" 
    - ####  Real Time Monitoring - Initial Tests: """)

    col1, col2, col3, col4 = st.columns([1,1,1,0.5])

    from PIL import Image

    video_file2 = open('images/cnn/pode_detector.mp4', 'rb')
    video_bytes2 = video_file2.read()
    
    col3.write(' ')
    col3.write('___')
    col3.write(""" - ##### The process that needed to mensurate the productivity. """)
    col3.write('___')
