from pickletools import stackslice
from streamlit_option_menu import option_menu
import streamlit as st
import requests 
from streamlit_lottie import st_lottie

import webbrowser

def fruit_fly():


    st.success('### Object Detection - Fruit Fly (Pest)') 
    coluna1, coluna2, coluna3 = st.columns([1,0.1,0.5])

    coluna1.write(' ')
    coluna1.write('##### The objective of this project was to count the number of insects (Pests) present in the traps inside the field, automating the count that was done manually. The model was trained to identify Fruit Flies, one of the main pests in mango plantations.')

    st.write('___')

    coluna3.write("""
    
    ##### In this project were used: 
    -  Computer Vision;
    -  Convolutional Neural Network.
        
        """ )




    st.success('### Metrics:')
    
    col1, col2,col3 = st.columns([1,0.1,0.4])

    from PIL import Image
    img = Image.open('images/cnn/metrics_fly_r.png')
    newsize = (1300,700)
    img2 = img.resize(newsize)

        ########## JANELA LATERAL ##########

    col1.image(img, use_column_width=True)
    col3.write('___')
    col3.write(""" 
    - ##### Unlike the Mango's Model, the dataset of this model (Images) was not of a good quality, which impacted the model metrics. However, in terms of performance and problem solving, the model proved to be quite effective.
        """)
    col3.write('___')



    
    # img_loss = Image.open('fly_loss.png')
    # newsize2 = (1300,700)
    # img2_loss = img_loss.resize(newsize2)

    #     ########## JANELA LATERAL ##########

    # col2.image(img_loss, use_column_width=True)


    st.write('___')
    st.write(' # How it works:')
    st.write('___')

    coll11, coll22, coll33, coll44,coll55 = st.columns([0.5,1,1,1,0.5])


    from PIL import Image
    img1 = Image.open('images/cnn/im_1out.jpeg')
    
    img3 = Image.open('images/cnn/im_1inpu.jpeg')

    newsize = (300,400)
    img1_n = img1.resize(newsize)
    
    img3_n = img3.resize(newsize)

        ########## JANELA LATERAL ##########
    coll22.error(""" - ### Input """)
    coll22.image(img3_n, use_column_width=True)

    with coll33:
        st.info(""" - ### CNN  """)
        def get_lottie(url):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

        lottie_icon = get_lottie('https://assets6.lottiefiles.com/packages/lf20_knvn3kk2.json')
        st_lottie(lottie_icon, height = 300, key = 'lttie')
    
    coll44.error(""" - ### Output """)
    coll44.image(img1_n, use_column_width=True)
