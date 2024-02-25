import sys
sys.path.append('/usr/local/lib/python3.9/site-packages/pygwalker')
import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)


st.title("Use Pygwalker In Streamlit")  # Add Title
df = pd.read_csv("removed_ads_table_22_04_23.csv")  # Import your data
pyg_html = pyg.to_html(df)  # Generate the HTML using Pygwalker
components.html(pyg_html, height=1000, scrolling=True)  # Embed the HTML into the Streamlit app
