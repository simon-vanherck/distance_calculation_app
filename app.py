import streamlit as st
import numpy as np
import pandas as pd
import time
import google_api_client


from pages import home, dashboard
from multipage import MultiPage

app = MultiPage()

st.sidebar.title('Google API Client')
#add a drop downmenu to navigate through files.

app.add_page("Home", home.app)
app.add_page("Dashboard", dashboard.app)

app.run()