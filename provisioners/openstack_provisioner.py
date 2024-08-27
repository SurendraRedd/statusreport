import streamlit as st
from streamlit_extras.stodo import to_do
import datetime
import json
import os

# Define tool version (you can set this dynamically based on user input or some other logic)
TOOL_VERSION = "v1.0.0"

# File path for persistent storage
DATA_FILE = f"OpenStack-{TOOL_VERSION}.json"

# Create navigation
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Header template
html_temp = """
<body style="background-color:red;">
<div style="background-color:blue;padding:10px">
<h3 style="color:white;text-align:center;"> Home Page</h3>
</div>
</body>
"""
# st.markdown(html_temp, unsafe_allow_html=True)

hide_footer_style = """
<style>
.reportview-container .main footer {visibility: hidden;}    
</style>
"""
st.markdown(hide_footer_style, unsafe_allow_html=True)

st.title(":point_down: OpenStack V1.0.0 Release - :blue[Execution Details]")
st.markdown("---")

st.subheader("Prerequisites")
with st.expander("Details", expanded=True):
    to_do([(st.write, ":memo: OSM Signature Completed ?")], "1")
    to_do([(st.write, ":memo: System Requirements Signature Completed ?")], "2")
    to_do([(st.write, ":memo: Installation Guide Signature Completed ?")], "3")
    to_do([(st.write, ":memo: Installation Specification Signature Completed ?")], "4")

st.subheader("Workflows")
start_date_1 = st.date_input(":calendar: Execution Start Date", datetime.date(2024, 8, 27))
st.write("\n")