from pickletools import stackslice
from streamlit_option_menu import option_menu
import streamlit as st
import requests 
from streamlit_lottie import st_lottie

import webbrowser

def mango_size():
            st.success("### Random Forest Regressor applied in prediction of percentages of calibers in mango production")
            st.write(" #### Abstract")
            st.write("""  
            - The aim of this study is to predict the percentage distribution of the calibers of mangos of 4 varieties in the largest exporter and producer of mangos in Brazil, as well as to measure the performance and the errors for each model created. To do so, a process of extraction and transformation of the data before the exploratory analysis was performed, and subsequent modeling of the predictive models. The entire process of analysis, use of the data, and modeling of the algorithms occurred in the Python language. The data used in the study originate from years of collection and integration of different sources of data carried out by the company. Four regression models were created using Random Forest (RF), one for each variety of the fruit that composes the dataset. The algorithms showed satisfactory results for the varieties Kent, Keitt, Tommy Atkins and Palmer, with the following R² of the models: 87.29%, 74.37%, 87.69%, and 62.75%, respectively. During the Feature Selection step, the high importance of Nitrogen (N) was perceived in all the models, highlighting the representative nature of this element in fruit formation. From the models created, it is possible to predict the percentage distribution of the calibers of mangos from each growing area 6 months in advance, using data that characterize each area, as well as information on the presence of leaf nutrients, as input. """)

            st.success('#### Manuscript recently submitted to magazine, wait for more details..')


            def get_lottie(url):
                r = requests.get(url)
                if r.status_code != 200:
                    return None
                return r.json()
            st.write(' ')
            lottie_icon = get_lottie('https://assets4.lottiefiles.com/packages/lf20_poqmycwy.json')
            st_lottie(lottie_icon, height = 220, key = 'lttie')