#import plotly
import pandas as pd
import os
import streamlit as st
import plotly.express as px
data = os.getcwd()+"/data/tbl_calls.csv"
df = pd.read_csv(data, delimiter=';')
fig = px.line(df, x="date",y="calls", title="Historical record of calls")

st.write("This is the dashboard page but doesn't do anything yet")

with st.spinner("Loading Dashboard ..."):
    st.write()
    st.plotly_chart(fig, use_container_width=True)
        