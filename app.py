import streamlit as st
import numpy as np
import pandas as pd
import time
import google_api_client
from pages import home, dashboard

def main():
    pages = {
        "Home": home.app,
        "Dashboard":dashboard.app,
    }

    # If 'page' is present, update session_state with itself to preserve
    # values when navigating from Home to Settings.
    if "page" in st.session_state:
        st.session_state.update(st.session_state)

    # If 'page' is not present, setup default values for settings widgets.
    else:
        st.session_state.update({
            # Default page
            "page": "Home",

            # Radio, selectbox and multiselect options
            "options": ["Hello", "Everyone", "Happy", "Streamlit-ing"],

            # Default widget values
            "text": "",
            "slider": 0,
            "checkbox": False,
            "radio": "Hello",
            "selectbox": "Hello",
            "multiselect": ["Hello", "Everyone"],
        })


    with st.sidebar:
        page = st.radio("Select your page", tuple(pages.keys()))

    pages[page]()

if __name__ == "__main__":
    main()