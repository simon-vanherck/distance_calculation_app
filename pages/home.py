import streamlit as st
import numpy as np
import pandas as pd
import time
import google_api_client

def app():
    """Used to write the page in the app.py file"""
    uploaded_file = st.sidebar.file_uploader("Choose a file to upload", accept_multiple_files=False, type=["xlsx","xls"])

    if uploaded_file is not None:

        file_name = str(uploaded_file.name)
        data_source = pd.read_excel(uploaded_file)

        st.write("Uploaded Dataframe :")
        st.write(data_source)
    
        column_names = list(data_source.columns.values)
        
        TOBE_destinations = []
        TOBE_destinations = st.sidebar.multiselect("Select all TO BE destinations",column_names)
        text_input = st.sidebar.selectbox('Select Employee ID column name',column_names)        

        estimated_cost = st.sidebar.write(
            str('Estimated cost for distance calculation: '+
            str(len(TOBE_destinations)*len(data_source.index)*0.005)+str(' €'))
            )
        submit_button = st.sidebar.button(label='Submit')
        

        if submit_button == True :
            google_api_client.update_reports()

            with st.spinner('Fetching employee data...'):
                data_source = google_api_client.get_private_address(data_source,employee_id_column= text_input)
                data_source = google_api_client.get_work_address(data_source,employee_id_column= text_input)
                data_source.replace(np.nan,"", inplace = True)
                data_source.dropna(axis=0, how="all" ,inplace= True)
            st.success('Employee Data Fetched!')

            google_api_client.update_depature_time()

            #add a progress bar based on the number of rows * the number of columns
            counter = 0
            with st.spinner('Evaluationg distances...'):
                progress_bar = st.progress(0.0)
                offset = 0.0
                for i in TOBE_destinations:
                    data_source[i] = google_api_client.get_distance(
                        data_source,
                        origins_col=data_source["Private Address"].name,
                        destinations_col=i,
                        progress_cb=lambda count: progress_bar.progress(count + offset),
                        total=len(TOBE_destinations) * len(data_source.index),
                    )
                    offset += 1.0 / len(TOBE_destinations)

            st.success('distances calculated !')

            print(type(data_source))
            data_source.to_excel(file_name)
            st.write(file_name)