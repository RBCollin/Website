from pickletools import stackslice
from streamlit_option_menu import option_menu
import streamlit as st
import requests 
from streamlit_lottie import st_lottie

import webbrowser

def covid_study():
            st.success("### Data analysis and machine learning techniques in the analysis of car sales in Brazil during the Covid-19 pandemic")
            st.write(" #### Abstract")
            st.write("""  
            - This study aims to analyze the impacts of Covid-19 on vehicle sales in Brazil, correlating these factors with semiconductors imports and economic indicators using Machine Learning models. For this, a collection and preparation of data took place before performing the exploratory analysis, and therefore the developing the predictive models. This work is characterized as an applied and exploratory research, with a quantitative approach. The Python language was used to perform exploratory analysis and to create the models. The data used in this study were collected from multiples sources of private companies, government, associations and research institutes. Three regression algorithms were used: Random Forest, Multi-Layer Perceptron and Multiple Linear Regression. The neural network presented the best results among the applied algorithms, reaching an R² of 82.01% in the test data set. After the exploratory analysis, it was also noticed the high impact that semiconductors have on vehicle sales and the drastic effects caused by Covid-19 on the variables used in the study. With the model created, it is possible to predict the sales of vehicles in Brazil in a given month based on some economic indicators, semiconductor imports and the monthly deaths of Covid-19  """)


            st.write("[You can find the article here or consult the DOI Link at the bottom: (Portuguese) >](https://navus.sc.senac.br/index.php/navus/article/view/1717/pdf)")
            st.write("DOI: https://doi.org/10.22279/navus.2022.v12.p01-24.1717")

            st.write(""" 
            - #### Mains Results:""")

            coluna1, coluna2 = st.columns(2)
            from PIL import Image
            img1 = Image.open('images/published/results_navus1.png')
            img2 = Image.open('images/published/results_navus2.png')
            

            newsize = (416,416)
            img1_n = img1.resize(newsize)
            img2_n = img2.resize(newsize)
            


            coluna1.image(img1, use_column_width=True)
            coluna2.write(""" 
                - The performance measurements of the models with the training and testing data can be consulted in the table on the side, the measurements used were the RMSE and R². where the best performance of Random Forest for the training data is evident, however, with new data the MLP Regressor presented more expressive results in all measurements""")
            coluna1.write('')
            coluna1.write('')
            coluna1.image(img2, use_column_width=True)
            coluna2.write('')
            coluna2.write('')
            coluna2.write('')
            coluna2.write('')
            coluna2.write('')
            coluna2.write(""" 
                - This graph represents the performance of the MLP Regressor for the new data, the red line represents the actual values ​​in car units sold in one month, and the dark line represents the model estimate. """)
