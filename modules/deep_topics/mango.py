from pickletools import stackslice
from streamlit_option_menu import option_menu
import streamlit as st
import requests 
from streamlit_lottie import st_lottie

import webbrowser

def mango_count():

    st.success('### Tracker and Classification - Mango Count') 
    coluna1, coluna2, coluna3 = st.columns([1,0.1,0.5])

    coluna1.write(' ')
    coluna1.write('##### The objective of this project was to count the mangos discarded in two belts of the process, until then the company only counted the mangoes within the quality standards. To account for real-time processing, it was necessary to estimate the weight of each fruit identified in the image and join it with the data from the database. Was created a control panel (Streamlit) and a telegram bot to send messages about the percentages processed !')
    st.write(""" 
            - The model was trained to identify two classes, mango and cut mangoes to indicate the completion of processing ! 
    """)
    st.write('___')

    coluna3.write("""

    ##### In this project were used:
    -  Computer vision;
    -  Convolutional Neural Network;
    -  Tracker;
    -  Telegram Bot;
    -  Data query via api and DBeaver database;
    -  Plotly and Streamlit to deploy. """ )

    st.error ('### Perfomance:')
    st.write ('___')
    col21, col22, col23 = st.columns([1,0.1,0.65])
    #col21.error ('### Desempenho:')

    from PIL import Image
    img_cpu = Image.open('images/yolo_mango_graphs/cpu_usage.png')
    img_gpu = Image.open('images/yolo_mango_graphs/gpu_usage_models.png')
    img_MAP = Image.open('images/yolo_mango_graphs/map_metric.png')
    img_resume = Image.open('images/yolo_mango_graphs/resume_metrics.png')


        ########## JANELA LATERAL ##########

    col21.image(img_cpu, use_column_width=True)
    col21.image(img_gpu, use_column_width=True)
    col23.write(" ")
    col23.write(" ")
    col23.write(" ")
    col23.write(" ")
    
    col23.write(""" 
    - ######  A first model was developed, which in practice presented excellent results, but became too heavy for the machine to process. To solve this, another model was created, with similar performance but which used fewer computational components to work. The comparison between the models can be seen in the following images. It is noticed that a model uses more CPU and GPU, this model converged to the fastest result, but it was not viable in terms of production. """)
    col23.write("___")

    col23.write("""
    - ###### It is also worth mentioning that the data collection process involved collecting videos, cutting the frames and labeling/labeling the images for further training.
    """)

    col23.write(" ")
    col23.write("___")
    col23.error(""" 
    - ### Metrics
    """)
    col23.write("___")

    col21.image(img_MAP, use_column_width=True)

    col23.write(" ")
    col23.write(" ")
    col23.write(" ")
    col23.write(" ")
    col23.write(""" 
    - ###### As I said, the models have similar metrics, but one converged faster in training and the other performed better in practice.  """)

    col23.image(img_resume, use_column_width=True)







    # img_loss = Image.open('loss.png')
    # newsize2 = (1300,700)
    # img2_loss = img_loss.resize(newsize2)

    #     ########## JANELA LATERAL ##########

    # col2.image(img_loss, use_column_width=True)



    st.write('# How it works:')



    st.error(""" 
    - ####  Front-End: """)

    col11, col22 = st.columns(2)
    video_file = open('images/cnn/video_mango_count1.mp4', 'rb')
    video_bytes = video_file.read()


    col11.video(video_bytes)
    col22.write(' ')
    col22.write(' ')
    col22.write('___')
    col22.write("""
        - ##### For the visualization of the information, this dashboard was developed to take the information in real time. To bring the video on the front, OBS Studio was used to capture the back-end of the models plus youtube to make the streaming to be captured by the front code without affect the real-time capability of models.
        """)
    col22.write('___')




    st.error(""" 
    - ####  Back-End: """)

    

    col111, col222 = st.columns(2)
    video_file2 = open('images/cnn/back_end_count.mp4', 'rb')
    video_bytes2 = video_file2.read()


    col111.video(video_bytes2)
    col222.write(' ')
    col222.write(' ')
    col222.write('___')
    col222.write("""
        - ##### There are two tracker models and two classifier models running at the same time, strategies were needed to unite the counts and also store and update the variables in the database without affecting the Real Time of the models.
        """)
    col222.write('___')


    st.error(""" 
    - ####  Bot: """)

    col1, col2, col3, col4 = st.columns([1,1,1,0.5])

    from PIL import Image

    img = Image.open('images/regression_model/telegram_bot.png')
    newsize = (800,650)
    img2 = img.resize(newsize)

        ########## JANELA LATERAL ##########
    col2.write(' ')
    col2.image(img, use_column_width=True)
    col3.write(' ')
    col3.write('___')
    col3.write(""" - ##### A method was also developed to estimate the weights of the counted fruits and send this information along with the processed percentage to the decision makers through a telegram bot. """)
    col3.write('___')
