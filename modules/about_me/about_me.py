#st.subheader('Hello, i am Bernard Collin :wave: ')
from pickletools import stackslice
from streamlit_option_menu import option_menu
import streamlit as st
import requests 
from streamlit_lottie import st_lottie
from bokeh.models.widgets import Div

import webbrowser

def about_me():
    coluna1, coluna2= st.columns([1,1])


    coluna1.success('## Hello, i am Bernard Collin :wave: ')





    st.title('A Data Scientist and Production Engineer :snake:')

    st.write("Merging Engineering knowledge and process vision with Data Science techniques through the Python programming language, using statistical analysis, machine and deep learning to solve problems and optimize processes.")
    st.write("[>Degree-Diploma<](https://acadigitus.univasf.edu.br/diploma/3984-3984-9d6689938fa3%20)")
    colz, colw = st.columns([1,0.4])
    colw.error("Please use a desktop or laptop computer to get a better experience.")

    st.write('___')

    col1,col2 = st.columns(2)

    with col1:
        #st.success('### Section A')
        st.success('## Professional Background:')
        st.write('___')

        st.write(' - First, during Production Engineering college I worked as a volunteer for a junior company at the university, where I provided Production Engineering consulting services to other companies in the university region, during this period I worked as a Project Advisor and Quality Advisor.')

        st.write(' - ###### After that period, I started my internship as a Production Engineering, where I worked on the standardization and mapping of the internal processes of a grape producing farm in the region of São Francisco Valley.')

        
        st.write('-  Then, I started to study Python and Machine Learning while still in college to combine the vision of Data Science with Production Engineering, with that I was able to do my final course project using practical knowledge in both areas (this project can be consulted in the Published Works section).')
        
        st.write(' - ###### Close to finishing my undergraduate course I got a job as a Data Scientist in the largest producer and exporter of mangoes in Brazil, where I could develop myself and develop a series of Data Analysis, Automation and Artificial Intelligence projects.')
        
        st.write(' - Today I work at one of the largest business consulting firms in Latin America, providing services to large companies and multinationals. I work as a consultant in Data Analysis and Artificial Intelligence, working daily on projects using agile methodology (Scrum) and Kanban together with the teams involved.')
        
        st.write('___')

    colu1, colu2 = st.columns([1,0.1])
    col11,col22,col33, col44 = st.columns(4)

    #colu1.success('### Section B')
    colu1.success('## Skills and Experience:')


    col11.write("""
        - #### Production Engineering:
            - Supply Chain Management;
            - Bussiness;
            - Marketing;
            - Project Management;
            - Statistics;
            - Process Control. """ )
    col22.write( """
        - #### Python:
            - Data Analysis and Pre-Processing;
                - Pandas, Numpy, Z-score, Scipy, StandardScaler, MinMaxScaler, RobustScaler, OneHotEncoder...
            - Data Visualization;
                - Plotly, Seaborn, Matplotlib;
            - Deploy;
                - Streamlit and Dash.
            - Computer Vision:
                -  OpenCV
            - Jobs;
            - Automation;
            - Socket;
            - Exception Handling.""")

    col33.write( """   
        - #### Machine Learning and Deep Learning:
            - Scikit-Learn, XGBoost;
            - Unsurpervised and Supervised Learning;
            - PyTorch;
            - Convolutional Neural Networks;
            - Artificial Neural Networks;
            - Trackers;
            - NLP: NLTK | Sequence Labeling;
            - Computer Vision for Deep Learning. """)
    col44.write( """
        - #### Others Skills;
            - Power BI;
            - OBS Studio;
            - Wondershare Filmora;
            - DBeaver - Database;
            - SQL;
            - Edge-Impulse;
            - Ultralytics;
            - Roboflow.
                """)

    with col2:
        
        def get_lottie(url):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()
        st.write(' ')
        lottie_icon = get_lottie('https://assets9.lottiefiles.com/packages/lf20_yswivetl.json')
        st_lottie(lottie_icon, height = 450, key = 'lttie')
        
    with st.container():

        st.write("---")
        st.success("### Get in touch with me:")
        st.write("##")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/bernard.collin@hotmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)

        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            from PIL import Image
            img = Image.open('soc_img.png')
            newsize = (1300,700)
            img2 = img.resize(newsize)

                ########## JANELA LATERAL ##########

            st.image(img, use_column_width=True)
            st.empty()

    coluna1, coluna2, coluna3 = st.columns([0.3,1,0.3])
    with coluna2:
            
        selected = option_menu(
            menu_title = ' ',
            options = ['Linkedin','Whatsapp','CV-Europass','Git','Gmail'],
            icons = ['linkedin','whatsapp', 'journal-album','github','envelope'],
            menu_icon = ' ',
            default_index = 4,
            orientation = 'horizontal',
            styles={
                    "container": {"padding": "0!important", "background-color": "##00172B"},
                    "icon": {"color": "#39B6B0", "font-size": "28px"}, 
                    "nav-link": {"font-size": "12px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                    "nav-link-selected": {"background-color": "#00172B","font-size": "14px"},
                }
        )

        if selected == 'CV-Europass':
            js = "window.open('https://europa.eu/europass/eportfolio/api/eprofile/shared-profile/4bc33f1f-1cee-4d68-877e-084948f30439?view=html')"  # New tab or window
            #js = "window.location.href = 'https://www.streamlit.io/'"  # Current tab
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)



        if selected == 'Linkedin':
            js = "window.open('https://www.linkedin.com/in/bernard-collin-b4a9b611b/')"  # New tab or window
            #js = "window.location.href = 'https://www.streamlit.io/'"  # Current tab
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)


        if selected == 'Whatsapp':
            js = "window.open('https://wa.me/5575982381806')"  # New tab or window
            #js = "window.location.href = 'https://www.streamlit.io/'"  # Current tab
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
            
        if selected == 'Git':
     
            js = "window.open('https://github.com/RBCollin')"  # New tab or window
            #js = "window.location.href = 'https://www.streamlit.io/'"  # Current tab
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
     
    

        if selected == 'Gmail':
            st.write('bernardcollin92@gmail.com')
            
            
        
    


