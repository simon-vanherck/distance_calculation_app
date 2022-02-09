import os
import requests
import json
import pandas as pd
import numpy as np
from datetime import datetime, date, time
import time
from datetime import datetime


import googlemaps

#google API key - do not share
gmaps_key =''
#download_path1 = os.getcwd()+'/data/reports/Staff_Allocation.xlsx'
#download_path2 = os.getcwd()+'/data/reports/Personaldata.xlsx'
#Evaluate departure time with the following rule :
#1st business monday of the following month at 8AM. 
#Eg. If we are the 7/04 then we take the next month, first business monday which is a 3/05/2021
def update_depature_time():
    global departure_time
    today_date = pd.Timestamp.today()
    departure_date = today_date + pd.tseries.offsets.BMonthBegin(0)
    departure_time = departure_date.replace(hour=8, minute=0, second=0, microsecond=0)
    return departure_time


departure_time = datetime.now()


def get_distance(data_source, origins_col, destinations_col, progress_cb, total):
    distance_matrix_results =[] #empty results column before recalling function
    mode="driving"
    language="en"
    units="metric"
    traffic_model="pessimistic"
    avoid=None
    transit_mode=None
    transit_routing_preference=None
    region=None
    arrival_time=None
    gmaps = googlemaps.Client(key=gmaps_key)
    total_counter = 0.0
    for index, row in data_source.iterrows():
        if row[destinations_col] =="":
            distance_matrix_results.append("")
        else:    
            origins = row[origins_col]
            destinations = row[destinations_col]
            response = gmaps.distance_matrix(origins, destinations, mode, language, avoid, units, departure_time, arrival_time, transit_mode, transit_routing_preference, traffic_model, region)
            try:
                response = response["rows"][0]["elements"][0]["distance"]["value"]/1000
                distance_matrix_results.append(response)
            except:
                distance_matrix_results.append("Problem")
        total_counter = total_counter + 1
        print(total_counter / total)
        progress_cb(total_counter / total)
    return distance_matrix_results