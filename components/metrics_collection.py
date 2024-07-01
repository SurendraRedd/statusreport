import streamlit as st
from streamlit_extras.stodo import to_do
import datetime
import streamlit_shadcn_ui as ui

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
#st.markdown(html_temp, unsafe_allow_html=True)    

hide_footer_style = """
<style>
.reportview-container .main footer {visibility: hidden;}    
"""
st.markdown(hide_footer_style, unsafe_allow_html=True)

st.title(":point_down: Metrics Collection - :blue[Execution Status]")
st.markdown("---")

st.subheader("Prerequisites")
with st.expander("Details", expanded=True):
    to_do([(st.write, "OSM Signature Completed ?")],"1",)
    to_do([(st.write, "System Requirements Signature Completed ?")],"2",)
    to_do([(st.write, "Installation Guide Signature Completed ?")],"3",)
    to_do([(st.write, "Installation Specification Signature Completed ?")],"4",)

st.subheader("Workflows")
st.date_input(":point_right: Execution Start Date", datetime.date(2024, 7, 1))
st.write("\n")

st.subheader("AKS Execution Details")

# Create three columns
col1, col2, col3 = st.columns(3)

# Status in each column
with col1:
    st.subheader("Installation")
    with st.expander("Details", expanded=True):
        to_do([(st.write, "Initial SEQ Signature Completed?")],"5",)
        to_do([(st.write, "Installation Plan & Report Signature Completed?")],"6",)
        to_do([(st.write, "Installation SEQ Signature Completed?")],"7",)
        to_do([(st.write, "Servat Execution Completed?")],"8",)
        home_switch_value1 = ui.switch(default_checked=False, label="Installation Stage Completed(Yes/No)", key="homeswitch1")
        if home_switch_value1:
            st.metric(label=":point_down: Completed", value="Yes", delta="")
        else:
            st.metric(label=":point_down: Completed", value="No", delta="")

with col2:
    st.subheader("Installation with PVC")
    with st.expander("Details", expanded=True):
        to_do([(st.write, "Installation Plan & Report Signature Completed?")],"10",)
        to_do([(st.write, "Installation with PVC SEQ Signature Completed?")],"9",)
        to_do([(st.write, "Servat Execution Completed?")],"11",)
        home_switch_value2 = ui.switch(default_checked=False, label="Installation with PVC Stage Completed (Yes/No)", key="homeswitch2")
        if home_switch_value2:
            st.metric(label=":point_down: Completed", value="Yes", delta="")
        else:
            st.metric(label=":point_down: Completed", value="No", delta="")

with col3:
    st.subheader("Uninstallation")
    with st.expander("Details", expanded=True):
        to_do([(st.write, "Uninstallation Plan & Report Signature Completed?")],"14",)
        to_do([(st.write, "Uninstallation SEQ Signature Completed?")],"15",)
        to_do([(st.write, "Servat Execution Completed?")],"16",)
        home_switch_value3 = ui.switch(default_checked=False, label="Uninstallation Stage Completed (Yes/No)", key="homeswitch3")
        if home_switch_value3:
            st.metric(label=":point_down: Completed", value="Yes", delta="")
        else:
            st.metric(label=":point_down: Completed", value="No", delta="")           

txt = st.text_area("Notes", "")

if home_switch_value1 and home_switch_value2 and home_switch_value3:
    st.success('Overall Status: :point_right: Completed', icon="✅")
    st.date_input(":point_right: Execution Completed Date", datetime.date(2024, 23, 5))
elif not home_switch_value1 and not home_switch_value2 and not home_switch_value3:
    st.warning('Overall Status: :point_right: Not Started', icon="⚠️")
else:
    st.info('Overall Status: :point_right: In Progress', icon="ℹ️")

st.date_input(":point_right: Execution Completion Date", datetime.date(2024, 7, 1))
st.write("\n")