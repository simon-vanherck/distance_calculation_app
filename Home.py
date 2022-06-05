from urllib import request
import streamlit as st
import numpy as np
import pandas as pd
import time
import google_api_client
import os

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")
uploaded_file = st.sidebar.file_uploader("Choose a file to upload", accept_multiple_files=False, type=["xlsx","xls"])

if uploaded_file is not None:

    file_name = str(uploaded_file.name)
    data_source = pd.read_excel(uploaded_file)

    st.write("Uploaded Dataframe :")
    st.write(data_source)

    column_names = list(data_source.columns.values)
    
    requested_parameters = {
    }

    TOBE_destinations = []
    ORIGIN_column = st.sidebar.selectbox('Select origin column name',column_names)      
    TOBE_destinations = st.sidebar.multiselect("Select destination(s) column(s)",column_names)

    engine = st.sidebar.radio(label="Engine Choice", options=("Google Maps","Open Street Map (free)"))  

    if engine == "Google Maps":
        estimated_cost = st.sidebar.write(
            str('Estimated cost for distance calculation: '+
            str(len(TOBE_destinations)*len(data_source.index)*0.005)+str(' €'))
            )
        with st.container():
            st.write("Google API parameters menu")
            requested_parameters['api_key'] = st.text_input("Google API key")
            requested_parameters['transit_routing_preference'] = st.selectbox("Transportation mode",["driving","walking","bicycling","public transit"])
            requested_parameters['start_date'] = st.date_input("Start Date")
            requested_parameters['start_time'] = st.time_input("Start time")
    
    st.write(requested_parameters)
        
    submit_button = st.sidebar.button(label='Submit')
    

    if submit_button == True :


        #add a progress bar based on the number of rows * the number of columns
        counter = 0
        with st.spinner('Evaluating distances...'):
            progress_bar = st.progress(0.0)
            offset = 0.0
            for i in TOBE_destinations:
                data_source[str('distance for ')+i] = google_api_client.get_distance(
                    data_source,
                    requested_parameters,
                    origins_col= ORIGIN_column,
                    destinations_col=TOBE_destinations,
                    progress_cb=lambda count: progress_bar.progress(count + offset),
                    total=len(TOBE_destinations) * len(data_source.index)
                )
                offset += 1.0 / len(TOBE_destinations)

        st.success('distances calculated !')

        st.download_button(
            label='Download file',
            data=data_source.to_csv(),
            file_name='Calculated distance.csv',
            mime='text/csv',
        )

