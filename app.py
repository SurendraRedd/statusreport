"""
This application contains the code related to the
Azure SaaS Release - Round 2 Status Details dashboard.
"""

__author__ = 'Surendra Reddy'
__version__ = '1.0'
__maintainer__ = 'Surendra Reddy'
__email__ = 'tbd'
__status__ = 'Prototype'

import streamlit as st  # noqa: E402
import datetime  # noqa: E402
import streamlit_shadcn_ui as ui  # noqa: E402
import base64
from streamlit_star_rating import st_star_rating  # noqa: E402
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards


print('# ' + '=' * 78)
print('Author: ' + __author__)
print('Version: ' + __version__)
print('Maintainer: ' + __maintainer__)
print('Email: ' + __email__)
print('Status: ' + __status__)
print('# ' + '=' * 78)

st.set_page_config(layout="wide", page_title="Azure SaaS Release - Round 2 Status Details", page_icon="🎄")

def load_gif(workflow_name):
    if workflow_name == "System Preparation & Initial Deployment":
        file_ = open("./systemprep_deploy.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
            unsafe_allow_html=True,
        )

    if workflow_name == "Update Configuration":
        file_ = open("./update_config.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
            unsafe_allow_html=True,
        )
    
    if workflow_name == "Uninstallation":
        file_ = open("./uninstall.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
            unsafe_allow_html=True,
        )

# Define function to create stages for each workflow
def create_workflow_stages(workflow_name):
    #st.subheader(workflow_name)
    st.write("\n")
    if workflow_name == "System Preparation & Initial Deployment":
        load_gif(workflow_name)
        st.write("\n")
        st.write("\n")

        with st.expander("Status", expanded=True):
            col1, col2, col3, col4, col5, col6 = st.columns(6)
            with col1:
                switch_value1 = ui.switch(default_checked=False, label="Initial SEQ", key="switch1")
                st.write("Completed:", switch_value1)
            with col2:
                switch_value2 = ui.switch(default_checked=False, label="Installation Plan & Report", key="switch2")
                st.write("Completed:", switch_value2)
            with col3:
                switch_value3 = ui.switch(default_checked=False, label="Installation Plan & Report", key="switch3")
                st.write("Completed:", switch_value3)
            with col4:
                switch_value4 = ui.switch(default_checked=False, label="Deployment SEQ", key="switch4")
                st.write("Completed:", switch_value4)
            with col5:
                switch_value5 = ui.switch(default_checked=False, label="Installation Qualification", key="switch5")
                st.write("Completed:", switch_value5)
            with col6:
                switch_value6 = ui.switch(default_checked=False, label="Servat Execution", key="switch6")
                st.write("Completed:", switch_value6)

            st.write("---")

            if switch_value1 and switch_value2 and switch_value3 and switch_value4 and switch_value5 and switch_value6:
                st.success('Overall Status: :point_right: Completed')
            elif not switch_value1 and not switch_value2 and not switch_value3 and not switch_value4 and not switch_value5 and not switch_value6:
                st.warning('Overall Status: :point_right: Not Started')
            else:
                st.info('Overall Status: :point_right: In Progress')

    if workflow_name == "Update Configuration":
        load_gif(workflow_name)
        st.write("\n")
        st.write("\n")

        with st.expander("Status", expanded=True):
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                uc_switch_value1 = ui.switch(default_checked=False, label="Deployment SEQ", key="ucswitch1")
                st.write("Completed:", uc_switch_value1)
            with col2:
                uc_switch_value2 = ui.switch(default_checked=False, label="Installation Plan & Report", key="ucswitch2")
                st.write("Completed:", uc_switch_value2)
            with col3:
                uc_switch_value3 = ui.switch(default_checked=False, label="Update Config SEQ", key="ucswitch3")
                st.write("Completed:", uc_switch_value3)
            with col4:
                uc_switch_value4 = ui.switch(default_checked=False, label="Servat Execution", key="ucswitch4")
                st.write("Completed:", uc_switch_value4)

            st.write("---")

            if uc_switch_value1 and uc_switch_value2 and uc_switch_value3 and uc_switch_value4:
                st.success('Overall Status: :point_right: Completed')
            elif not uc_switch_value1 and not uc_switch_value2 and not uc_switch_value3 and not uc_switch_value4:
                st.warning('Overall Status: :point_right: Not Started')
            else:
                st.info('Overall Status: :point_right: In Progress')

    if workflow_name == "Uninstallation":        
        load_gif(workflow_name)
        st.write("\n")
        st.write("\n")

        with st.expander("Status", expanded=True):
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                un_switch_value1 = ui.switch(default_checked=False, label="Deployment SEQ", key="unswitch1")
                st.write("Completed:", un_switch_value1)
            with col2:
                un_switch_value2 = ui.switch(default_checked=False, label="Installation Plan & Report", key="unswitch2")
                st.write("Completed:", un_switch_value2)
            with col3:
                un_switch_value3 = ui.switch(default_checked=False, label="Update Config SEQ", key="unswitch3")
                st.write("Completed:", un_switch_value3)
            with col4:
                un_switch_value4 = ui.switch(default_checked=False, label="Servat Execution", key="unswitch4")
                st.write("Completed:", un_switch_value4)

            st.write("---")

            if un_switch_value1 and un_switch_value2 and un_switch_value3 and un_switch_value4:
                st.success('Overall Status: :point_right: Completed')
            elif not un_switch_value1 and not un_switch_value2 and not un_switch_value3 and not un_switch_value4:
                st.warning('Overall Status: :point_right: Not Started')
            else:
                st.info('Overall Status: :point_right: In Progress')


# Define the main function for each page
def home():
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

    st.title(":point_down: Azure SaaS Release - Round 2 Status Details")
    st.markdown("---")
    st.write("\n")
    st.write("\n")
    st.write("\n")

    st.subheader("Phases")
    st.date_input(":point_down: Execution Start Date", datetime.date(2024, 4, 2))

    # Create three columns
    col1, col2, col3, col4 = st.columns(4)

    # Status in each column
    with col1:
        st.subheader("System Preparation")
        with st.expander("Details", expanded=True):
            home_switch_value1 = ui.switch(default_checked=False, label="System Preparation (Yes/No)", key="homeswitch1")
            if home_switch_value1:
                st.metric(label=":point_down: Status", value="Yes", delta="")
            else:
                st.metric(label=":point_down: Status", value="No", delta="")

    with col2:
        st.subheader("Initial Deployment")
        with st.expander("Details", expanded=True):
            home_switch_value2 = ui.switch(default_checked=False, label="Initial Deployment (Yes/No)", key="homeswitch2")
            if home_switch_value2:
                st.metric(label=":point_down: Status", value="Yes", delta="")
            else:
                st.metric(label=":point_down: Status", value="No", delta="")

    with col3:
        st.subheader("Update Configuration")
        with st.expander("Details", expanded=True):
            home_switch_value3 = ui.switch(default_checked=False, label="Update Configuration (Yes/No)", key="homeswitch3")
            if home_switch_value3:
                st.metric(label=":point_down: Status", value="Yes", delta="")
            else:
                st.metric(label=":point_down: Status", value="No", delta="")           

    with col4:
        st.subheader("Uninstallation")
        with st.expander("Details", expanded=True):
            home_switch_value4 = ui.switch(default_checked=False, label="Uninstallation (Yes/No)", key="homeswitch4")
            if home_switch_value4:
                st.metric(label=":point_down: Status", value="Yes", delta="")
            else:
                st.metric(label=":point_down: Status", value="No", delta="")

    if home_switch_value1 and home_switch_value2 and home_switch_value3 and home_switch_value4:
        #st.markdown("Overall Status: :point_right: Completed")
        st.success('Overall Status: :point_right: Completed')
        st.balloons()
    elif not home_switch_value1 and not home_switch_value2 and not home_switch_value3 and not home_switch_value4:
        #st.markdown("Overall Status: :point_right: Not Started")
        st.warning('Overall Status: :point_right: Not Started')
    else:
        #st.markdown("Overall Status: :point_right: In Progress")
        st.info('Overall Status: :point_right: In Progress')

    st.write("\n")
    st.write("\n")
    st.write("---")

    st_star_rating(label = "Please rate you experience", maxValue = 5, defaultValue = 4, key = "rating", emoticons = True )

def workflow1():
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
        <div style="background-color:tomato;padding:10px">
        <h3 style="color:white;text-align:center;"> System Preparation and Initial Deployment</h3>
        </div>
        </body>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    hide_footer_style = """
    <style>
    .reportview-container .main footer {visibility: hidden;}    
    """
    st.markdown(hide_footer_style, unsafe_allow_html=True)

    create_workflow_stages("System Preparation & Initial Deployment")    

def workflow2():
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
        <div style="background-color:tomato;padding:10px">
        <h3 style="color:white;text-align:center;"> Update Configuration</h3>
        </div>
        </body>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    hide_footer_style = """
    <style>
    .reportview-container .main footer {visibility: hidden;}    
    """
    st.markdown(hide_footer_style, unsafe_allow_html=True)

    create_workflow_stages("Update Configuration")

def workflow3():
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
        <div style="background-color:tomato;padding:10px">
        <h3 style="color:white;text-align:center;"> Uninstallation</h3>
        </div>
        </body>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    hide_footer_style = """
    <style>
    .reportview-container .main footer {visibility: hidden;}    
    """
    st.markdown(hide_footer_style, unsafe_allow_html=True)
    
    create_workflow_stages("Uninstallation")

# Create navigation
#navigation = st.sidebar.radio("Navigation", ["Home", "System Prep + Initial Deployment", "Update Configuration", "Uninstallation"])
with st.sidebar:
    selected2 = option_menu(None, ["Home", "System Prep + Initial Deployment", "Update Configuration", 'Uninstallation'], 
        icons=['house', 'cloud-upload', "list-task", 'gear'], 
        menu_icon="cast", default_index=0)

# Display selected page
if selected2 == "Home":
    home()
elif selected2 == "System Prep + Initial Deployment":
    workflow1()
elif selected2 == "Update Configuration":
    workflow2()
elif selected2 == "Uninstallation":
    workflow3()