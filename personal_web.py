from pickletools import stackslice
from streamlit_option_menu import option_menu
import streamlit as st
import requests 
from streamlit_lottie import st_lottie

import webbrowser



st.set_page_config(layout="wide", page_title="Bernard's Webpage", page_icon=":bar_chart:"
)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
        


local_css("style/style.css")





with st.sidebar:
    st.markdown('''
    <a href="javascript:document.getElementsByClassName('css-y4qlto e1fqkh3o1')[1].click();" target="_self">
        <img src="https://i.ibb.co/yP2wjhW/jaka-02.png" alt="Logo JAKA" style="width:50px;height:50px;"/>
    </a>
    ''', unsafe_allow_html=True
)
    
    selected = option_menu(
        menu_title = 'Bernard Collin - Data Scientist',
        options = ['About Me','Main Projects'],
        icons = ['file-person-fill','collection-fill'],
        menu_icon = 'globe',
        default_index = 0,
        orientation = 'vertical',
        styles={
                "container": {"padding": "0!important", "background-color": "##00172B"},
                "icon": {"color": "#39B6B0", "font-size": "28px"}, 
                "nav-link": {"font-size": "12px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#00172B","font-size": "14px"},
            }
        
    )


if selected == 'Main Projects':
    coluna1,coluna2,coluna3 = st.columns([0.3,1,0.3])

    with coluna2:
        
        selected2 = option_menu(
        menu_title = 'Projects',
        options = ['Deep Learning and Computer Vision', 'Machine Learning and Analysis','Published Works'],
        icons = ['robot','gpu-card','journal-text'],
        menu_icon = 'boxes',
        default_index = 0,
            orientation = 'horizontal',
            styles={
                    "container": {"padding": "0!important", "background-color": "#edf2fb"},
                    "icon": {"color": "#39B6B0", "font-size": "28px"}, 
                    "nav-link": {"font-size": "12px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                    "nav-link-selected": {"background-color": "#00172B","font-size": "14px"},
                }
        )


    if selected2 ==  'Machine Learning and Analysis':
            with st.sidebar:
                selected_ml = option_menu(key = 'nham2',
                menu_title = 'Machine Learning Projects',
                options = ['Regression','Time Series','Clustering','Statistical Process Control'],
                icons = ['graph-down','graph-up-arrow','diagram-3-fill','sliders'],
                menu_icon = 'robot',
                default_index = 0,
                orientation = 'vertical',
                styles={
                "container": {"padding": "0!important", "background-color": "##00172B"},
                "icon": {"color": "#39B6B0", "font-size": "28px"}, 
                "nav-link": {"font-size": "12px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#00172B","font-size": "14px"},
            }
    )

            if selected_ml == 'Regression':
                from modules.machine_topics.regression import *
                regression_pag()

            if selected_ml == 'Statistical Process Control':
                from modules.machine_topics.statistical import *
                statistical()
                
            if selected_ml == 'Clustering':
                from modules.machine_topics.cluster import *
                clusters()
                
            if selected_ml == 'Time Series':
                from modules.machine_topics.time_series import *

                time_series()

                
    if selected2 == 'Deep Learning and Computer Vision':

        with st.sidebar:
            selected_dpl = option_menu(key = 'nham3',
            menu_title = 'Deep Learning and Computer Vision projects',
            options = ['Hand Tracking and Pose Estimation', 'Tracker and Classification - Mango Count','Object Detection - Fruit Fly (Pest)'],
            icons = ['person-bounding-box','123','bounding-box'],
            menu_icon = 'pip',
            default_index = 0,
            orientation = 'vertical',
            styles={
                "container": {"padding": "0!important", "background-color": "##00172B"},
                "icon": {"color": "#39B6B0", "font-size": "28px"}, 
                "nav-link": {"font-size": "12px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#00172B","font-size": "14px"},
            }
    )

        if selected_dpl == 'Tracker and Classification - Mango Count':
            from modules.deep_topics.mango import *
            mango_count()


        if selected_dpl == 'Object Detection - Fruit Fly (Pest)':

            from modules.deep_topics.fruit_fly import *
            fruit_fly()
            
        if selected_dpl == 'Hand Tracking and Pose Estimation':
            from modules.deep_topics.computer_vision import *
            computer_vision()

    
    if selected2 == 'Published Works':

        with st.sidebar:

            selected_pw = option_menu(key = 'nham5',
            menu_title = 'Published Works',
            options = ['Data analysis / predict car sales in Brazil / Covid-19 pandemic','Prediction of percentages of calibers in mango production'],
            icons = ['journal','book-half'],
            menu_icon = 'journal-text',
            default_index = 0,
            orientation = 'vertical',
            styles={
                "container": {"padding": "0!important", "background-color": "##00172B"},
                "icon": {"color": "#39B6B0", "font-size": "28px"}, 
                "nav-link": {"font-size": "12px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#00172B","font-size": "14px"},
            }
    )

        if selected_pw == 'Data analysis / predict car sales in Brazil / Covid-19 pandemic':
            from modules.published_topics.covid_study import *
            covid_study()
           

        if selected_pw == 'Prediction of percentages of calibers in mango production':
            from modules.published_topics.mango_size import *
            mango_size()

if selected == 'About Me':
    
    from modules.about_me.about_me import *
    about_me()

