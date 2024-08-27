import streamlit as st
from streamlit_extras.stodo import to_do
import datetime
import json
import os

# Define tool version (you can set this dynamically based on user input or some other logic)
TOOL_VERSION = "v1.0.0"

# File path for persistent storage
DATA_FILE = f"OpenStack-{TOOL_VERSION}.json"