from pickletools import stackslice
from streamlit_option_menu import option_menu
import streamlit as st
import requests 
from streamlit_lottie import st_lottie

import webbrowser

def regression_pag():
    st.success('# Regression')
    st.write('___')
    coluna1, coluna2, coluna3 = st.columns([0.2,1,0.2])

    coluna2.write("""  #### In this topic, the main points obtained with the study will be addressed, the details of preparation, normalization and treatment of the data are not fully explicit. The results were only achieved after a long and time-consuming analysis of data and treatments to adopt the best strategies to eliminate bias considering the various variables present, the points addressed here are summaries of the real case. """)

    st.write('___')
    st.info("""  ### Performance """)

    col1, col2, col3 = st.columns([1,1,0.2])

    from PIL import Image
    img = Image.open('images/regression_model/medias_grupos_previsao.png')
    newsize = (1300,700)
    img2 = img.resize(newsize)
    col1.image(img, use_column_width=True)

    col2.write(' ')
    col2.write(' ')
    col2.write(' ')

    col2.write(' - ##### The model created provides predictions, in percentages, of the concentration of each mango weight class within a set of mangoes produced in a planted area. Each variable on the x-axis represents a specific fruit size group.')
    col2.write(' - ##### In this graph it is possible to identify an average distribution of groups of a set of areas that were applied in the model, the light blue represents the predicted average of this set of areas for each class. It is noticed that the model can adjust very well to the real data, solving the proposed problem.')


    st.info("""  ###  Data Trataments  """)
    st.write('___')

    coll1, coll2, coll3 = st.columns([1,1,1])


    img = Image.open('images/regression_model/merge_groupby.png')
    img2 = Image.open('images/regression_model/percents_amost.png')
    img3 = Image.open('images/regression_model/pivot.png')

    coll1.image(img, use_column_width=True)
    coll2.image(img3, use_column_width=True)
    coll2.image(img2, use_column_width=True)


    coll3.write(' ')
    coll3.write(' ')
    coll3.write(' ')
    coll3.write(' ')


    coll3.write('___')
    coll3.write(""" 

        - ##### A number of strategies were adopted to make the dataset look optimal:
        - Strategies such as Merge, Groupby and Pivot were the most used to create a set of necessary variables that reflected reality and could be interpreted by the model..
        """ )

    coll3.write('___')

    st.write('___')


    st.info (""" ### Resume: Analysis and Outliers """)
    st.write('___')

    coll11, coll22 = st.columns([1,1])

    img = Image.open('images/regression_model/histogram_plotly.png')
    img2 = Image.open('images/regression_model/plotly_outliers.png')
    img3 = Image.open('images/regression_model/remove_outliers_z_score.png')

    coll11.image(img, use_column_width=True)
    coll22.image(img2, use_column_width=True)
    coll22.image(img3, use_column_width=True)
    coll22.write(""" 
    -  ##### The graphic library used was Plotly, the strategies for removing and identifying outliers were: 
        - Boxplot and the Z-score considering a deviation of up to 1.5 from the mean.
                        """)
    coll11.write(' - ##### One of the main insights obtained with the analysis was the identification of the different percentage concentration behaviors that each mango weight class varies with the advance of the days.')
    st.write('___')

    st.info("""  ### Model Metrics """)
    st.write('___')


    coll11, coll22 = st.columns([1,1])

    img = Image.open('images/regression_model/model_metrics.png')
    img2 = Image.open('images/regression_model/comparativo_total_grupos.png')

    coll11.image(img, use_column_width=True)
    coll22.write('')
    coll22.write(' - ##### The model performed very well with a fit of 87.09% for the test data and predicted totals very close to the actual percentages, perceptible by the pie charts for each sub-group. Such metrics reinforce the good fit, identified in the performance topic, when the model was put into practice with new data.')
    coll22.write('___')

    #coll22.write(' - ###### A linha verde no gráfico exemplifica o erro real para cada previsão fornecida pelo modelo, perceb-se que a mesma concentra-se aço entre 5 e -5 %, o que mais uma vez reflete a sua métrica RMSE de 3.86 % ')

    coll22.image(img2, use_column_width=True)
    coll22.write('___')
    coll22.write(' - ##### The green line in the graph exemplifies the real error for each prediction provided by the model, it can be seen that it concentrates steel between 5 and -5 %, which reflects its RMSE metric of 3.86 %')

    st.write('___')


    st.info("""  ### Error Analysis """)
    st.write('___')


    coll11, coll22 = st.columns([1,1])

    img = Image.open('images/regression_model/real_cases_error_analysis.png')


    coll11.image(img, use_column_width=True)
    coll22.write(' ')
    coll22.write(' ')
    coll22.write(' ')
    coll22.write(' ')
    coll22.write( """
    - ##### The model was applied to predict new datasets, and the results show that the model tends to err when the distance of days from the forecast increases and when another variable, in orange, is underperforming. 
        - ##### This variable reflects one of the essential steps of the process, and when it is a high value, the more imprecise that variable is.""")
    st.write('___')
