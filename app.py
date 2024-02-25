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

# Add Title
st.title("Use Pygwalker In Streamlit")

# Import your data
df = pd.read_csv("removed_ads_table_22_04_23.csv")

# Generate the HTML using Pygwalker
pyg_html = pyg.to_html(df)

# Embed the HTML into the Streamlit app
components.html(pyg_html, height=1000, scrolling=True)
