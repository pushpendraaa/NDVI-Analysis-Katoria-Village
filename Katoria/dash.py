import streamlit as st
import pandas as pd
import streamlit.components.v1 as components 
import numpy as np
import plotly.express as px
import chart_studio.plotly as py
import chart_studio.tools as tls
import plotly.graph_objs as go
import plotly.express as px
from streamlit_option_menu import option_menu
from PIL import Image


#title
st.markdown( 
 '<div> Katoria NDVI Analysis</div>', 
 unsafe_allow_html = True
 )

st.markdown('\n')

# with open("styles.css", "r") as source_style:
#  st.markdown(f"<style>{source_style.read()}</style>", 
#              unsafe_allow_html = True)
header_project = st.container()
data_collection = st.container()
data_analysis = st.container()


#add a sidebar

df = pd.read_csv("Katoria.csv")

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=[
            "Project Information",            
            "Interactive Data Analysis",
            "Insights"              
        ],
        default_index=0,
    )
if selected == "Project Information":

    with header_project:
        st.subheader("Introduction")
        introduction_str=""" 
        The project aims to turn wasteland into green land in a village located in Katoria 
        using time series analysis of NDVI (Normalized Difference Vegetation Index) using
        GEE (Google Earth Engine). The project aims to address the problem of land degradation
        and desertification in the area due to unsustainable land use practices, deforestation,
        and climate change. These factors have resulted in the degradation of the ecosystem
        services and the loss of livelihoods for the local communities. The solution proposed
        is to use remote sensing technology and time series analysis of NDVI to monitor vegetation
        dynamics and to identify the areas with the potential to regenerate and restore vegetation cover.
        The analysis will be conducted using GEE, a cloud-based platform that allows for the analysis
        of large volumes of satellite imagery and geospatial data.
        """
        st.text(introduction_str)

        st.subheader("Our Solution")

        our_solution_str=""" 
        We Developed a machine learning model, which predicts the NDVI for the next period in the Katoria Village.
        This will help the farmers to know about the NDVI trends of the plant, through which they can pre-plan the 
        growth of the plants correctly.
        """
        st.text(our_solution_str)


        st.subheader("The Data")

        the_dat_Srt=""" 
        We have used the Google Earth Engine (GEE) for the data collection of Katoria region in Bihar,
        The NDVI values was extracted from the Landsat imagery using GEE's algorithms, and the time series
        analysis of NDVI will be conducted to  identify the areas with the potential for restoration and to
        assess the vegetation dynamics over time.
        """
        st.text(the_dat_Srt)
if selected == "Interactive Data Analysis":
    st.sidebar.subheader("Visualisation Settings")
    # add a checkbox to show/hide dataset
    show_data = st.sidebar.checkbox("Show dataset")

    if show_data:
        st.write(df)

    global numeric_columns
    try:
        numeric_columns  = list(df.select_dtypes(['float','int' ]).columns)
    except Exception as e:
        print(e)
    chart_select = st.sidebar.selectbox(
        label = 'Select the Chart Type',
        options = ['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot']
    )
    if chart_select =='Scatterplots':
        st.sidebar.subheader('Scatterplot Settings')
        try:
            x_values = st.sidebar.selectbox('X axis', options = numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options = numeric_columns)
            plot = px.scatter(data_frame = df, x = x_values, y = y_values)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)
    if chart_select =='Lineplots':
        st.sidebar.subheader('Lineplots Settings')
        try:
            x_values = st.sidebar.selectbox('X axis', options = numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options = numeric_columns)
            plot = px.area(data_frame = df, x = x_values, y = y_values)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)
    if chart_select =='Boxplots':
        st.sidebar.subheader('Boxplot Settings')
        try:
            x_values = st.sidebar.selectbox('X axis', options = numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options = numeric_columns)
            plot = px.box(data_frame = df, x = x_values, y = y_values)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)
    if chart_select == 'Histogram':
        st.sidebar.subheader('Histogram Settings')
        try:
            x_values = st.sidebar.selectbox('Select the variable to plot histogram', options = numeric_columns)
            bins = st.sidebar.slider("Select the number of bins", min_value=5, max_value=50, value=20, step=1)
            plot = px.histogram(data_frame = df, x = x_values, nbins=bins)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)
if selected == "Insights":
    image = Image.open('crop.png')
    st.image(image, caption='Crop Calendar')
    with header_project:
        st.subheader("Crop Calendar")
        crop_str=""" 
        May: This is the time for land preparation, such as plowing, harrowing, leveling, and bunding.
        June: Rice seeds are sown during this month. Farmers usually start with early-maturing varieties
        in lowland areas and then move on to the main crop.
        July: This month is critical for the growth of rice plants, as it is the time when monsoon rains
        arrive in most parts of India. Farmers need to ensure that the fields are adequately flooded and
        the young plants are not submerged.
        August: The rice plants start to tiller (produce side shoots) during this month, which helps to
        increase the number of panicles (flower clusters) and eventually the number of grains per panicle.
        September: This is the month when the rice plants start to flower. Farmers need to be vigilant to
        prevent damage from pests and diseases.
        October: The rice plants start to form grains during this month. Farmers need to ensure that the
        fields are kept flooded and that there is enough sunlight for the grains to mature.
        November: This is the month when the rice plants start to mature, and the grains start to turn yellow.
        Farmers need to monitor the fields and start preparing for harvest.
        December: This is the time for harvesting the rice crop. Farmers usually harvest the crop manually
        or with the help of machines. Once the rice is harvested, it is dried, threshed, and stored for later use.
        January: After the harvest, farmers usually prepare the fields for the next crop by plowing, harrowing,
        and applying fertilizers.
        """
        st.text(crop_str)
    with header_project:
        st.subheader("Forecasting and Analysis")
        import streamlit as st

# Display a message that includes the Colab link
        st.write("Check out this Colab notebook (https://colab.research.google.com/drive/1JGPFoVrahgPafikYoaocA30IF3Bgm8JP#scrollTo=ItJdgY4Mx5nm")
