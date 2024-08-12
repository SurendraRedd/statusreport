import streamlit as st
import datetime
import json
import os

# Define tool version (set this dynamically based on your logic)
TOOL_VERSION = "v1.2.1"

# File path for persistent storage
DATA_FILE = f"cups-{TOOL_VERSION}.json"

# Function to load data from the file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {
        'todo_states': {f"{TOOL_VERSION}-{i}": False for i in range(1, 29)},
        'home_switches': {f"{TOOL_VERSION}-homeswitch{i}": False for i in range(1, 7)},
        'notes': "",
        'observations': "",
        'start_date': datetime.date(2024, 5, 22).isoformat(),
        'completed_date': datetime.date(2024, 5, 23).isoformat()
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

if 'start_date' not in st.session_state:
    st.session_state.start_date = datetime.date.fromisoformat(data['start_date'])

if 'completed_date' not in st.session_state:
    st.session_state.completed_date = datetime.date.fromisoformat(data['completed_date'])

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

st.title(":point_down: CUPS V1.2.1 Release - :blue[Execution Details]")
st.markdown("---")

st.subheader("Prerequisites")
with st.expander("Details", expanded=True):
    to_do([(st.write, ":memo: OSM Signature Completed ?")], f"{TOOL_VERSION}-1")
    to_do([(st.write, ":memo: System Requirements Signature Completed ?")], f"{TOOL_VERSION}-2")
    to_do([(st.write, ":memo: Installation Guide Signature Completed ?")], f"{TOOL_VERSION}-3")
    to_do([(st.write, ":memo: Installation Specification Signature Completed ?")], f"{TOOL_VERSION}-4")

st.subheader("Workflows")
# Use unique keys for date inputs
start_date_key = f"{TOOL_VERSION}-start_date"
completed_date_key = f"{TOOL_VERSION}-completed_date"

st.session_state.start_date = st.date_input(
    ":calendar: Execution Start Date", 
    st.session_state.start_date,
    key=start_date_key
)
st.session_state.completed_date = st.date_input(
    ":calendar: Execution Completed Date", 
    st.session_state.completed_date,
    key=completed_date_key
)

st.write("\n")

tab1, tab2 = st.tabs(["AKS Execution Details", "OCP Execution Details"])

with tab1:
    # Create three columns
    col1, col2, col3 = st.columns(3)

    # Status in each column
    with col1:
        st.subheader(":hammer_and_wrench: Installation")
        with st.expander("Activities", expanded=True):
            to_do([(st.write, ":memo: Initial SEQ Signature Completed?")], f"{TOOL_VERSION}-5")
            to_do([(st.write, ":memo: Installation Plan & Report Signature Completed?")], f"{TOOL_VERSION}-6")
            to_do([(st.write, ":memo: Installation SEQ Signature Completed?")], f"{TOOL_VERSION}-7")
            to_do([(st.write, ":memo: Servat Execution Completed?")], f"{TOOL_VERSION}-8")
            st.write("---")
            home_switch_value1 = st.checkbox("Installation Stage Completed (Yes/No)", value=st.session_state.home_switches[f"{TOOL_VERSION}-homeswitch1"], key=f"{TOOL_VERSION}-homeswitch1")
            st.session_state.home_switches[f"{TOOL_VERSION}-homeswitch1"] = home_switch_value1
            if home_switch_value1:
                st.metric(label=":checkered_flag: Completed", value="Yes", delta="")
            else:
                st.metric(label=":checkered_flag: Completed", value="No", delta="")

    with col2:
        st.subheader(":package: Installation with PVC")
        with st.expander("Activities", expanded=True):
            to_do([(st.write, ":memo: Installation SEQ Signature Completed?")], f"{TOOL_VERSION}-9")
            to_do([(st.write, ":memo: Installation Plan & Report Signature Completed?")], f"{TOOL_VERSION}-10")
            to_do([(st.write, ":memo: Installation with PVC SEQ Signature Completed?")], f"{TOOL_VERSION}-11")
            to_do([(st.write, ":memo: Servat Execution Completed?")], f"{TOOL_VERSION}-12")
            st.write("---")
            home_switch_value2 = st.checkbox("Installation with PVC Stage Completed (Yes/No)", value=st.session_state.home_switches[f"{TOOL_VERSION}-homeswitch2"], key=f"{TOOL_VERSION}-homeswitch2")
            st.session_state.home_switches[f"{TOOL_VERSION}-homeswitch2"] = home_switch_value2
            if home_switch_value2:
                st.metric(label=":checkered_flag: Completed", value="Yes", delta="")
            else:
                st.metric(label=":checkered_flag: Completed", value="No", delta="")

    with col3:
        st.subheader(":wastebasket: Uninstallation")
        with st.expander("Activities", expanded=True):
            to_do([(st.write, ":memo: Installation with PVC SEQ Signature Completed?")], f"{TOOL_VERSION}-13")
            to_do([(st.write, ":memo: Uninstallation Plan & Report Signature Completed?")], f"{TOOL_VERSION}-14")
            to_do([(st.write, ":memo: Uninstallation SEQ Signature Completed?")], f"{TOOL_VERSION}-15")
            to_do([(st.write, ":memo: Servat Execution Completed?")], f"{TOOL_VERSION}-16")
            st.write("---")
            home_switch_value3 = st.checkbox("Uninstallation Status (Yes/No)", value=st.session_state.home_switches[f"{TOOL_VERSION}-homeswitch3"], key=f"{TOOL_VERSION}-homeswitch3")
            st.session_state.home_switches[f"{TOOL_VERSION}-homeswitch3"] = home_switch_value3
            if home_switch_value3:
                st.metric(label=":checkered_flag: Completed", value="Yes", delta="")
            else:
                st.metric(label=":checkered_flag: Completed", value="No", delta="")

    txt = st.text_area(":memo: Notes", value=st.session_state.notes)
    st.session_state.notes = txt

    if home_switch_value1 and home_switch_value2 and home_switch_value3:
        st.success('Overall Status: :trophy: Completed', icon="✅")
        st.session_state.completed_date = st.date_input(":calendar: Execution Completed Date", st.session_state.completed_date, key=completed_date_key)
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
            to_do([(st.write, ":memo: Initial SEQ Signature Completed?")], f"{TOOL_VERSION}-17")
            to_do([(st.write, ":memo: Installation Plan & Report Signature Completed?")], f"{TOOL_VERSION}-18")
            to_do([(st.write, ":memo: Installation SEQ Signature Completed?")], f"{TOOL_VERSION}-19")
            to_do([(st.write, ":memo: Servat Execution Completed?")], f"{TOOL_VERSION}-20")
            st.write("---")
            home_switch_value4 = st.checkbox("Installation Stage Completed (Yes/No)", value=st.session_state.home_switches[f"{TOOL_VERSION}-homeswitch4"], key=f"{TOOL_VERSION}-homeswitch4")
            st.session_state.home_switches[f"{TOOL_VERSION}-homeswitch4"] = home_switch_value4
            if home_switch_value4:
                st.metric(label=":checkered_flag: Completed", value="Yes", delta="")
            else:
                st.metric(label=":checkered_flag: Completed", value="No", delta="")

    with col2:
        st.subheader(":package: Installation with PVC")
        with st.expander("Activities", expanded=True):
            to_do([(st.write, ":memo: Installation SEQ Signature Completed?")], f"{TOOL_VERSION}-21")
            to_do([(st.write, ":memo: Installation Plan & Report Signature Completed?")], f"{TOOL_VERSION}-22")
            to_do([(st.write, ":memo: Installation with PVC SEQ Signature Completed?")], f"{TOOL_VERSION}-23")
            to_do([(st.write, ":memo: Servat Execution Completed?")], f"{TOOL_VERSION}-24")
            st.write("---")
            home_switch_value5 = st.checkbox("Installation with PVC Stage Completed (Yes/No)", value=st.session_state.home_switches[f"{TOOL_VERSION}-homeswitch5"], key=f"{TOOL_VERSION}-homeswitch5")
            st.session_state.home_switches[f"{TOOL_VERSION}-homeswitch5"] = home_switch_value5
            if home_switch_value5:
                st.metric(label=":checkered_flag: Completed", value="Yes", delta="")
            else:
                st.metric(label=":checkered_flag: Completed", value="No", delta="")

    with col3:
        st.subheader(":wastebasket: Uninstallation")
        with st.expander("Activities", expanded=True):
            to_do([(st.write, ":memo: Installation with PVC SEQ Signature Completed?")], f"{TOOL_VERSION}-25")
            to_do([(st.write, ":memo: Uninstallation Plan & Report Signature Completed?")], f"{TOOL_VERSION}-26")
            to_do([(st.write, ":memo: Uninstallation SEQ Signature Completed?")], f"{TOOL_VERSION}-27")
            to_do([(st.write, ":memo: Servat Execution Completed?")], f"{TOOL_VERSION}-28")
            st.write("---")
            home_switch_value6 = st.checkbox("Uninstallation Status (Yes/No)", value=st.session_state.home_switches[f"{TOOL_VERSION}-homeswitch6"], key=f"{TOOL_VERSION}-homeswitch6")
            st.session_state.home_switches[f"{TOOL_VERSION}-homeswitch6"] = home_switch_value6
            if home_switch_value6:
                st.metric(label=":checkered_flag: Completed", value="Yes", delta="")
            else:
                st.metric(label=":checkered_flag: Completed", value="No", delta="")

    txt = st.text_area(":memo: Observations", value=st.session_state.observations)
    st.session_state.observations = txt

    if home_switch_value4 and home_switch_value5 and home_switch_value6:
        st.success('Overall Status: :trophy: Completed', icon="✅")
        st.session_state.completed_date = st.date_input(":calendar: Execution Completed Date", st.session_state.completed_date, key=completed_date_key)
    elif not home_switch_value4 and not home_switch_value5 and not home_switch_value6:
        st.warning('Overall Status: :hourglass: Not Started', icon="⚠️")
    else:
        st.info('Overall Status: :hourglass_flowing_sand: In Progress', icon="ℹ️")

# Save data on each interaction
data = {
    'todo_states': st.session_state.todo_states,
    'home_switches': st.session_state.home_switches,
    'notes': st.session_state.notes,
    'observations': st.session_state.observations,
    'start_date': st.session_state.start_date.isoformat(),
    'completed_date': st.session_state.completed_date.isoformat()
}
save_data(data)

# Display user_data.json content
with st.expander("View JSON Data"):
    with open(DATA_FILE, "r") as file:
        st.write(DATA_FILE)
        json_data = json.load(file)
        st.json(json_data)
