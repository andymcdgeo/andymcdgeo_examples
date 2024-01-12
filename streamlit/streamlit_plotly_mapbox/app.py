import streamlit as st
import plotly.express as px
import pandas as pd


def display_map(location_data:pd.DataFrame):

    fig = px.scatter_mapbox(location_data, lat="Latitude", lon="Longitude", zoom=3, 
                            hover_name='Well Name', hover_data=['Completion Year', 'Purpose'])

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig


# Setup streamlit page to be wide by default
st.set_page_config(layout='wide')

# Setup the file uploader
st.header('Upload a File')
st.write('Upload a CSV file containing latitude and longitude data')

uploaded_file = st.file_uploader('Upload Location Data')

#Check if file has been uploaded and display map
if uploaded_file:
    st.header('Well Location Map')
    df = pd.read_csv(uploaded_file, 
                     usecols=['wlbWellboreName', 'wlbNsDecDeg', 'wlbEwDesDeg', 'wlbPurposePlanned', 'wlbCompletionYear'])
    df.columns = ['Well Name', 'Purpose', 'Completion Year', 'Latitude', 'Longitude']
    
    px_map = display_map(df)

    st.plotly_chart(px_map, use_container_width=True)