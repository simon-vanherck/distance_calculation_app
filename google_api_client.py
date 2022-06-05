import os
import requests
import json
import pandas as pd
import numpy as np
from datetime import datetime, date, time
import googlemaps


def get_distance(data_source, requested_parameters, origins_col, destinations_col, progress_cb, total):
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
    gmaps = googlemaps.Client(key=requested_parameters['api_key'])
    total_counter = 0.0
    for index, row in data_source.iterrows():
        if row[destinations_col].empty:
            distance_matrix_results.append("")
        else:    
            origins = row[origins_col]
            destinations = row[destinations_col]
            response = gmaps.distance_matrix(origins=origins, destinations=destinations,mode=requested_parameters['transit_routing_preference'])
            try:
                response = response["rows"][0]["elements"][0]["distance"]["value"]/1000
                distance_matrix_results.append(response)
            except:
                distance_matrix_results.append("error")
        total_counter = total_counter + 1
        print(total_counter / total)
        progress_cb(total_counter / total)
    return distance_matrix_results