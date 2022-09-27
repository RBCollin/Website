from pickletools import stackslice
from streamlit_option_menu import option_menu
import streamlit as st
import requests 
from streamlit_lottie import st_lottie

import webbrowser

def clusters():
    st.write('___')
    from PIL import Image
    col1, col2, col3 = st.columns([1,0.2,1])


    col1.success('# Clustering')
    
    col1.write(""" - ##### In this section I’ll show the main strategies that generally I use to unsupervised problems. For clustering I really like to use K-Means, evaluating the number of clusters through the metric "Silhoutte Score" as well as the graphic representation of the clusters characterized by this metric. Finally, I use Plotly for 2d or 3d plots when possible to have a dimensional view of the variable groups.""")
    col1.write(' - ###### To achieve these results, K-Means was used as a strategy, determining the number of clusters through the Silhoutte Score metric and the graphic performance of the groups.')

    col1.write('___')
    col1.write(' ')


    col3.info(""" - ### Example of Clustering used. """)


    video_file = open('images/clustering/clustering.mp4', 'rb')
    video_bytes = video_file.read()
        
    col3.video(video_bytes)

            
    col1.info(""" # K-Means """)
    
    img = Image.open('images/clustering/escolha_cluster.png')
    col3.info(""" 
    - ### Silhoutte Score Metric """)

    col3.image(img, use_column_width=True)

    col1.write(""" 
    - ##### The choice of 4 clusters was due to the fact that it has an acceptable number of clusters and a good Silhoutte Score value, it can be seen from the graphs that the amount of K=4 allows all groups to have a proportional size, the groups are above the Silhoutte Score line and with few residues present in the clusters (negative X axis).
        - ###### It is worth mentioning that the data were previously normalized and standardized to not bias the clustering and affect the centroids of the groups.
    
        """)
    
    col1.write('___')
    col1.info(""" 
        ### Graphical representation of the Silhoutte Score Metric """ )

    col1.write(""" 
    - ##### I usually choose a number of clusters that have a balance between:
        - ###### A good number of clusters;
        - ###### Silhoutte Score Value;
        - ###### Proportion between groups;
        - ###### Silhoutte Score value below all clusters;
        - ###### Intensity of the number of residues by groups.
    
    """ )
