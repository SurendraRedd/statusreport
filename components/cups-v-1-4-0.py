import streamlit as st
from streamlit_extras.stodo import to_do
import datetime
import json
import os

# Define tool version (you can set this dynamically based on user input or some other logic)
TOOL_VERSION = "v1.4.0"

# File path for persistent storage
DATA_FILE = f"cups-{TOOL_VERSION}.json"

# Function to load data from the file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {
        'todo_states': {
            f"{TOOL_VERSION}-1": False, f"{TOOL_VERSION}-2": False, f"{TOOL_VERSION}-3": False, f"{TOOL_VERSION}-4": False,
            f"{TOOL_VERSION}-5": False, f"{TOOL_VERSION}-6": False, f"{TOOL_VERSION}-7": False, f"{TOOL_VERSION}-8": False,
            f"{TOOL_VERSION}-9": False, f"{TOOL_VERSION}-10": False, f"{TOOL_VERSION}-11": False, f"{TOOL_VERSION}-12": False,
            f"{TOOL_VERSION}-13": False, f"{TOOL_VERSION}-14": False, f"{TOOL_VERSION}-15": False, f"{TOOL_VERSION}-16": False,
            f"{TOOL_VERSION}-17": False, f"{TOOL_VERSION}-18": False, f"{TOOL_VERSION}-19": False, f"{TOOL_VERSION}-20": False,
            f"{TOOL_VERSION}-21": False, f"{TOOL_VERSION}-22": False, f"{TOOL_VERSION}-23": False, f"{TOOL_VERSION}-24": False,
            f"{TOOL_VERSION}-25": False, f"{TOOL_VERSION}-26": False, f"{TOOL_VERSION}-27": False, f"{TOOL_VERSION}-28": False
        },
        'home_switches': {
            f"{TOOL_VERSION}-homeswitch1": False, f"{TOOL_VERSION}-homeswitch2": False, f"{TOOL_VERSION}-homeswitch3": False,
            f"{TOOL_VERSION}-homeswitch4": False, f"{TOOL_VERSION}-homeswitch5": False, f"{TOOL_VERSION}-homeswitch6": False
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

if 'observations1' not in st.session_state:
    st.session_state.observations1 = data['observations1']

if 'observations2' not in st.session_state:
    st.session_state.observations2 = data['observations2']

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

st.title(":point_down: CUPS V1.4.0 Release - :blue[Execution Details]")
st.markdown("---")

st.subheader("Prerequisites")
with st.expander("Details", expanded=True):
    to_do([(st.write, ":memo: OSM Signature Completed ?")], "1")
    to_do([(st.write, ":memo: System Requirements Signature Completed ?")], "2")
    to_do([(st.write, ":memo: Installation Guide Signature Completed ?")], "3")
    to_do([(st.write, ":memo: Installation Specification Signature Completed ?")], "4")

st.subheader("Workflows")
start_date_2 = st.date_input(":calendar: Execution Start Date", datetime.date(2024, 5, 22))
st.write("\n")

tab1, tab2, tab3, tab4 = st.tabs(["AKS Execution Details", "OCP Execution Details", "Openstack Execution Details", "EKS Execution Details"])

with tab1:
    # Create three columns
    col1, col2 = st.columns(2)

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
        st.subheader(":wastebasket: Uninstallation")
        with st.expander("Activities", expanded=True):
            to_do([(st.write, ":memo: Installation with PVC SEQ Signature Completed?")], "9")
            to_do([(st.write, ":memo: Uninstallation Plan & Report Signature Completed?")], "10")
            to_do([(st.write, ":memo: Uninstallation SEQ Signature Completed?")], "11")
            to_do([(st.write, ":memo: Servat Execution Completed?")], "12")
            st.write("---")
            home_switch_value2 = st.checkbox("Uninstallation Status (Yes/No)", value=st.session_state.home_switches["homeswitch2"], key="homeswitch2")
            st.session_state.home_switches["homeswitch2"] = home_switch_value2
            if home_switch_value2:
                st.metric(label=":checkered_flag: Completed", value="Yes", delta="")
            else:
                st.metric(label=":checkered_flag: Completed", value="No", delta="")

    txt = st.text_area(":memo: Notes", value=st.session_state.notes)
    st.session_state.notes = txt

    if home_switch_value1 and home_switch_value2:
        st.success('Overall Status: :trophy: Completed', icon="✅")
        end_date_2 = st.date_input(":calendar: Execution Completed Date", datetime.date(2024, 5, 23))
    elif not home_switch_value1 and not home_switch_value2:
        st.warning('Overall Status: :hourglass: Not Started', icon="⚠️")
    else:
        st.info('Overall Status: :hourglass_flowing_sand: In Progress', icon="ℹ️")

with tab2:
    # Create three columns
    col1, col2 = st.columns(2)

    # Status in each column
    with col1:
        st.subheader(":hammer_and_wrench: Installation")
        with st.expander("Activities", expanded=True):
            to_do([(st.write, ":memo: Initial SEQ Signature Completed?")], "13")
            to_do([(st.write, ":memo: Installation Plan & Report Signature Completed?")], "14")
            to_do([(st.write, ":memo: Installation SEQ Signature Completed?")], "15")
            to_do([(st.write, ":memo: Servat Execution Completed?")], "16")
            home_switch_value3 = st.checkbox(":memo: Installation (Yes/No)", value=st.session_state.home_switches["homeswitch3"], key="homeswitch3")
            st.session_state.home_switches["homeswitch3"] = home_switch_value3
            if home_switch_value3:
                st.metric(label=":checkered_flag: Completed", value="Yes", delta="")
            else:
                st.metric(label=":checkered_flag: Completed", value="No", delta="")
    with col2:
        st.subheader(":wastebasket: Uninstallation")
        with st.expander("Activities", expanded=True):
            to_do([(st.write, ":memo: Installation with PVC SEQ Signature Completed?")], "17")
            to_do([(st.write, ":memo: Uninstallation Plan & Report Signature Completed?")], "18")
            to_do([(st.write, ":memo: Uninstallation SEQ Signature Completed?")], "19")
            to_do([(st.write, ":memo: Servat Execution Completed?")], "20")
            home_switch_value4 = st.checkbox(":memo: Uninstallation (Yes/No)", value=st.session_state.home_switches["homeswitch4"], key="homeswitch4")
            st.session_state.home_switches["homeswitch4"] = home_switch_value4
            if home_switch_value4:
                st.metric(label=":checkered_flag: Completed", value="Yes", delta="")
            else:
                st.metric(label=":checkered_flag: Completed", value="No", delta="")

    txt1 = st.text_area(":memo: Observations", value=st.session_state.observations)
    st.session_state.observations = txt1

    if home_switch_value3 and home_switch_value4:
        st.success('Overall Status: :trophy: Completed', icon="✅")
    elif not home_switch_value3 and not home_switch_value4:
        st.warning('Overall Status: :hourglass: Not Started', icon="⚠️")
    else:
        st.info('Overall Status: :hourglass_flowing_sand: In Progress', icon="ℹ️")

with tab3:
    # Create three columns
    col1, col2 = st.columns(2)

    # Status in each column
    with col1:
        st.subheader(":hammer_and_wrench: Installation")
        with st.expander("Activities", expanded=True):
            to_do([(st.write, ":memo: Initial SEQ Signature Completed?")], "21")
            to_do([(st.write, ":memo: Installation Plan & Report Signature Completed?")], "22")
            to_do([(st.write, ":memo: Installation SEQ Signature Completed?")], "23")
            to_do([(st.write, ":memo: Servat Execution Completed?")], "24")
            home_switch_value5 = st.checkbox(":memo: Installation (Yes/No)", value=st.session_state.home_switches["homeswitch5"], key="homeswitch5")
            st.session_state.home_switches["homeswitch5"] = home_switch_value5
            if home_switch_value5:
                st.metric(label=":checkered_flag: Completed", value="Yes", delta="")
            else:
                st.metric(label=":checkered_flag: Completed", value="No", delta="")
    with col2:
        st.subheader(":wastebasket: Uninstallation")
        with st.expander("Activities", expanded=True):
            to_do([(st.write, ":memo: Installation with PVC SEQ Signature Completed?")], "25")
            to_do([(st.write, ":memo: Uninstallation Plan & Report Signature Completed?")], "26")
            to_do([(st.write, ":memo: Uninstallation SEQ Signature Completed?")], "27")
            to_do([(st.write, ":memo: Servat Execution Completed?")], "28")
            home_switch_value6 = st.checkbox(":memo: Uninstallation (Yes/No)", value=st.session_state.home_switches["homeswitch6"], key="homeswitch6")
            st.session_state.home_switches["homeswitch6"] = home_switch_value4
            if home_switch_value6:
                st.metric(label=":checkered_flag: Completed", value="Yes", delta="")
            else:
                st.metric(label=":checkered_flag: Completed", value="No", delta="")

    txt3 = st.text_area(":memo: Observations2", value=st.session_state.observations2)
    st.session_state.observations2 = txt3

    if home_switch_value5 and home_switch_value6:
        st.success('Overall Status: :trophy: Completed', icon="✅")
    elif not home_switch_value5 and not home_switch_value6:
        st.warning('Overall Status: :hourglass: Not Started', icon="⚠️")
    else:
        st.info('Overall Status: :hourglass_flowing_sand: In Progress', icon="ℹ️")

with tab4:
    # Create three columns
    col1, col2 = st.columns(2)

    # Status in each column
    with col1:
        st.subheader(":hammer_and_wrench: Installation")
        with st.expander("Activities", expanded=True):
            to_do([(st.write, ":memo: Initial SEQ Signature Completed?")], "29")
            to_do([(st.write, ":memo: Installation Plan & Report Signature Completed?")], "30")
            to_do([(st.write, ":memo: Installation SEQ Signature Completed?")], "31")
            to_do([(st.write, ":memo: Servat Execution Completed?")], "32")
            home_switch_value5 = st.checkbox(":memo: Installation (Yes/No)", value=st.session_state.home_switches["homeswitch5"], key="homeswitch5")
            st.session_state.home_switches["homeswitch5"] = home_switch_value5
            if home_switch_value5:
                st.metric(label=":checkered_flag: Completed", value="Yes", delta="")
            else:
                st.metric(label=":checkered_flag: Completed", value="No", delta="")
    with col2:
        st.subheader(":wastebasket: Uninstallation")
        with st.expander("Activities", expanded=True):
            to_do([(st.write, ":memo: Installation with PVC SEQ Signature Completed?")], "33")
            to_do([(st.write, ":memo: Uninstallation Plan & Report Signature Completed?")], "34")
            to_do([(st.write, ":memo: Uninstallation SEQ Signature Completed?")], "35")
            to_do([(st.write, ":memo: Servat Execution Completed?")], "36")
            home_switch_value6 = st.checkbox(":memo: Uninstallation (Yes/No)", value=st.session_state.home_switches["homeswitch6"], key="homeswitch6")
            st.session_state.home_switches["homeswitch6"] = home_switch_value4
            if home_switch_value6:
                st.metric(label=":checkered_flag: Completed", value="Yes", delta="")
            else:
                st.metric(label=":checkered_flag: Completed", value="No", delta="")

    txt4 = st.text_area(":memo: Observations1", value=st.session_state.observations1)
    st.session_state.observations1 = txt4

    if home_switch_value5 and home_switch_value6:
        st.success('Overall Status: :trophy: Completed', icon="✅")
    elif not home_switch_value5 and not home_switch_value6:
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
        st.write(DATA_FILE)
        json_data = json.load(file)
        st.json(json_data)
