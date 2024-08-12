import streamlit as st
from streamlit_extras.stodo import to_do
import datetime
import json
import os

# File path for persistent storage
DATA_FILE = "lc-v1.1.2.json"

# Function to load data from the file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {
        'todo_states': {
            "1": False, "2": False, "3": False, "4": False,
            "5": False, "6": False, "7": False, "8": False,
            "9": False, "10": False, "11": False, "12": False,
            "13": False, "14": False, "15": False, "16": False,
            "17": False, "18": False, "19": False, "20": False,
            "21": False, "22": False, "23": False, "24": False,
            "25": False, "26": False, "27": False, "28": False
        },
        'home_switches': {
            "homeswitch1": False, "homeswitch2": False, "homeswitch3": False,
            "homeswitch4": False, "homeswitch5": False, "homeswitch6": False
        },
        'notes': "",
        'observations': ""
    }

# Function to save data to the file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

# Initialize session state
data = load_data()

if 'todo_states' not in st.session_state:
    st.session_state.todo_states = data['todo_states']

if 'home_switches' not in st.session_state:
    st.session_state.home_switches = data['home_switches']

if 'notes' not in st.session_state:
    st.session_state.notes = data['notes']

if 'observations' not in st.session_state:
    st.session_state.observations = data['observations']

# Function to display to-do items with checkboxes
def to_do(items, key):
    for item in items:
        func, text = item
        checked = st.session_state.todo_states[key]
        if st.checkbox(f"{text}", value=checked, key=f"todo_{key}"):
            st.session_state.todo_states[key] = True
        else:
            st.session_state.todo_states[key] = False

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

st.title(":point_down: Logging Collection V1.1.2 Release - :blue[Execution Details]")
st.markdown("---")

st.subheader("Prerequisites")
with st.expander("Details", expanded=True):
    to_do([(st.write, ":memo: OSM Signature Completed ?")], "1")
    to_do([(st.write, ":memo: System Requirements Signature Completed ?")], "2")
    to_do([(st.write, ":memo: Installation Guide Signature Completed ?")], "3")
    to_do([(st.write, ":memo: Installation Specification Signature Completed ?")], "4")

st.subheader("Workflows")
st.date_input(":calendar: Execution Start Date", datetime.date(2024, 5, 22))
st.write("\n")

tab1, tab2 = st.tabs(["AKS Execution Details", "OCP Execution Details"])

with tab1:
    # Create three columns
    col1, col2, col3 = st.columns(3)

    # Status in each column
    with col1:
        st.subheader(":hammer_and_wrench: Installation")
        with st.expander("Activities", expanded=True):
            to_do([(st.write, ":memo: Initial SEQ Signature Completed?")], "5")
            to_do([(st.write, ":memo: Installation Plan & Report Signature Completed?")], "6")
            to_do([(st.write, ":memo: Installation SEQ Signature Completed?")], "7")
            to_do([(st.write, ":memo: Servat Execution Completed?")], "8")
            st.write("---")
            home_switch_value1 = st.checkbox("Installation Stage Completed (Yes/No)", value=st.session_state.home_switches["homeswitch1"], key="homeswitch1")
            st.session_state.home_switches["homeswitch1"] = home_switch_value1
            if home_switch_value1:
                st.metric(label=":checkered_flag: Completed", value="Yes", delta="")
            else:
                st.metric(label=":checkered_flag: Completed", value="No", delta="")

    with col2:
        st.subheader(":package: Installation with PVC")
        with st.expander("Activities", expanded=True):
            to_do([(st.write, ":memo: Installation SEQ Signature Completed?")], "9")
            to_do([(st.write, ":memo: Installation Plan & Report Signature Completed?")], "10")
            to_do([(st.write, ":memo: Installation with PVC SEQ Signature Completed?")], "11")
            to_do([(st.write, ":memo: Servat Execution Completed?")], "12")
            st.write("---")
            home_switch_value2 = st.checkbox("Installation with PVC Stage Completed (Yes/No)", value=st.session_state.home_switches["homeswitch2"], key="homeswitch2")
            st.session_state.home_switches["homeswitch2"] = home_switch_value2
            if home_switch_value2:
                st.metric(label=":checkered_flag: Completed", value="Yes", delta="")
            else:
                st.metric(label=":checkered_flag: Completed", value="No", delta="")

    with col3:
        st.subheader(":wastebasket: Uninstallation")
        with st.expander("Activities", expanded=True):
            to_do([(st.write, ":memo: Installation with PVC SEQ Signature Completed?")], "13")
            to_do([(st.write, ":memo: Uninstallation Plan & Report Signature Completed?")], "14")
            to_do([(st.write, ":memo: Uninstallation SEQ Signature Completed?")], "15")
            to_do([(st.write, ":memo: Servat Execution Completed?")], "16")
            st.write("---")
            home_switch_value3 = st.checkbox("Uninstallation Status (Yes/No)", value=st.session_state.home_switches["homeswitch3"], key="homeswitch3")
            st.session_state.home_switches["homeswitch3"] = home_switch_value3
            if home_switch_value3:
                st.metric(label=":checkered_flag: Completed", value="Yes", delta="")
            else:
                st.metric(label=":checkered_flag: Completed", value="No", delta="")

    txt = st.text_area(":memo: Notes", value=st.session_state.notes)
    st.session_state.notes = txt

    if home_switch_value1 and home_switch_value2 and home_switch_value3:
        st.success('Overall Status: :trophy: Completed', icon="✅")
        st.date_input(":calendar: Execution Completed Date", datetime.date(2024, 5, 23))
    elif not home_switch_value1 and not home_switch_value2 and not home_switch_value3:
        st.warning('Overall Status: :hourglass: Not Started', icon="⚠️")
    else:
        st.info('Overall Status: :hourglass_flowing_sand: In Progress', icon="ℹ️")

with tab2:
    # Create three columns
    col1, col2, col3 = st.columns(3)

    # Status in each column
    with col1:
        st.subheader(":hammer_and_wrench: Installation")
        with st.expander("Activities", expanded=True):
            to_do([(st.write, ":memo: Initial SEQ Signature Completed?")], "17")
            to_do([(st.write, ":memo: Installation Plan & Report Signature Completed?")], "18")
            to_do([(st.write, ":memo: Installation SEQ Signature Completed?")], "19")
            to_do([(st.write, ":memo: Servat Execution Completed?")], "20")
            home_switch_value4 = st.checkbox(":memo: Installation (Yes/No)", value=st.session_state.home_switches["homeswitch4"], key="homeswitch4")
            st.session_state.home_switches["homeswitch4"] = home_switch_value4
            if home_switch_value4:
                st.metric(label=":checkered_flag: Completed", value="Yes", delta="")
            else:
                st.metric(label=":checkered_flag: Completed", value="No", delta="")

    with col2:
        st.subheader(":package: Installation with PVC")
        with st.expander("Activities", expanded=True):
            to_do([(st.write, ":memo: Installation SEQ Signature Completed?")], "21")
            to_do([(st.write, ":memo: Installation Plan & Report Signature Completed?")], "22")
            to_do([(st.write, ":memo: Installation with PVC SEQ Signature Completed?")], "23")
            to_do([(st.write, ":memo: Servat Execution Completed?")], "24")
            home_switch_value5 = st.checkbox(":memo: Installation with PVC (Yes/No)", value=st.session_state.home_switches["homeswitch5"], key="homeswitch5")
            st.session_state.home_switches["homeswitch5"] = home_switch_value5
            if home_switch_value5:
                st.metric(label=":checkered_flag: Completed", value="Yes", delta="")
            else:
                st.metric(label=":checkered_flag: Completed", value="No", delta="")

    with col3:
        st.subheader(":wastebasket: Uninstallation")
        with st.expander("Activities", expanded=True):
            to_do([(st.write, ":memo: Installation with PVC SEQ Signature Completed?")], "25")
            to_do([(st.write, ":memo: Uninstallation Plan & Report Signature Completed?")], "26")
            to_do([(st.write, ":memo: Uninstallation SEQ Signature Completed?")], "27")
            to_do([(st.write, ":memo: Servat Execution Completed?")], "28")
            home_switch_value6 = st.checkbox(":memo: Uninstallation (Yes/No)", value=st.session_state.home_switches["homeswitch6"], key="homeswitch6")
            st.session_state.home_switches["homeswitch6"] = home_switch_value6
            if home_switch_value6:
                st.metric(label=":checkered_flag: Completed", value="Yes", delta="")
            else:
                st.metric(label=":checkered_flag: Completed", value="No", delta="")

    txt1 = st.text_area(":memo: Observations", value=st.session_state.observations)
    st.session_state.observations = txt1

    if home_switch_value4 and home_switch_value5 and home_switch_value6:
        st.success('Overall Status: :trophy: Completed', icon="✅")
        st.date_input(":calendar: Execution Completed Date", datetime.date(2024, 5, 23))
    elif not home_switch_value4 and not home_switch_value5 and not home_switch_value6:
        st.warning('Overall Status: :hourglass: Not Started', icon="⚠️")
    else:
        st.info('Overall Status: :hourglass_flowing_sand: In Progress', icon="ℹ️")

# Save data on each interaction
data = {
    'todo_states': st.session_state.todo_states,
    'home_switches': st.session_state.home_switches,
    'notes': st.session_state.notes,
    'observations': st.session_state.observations
}
save_data(data)

# Display user_data.json content
with st.expander("View JSON Data"):
    with open(DATA_FILE, "r") as file:
        json_data = json.load(file)
        st.write(DATA_FILE)
        st.json(json_data)