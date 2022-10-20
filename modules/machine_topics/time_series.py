from pickletools import stackslice
from streamlit_option_menu import option_menu
import streamlit as st
import requests 
from streamlit_lottie import st_lottie

import webbrowser

def time_series():

    from PIL import Image
    st.success('# ARIMA')
    st.write('___')
    coluna1, coluna2,coluna3 = st.columns([0.2,1,0.2])
    
    coluna2.write("""  
    - #### In this topic will be presented the results of an ARIMA model used to predict the Accumulated Weekly Degrees Day in a determined region of plantation.
        - ##### Degree day in agriculture reflects the thermal heating needs of the fruit for its development.
        - ##### As it is a variable directly related to the climate, Time Series was the best forecasting strategy applied in order to predict this heat accumulation during the annual weeks.
    """)

    

    st.write('___')





    st.info("""  ### Variabel Analysis and Correlation """)
    st.write('___')

    col21, col22, col23 = st.columns([1,1,1])
    st.write('___')

    img = Image.open('images/arima_model/adf_test.png')

    col21.image(img, use_column_width=True)

    col22.write(' ')
    col22.write(' ')
    col22.write(' ')
    col22.write(' - ##### Through the Augmented Dickey Fuller test, it was possible to identify that the series is stationary, as the p-value was lower than the significance level. ')
    col23.write(' ')
    col23.write(' ')
    col23.write(' ')
    col23.write("""
    - ##### In the other graphs, the 3-year behavior of the varieval can be observed, where the x-axis represents the weeks of each year.
        - The autocorrelation and partial correlation graphs that guide the choices of P,D and Q are also present.
    
    """)



    col1, col2, col3,col4 = st.columns([1,1,1,1])

    from PIL import Image

    img = Image.open('images/arima_model/gd_comportamento.png')

    img2 = Image.open('images/arima_model/autocorr_plot.png')
    img3 = Image.open('images/arima_model/auto_and_partial_corr.png')

    img4 = Image.open('images/arima_model/autorcorr.png')
    #img4 = Image.open('arima_model/gd_comportamento.png')



    col1.image(img, use_column_width=True)

    col2.write(' ')
    col2.image(img2, use_column_width=True)
    col3.image(img3, use_column_width=True)
    col4.image(img4, use_column_width=True)
    

    
    


    st.info("""  ###  Residuals  """)
    st.write('___')

    coll1, coll2, coll3,col4, col5 = st.columns([1,1.5,0.2,1.5,1])

    
    img = Image.open('images/arima_model/kde_residuos.png')
    #img2 = Image.open('regression_model/percents_amost.png')
    # img3 = Image.open('regression_model/pivot.png')


    coll2.write(' ')
    coll2.write(' ')
    coll2.image(img, use_column_width=True)
    #coll2.image(img3, use_column_width=True)
    #coll2.image(img2, use_column_width=True)
    
    
    col4.write(' ')

 
   
    


    col4.write(""" 

        - ##### With the help of the Plotly library, the Histogram was plotted along with the KDE of Residuals, where it appears to have a normal distribution with a higher density around 0:
        - It was also identified that the 1st quartile is represented by the value -14 and 75% of the errors are up to 13.
        - Considering that this is a variable with a standard deviation of 28 and a mean of 83, the errors were considered acceptable..
        """ )

    col4.write('___')

    st.write('___')


    st.info (""" ### Predict """)
    st.write('___')

    coll11, coll22, col33 = st.columns([0.2,1,0.2])

    img = Image.open('images/arima_model/predict.png')

    
    coll22.image(img, use_column_width=True)
    st.write('___')
