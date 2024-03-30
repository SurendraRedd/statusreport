"""
This application contains the code related to the
Azure SaaS Release - Round 2 Status Details dashboard.
"""

import streamlit as st  # noqa: E402
import datetime  # noqa: E402
import streamlit_shadcn_ui as ui  # noqa: E402
import base64
from streamlit_star_rating import st_star_rating  # noqa: E402
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards

st.set_page_config(layout="wide", page_title="Azure SaaS Release - Round 2 Status", page_icon=":writing_hand:")

def load_gif(workflow_name):
    if workflow_name == "System Preparation & Initial Deployment":
        file_ = open("./systemprep_deploy.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        with st.expander("See workflow below"):
            st.markdown(
                f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
                unsafe_allow_html=True,
            )

    if workflow_name == "Update Configuration":
        file_ = open("./update_config.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        with st.expander("See workflow below"):
            st.markdown(
                f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
                unsafe_allow_html=True,
            )
    
    if workflow_name == "Uninstallation":
        file_ = open("./uninstall.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        with st.expander("See workflow below"):
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

        with st.expander("Stages", expanded=True):
            col1, col2, col3, col4, col5, col6 = st.columns(6)
            with col1:
                switch_value1 = ui.switch(default_checked=False, label="InitialSEQ(Yes/No)", key="switch1")
                if switch_value1:
                    st.metric(label=":point_down: Completed", value="Yes", delta="")
                else:
                    st.metric(label=":point_down: Completed", value="No", delta="")
            with col2:
                switch_value2 = ui.switch(default_checked=False, label="InstPlan&Report(Yes/No)", key="switch2")
                if switch_value2:
                    st.metric(label=":point_down: Completed", value="Yes", delta="")
                else:
                    st.metric(label=":point_down: Completed", value="No", delta="")
            with col3:
                switch_value3 = ui.switch(default_checked=False, label="DepPlan&Report(Yes/No)", key="switch3")
                if switch_value3:
                    st.metric(label=":point_down: Completed", value="Yes", delta="")
                else:
                    st.metric(label=":point_down: Completed", value="No", delta="")
            with col4:
                switch_value4 = ui.switch(default_checked=False, label="DeploymntSEQ(Yes/No)", key="switch4")
                if switch_value4:
                    st.metric(label=":point_down: Completed", value="Yes", delta="")
                else:
                    st.metric(label=":point_down: Completed", value="No", delta="")
            with col5:
                switch_value5 = ui.switch(default_checked=False, label="InstQuali(Yes/No)", key="switch5")
                if switch_value5:
                    st.metric(label=":point_down: Completed", value="Yes", delta="")
                else:
                    st.metric(label=":point_down: Completed", value="No", delta="")
            with col6:
                switch_value6 = ui.switch(default_checked=False, label="ServatExecution(Yes/No)", key="switch6")
                if switch_value6:
                    st.metric(label=":point_down: Completed", value="Yes", delta="")
                else:
                    st.metric(label=":point_down: Completed", value="No", delta="")

            txt = st.text_area("Notes", "")
            st.write("---")

            if switch_value1 and switch_value2 and switch_value3 and switch_value4 and switch_value5 and switch_value6:
                st.success('Overall Status: :point_right: Completed', icon="✅")
                st.date_input(":point_right: Execution Start Date", datetime.date(2024, 4, 3))
            elif not switch_value1 and not switch_value2 and not switch_value3 and not switch_value4 and not switch_value5 and not switch_value6:
                st.warning('Overall Status: :point_right: Not Started', icon="⚠️")
            else:
                st.info('Overall Status: :point_right: In Progress', icon="ℹ️")

    if workflow_name == "Update Configuration":
        load_gif(workflow_name)
        st.write("\n")
        st.write("\n")

        with st.expander("Stages", expanded=True):
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                uc_switch_value1 = ui.switch(default_checked=False, label="Deployment SEQ (Yes/No)", key="ucswitch1")
                if uc_switch_value1:
                    st.metric(label=":point_down: Completed", value="Yes", delta="")
                else:
                    st.metric(label=":point_down: Completed", value="No", delta="")
            with col2:
                uc_switch_value2 = ui.switch(default_checked=False, label="Installation Plan & Report (Yes/No)", key="ucswitch2")
                if uc_switch_value2:
                    st.metric(label=":point_down: Completed", value="Yes", delta="")
                else:
                    st.metric(label=":point_down: Completed", value="No", delta="")
            with col3:
                uc_switch_value3 = ui.switch(default_checked=False, label="Update Config SEQ (Yes/No)", key="ucswitch3")
                if uc_switch_value3:
                    st.metric(label=":point_down: Completed", value="Yes", delta="")
                else:
                    st.metric(label=":point_down: Completed", value="No", delta="")
            with col4:
                uc_switch_value4 = ui.switch(default_checked=False, label="Servat Execution (Yes/No)", key="ucswitch4")
                if uc_switch_value4:
                    st.metric(label=":point_down: Completed", value="Yes", delta="")
                else:
                    st.metric(label=":point_down: Completed", value="No", delta="")

            txt = st.text_area("Notes", "")
            st.write("---")

            if uc_switch_value1 and uc_switch_value2 and uc_switch_value3 and uc_switch_value4:
                st.success('Overall Status: :point_right: Completed', icon="✅")
                st.date_input(":point_right: Execution Start Date", datetime.date(2024, 4, 4))
            elif not uc_switch_value1 and not uc_switch_value2 and not uc_switch_value3 and not uc_switch_value4:
                st.warning('Overall Status: :point_right: Not Started', icon="⚠️")
            else:
                st.info('Overall Status: :point_right: In Progress', icon="ℹ️")

    if workflow_name == "Uninstallation":        
        load_gif(workflow_name)
        st.write("\n")
        st.write("\n")

        with st.expander("Stages", expanded=True):
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                un_switch_value1 = ui.switch(default_checked=False, label="Deployment SEQ (Yes/No)", key="unswitch1")
                if un_switch_value1:
                    st.metric(label=":point_down: Completed", value="Yes", delta="")
                else:
                    st.metric(label=":point_down: Completed", value="No", delta="")
            with col2:
                un_switch_value2 = ui.switch(default_checked=False, label="Installation Plan & Report (Yes/No)", key="unswitch2")
                if un_switch_value2:
                    st.metric(label=":point_down: Completed", value="Yes", delta="")
                else:
                    st.metric(label=":point_down: Completed", value="No", delta="")
            with col3:
                un_switch_value3 = ui.switch(default_checked=False, label="Update Config SEQ (Yes/No)", key="unswitch3")
                if un_switch_value3:
                    st.metric(label=":point_down: Completed", value="Yes", delta="")
                else:
                    st.metric(label=":point_down: Completed", value="No", delta="")
            with col4:
                un_switch_value4 = ui.switch(default_checked=False, label="Servat Execution (Yes/No)", key="unswitch4")
                if un_switch_value4:
                    st.metric(label=":point_down: Completed", value="Yes", delta="")
                else:
                    st.metric(label=":point_down: Completed", value="No", delta="")

            txt = st.text_area("Notes", "")
            st.write("---")

            if un_switch_value1 and un_switch_value2 and un_switch_value3 and un_switch_value4:
                st.success('Overall Status: :point_right: Completed', icon="✅")
                st.date_input(":point_right: Execution Start Date", datetime.date(2024, 4, 5))
            elif not un_switch_value1 and not un_switch_value2 and not un_switch_value3 and not un_switch_value4:
                st.warning('Overall Status: :point_right: Not Started', icon="⚠️")
            else:
                st.info('Overall Status: :point_right: In Progress', icon="ℹ️")


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

    st.title(":point_down: Azure SaaS Release - :blue[Round 2 Status Details]")
    st.markdown("---")
    st.write("\n")

    st.subheader("Phases")
    st.write("\n")
    st.date_input(":point_right: Execution Start Date", datetime.date(2024, 4, 2))

    # Create three columns
    col1, col2, col3, col4 = st.columns(4)

    # Status in each column
    with col1:
        st.subheader("System Preparation")
        with st.expander("Details", expanded=True):
            home_switch_value1 = ui.switch(default_checked=False, label="System Preparation (Yes/No)", key="homeswitch1")
            if home_switch_value1:
                st.metric(label=":point_down: Completed", value="Yes", delta="")
            else:
                st.metric(label=":point_down: Completed", value="No", delta="")

    with col2:
        st.subheader("Initial Deployment")
        with st.expander("Details", expanded=True):
            home_switch_value2 = ui.switch(default_checked=False, label="Initial Deployment (Yes/No)", key="homeswitch2")
            if home_switch_value2:
                st.metric(label=":point_down: Completed", value="Yes", delta="")
            else:
                st.metric(label=":point_down: Completed", value="No", delta="")

    with col3:
        st.subheader("Update Configuration")
        with st.expander("Details", expanded=True):
            home_switch_value3 = ui.switch(default_checked=False, label="Update Configuration (Yes/No)", key="homeswitch3")
            if home_switch_value3:
                st.metric(label=":point_down: Completed", value="Yes", delta="")
            else:
                st.metric(label=":point_down: Completed", value="No", delta="")           

    with col4:
        st.subheader("Uninstallation")
        with st.expander("Details", expanded=True):
            home_switch_value4 = ui.switch(default_checked=False, label="Uninstallation (Yes/No)", key="homeswitch4")
            if home_switch_value4:
                st.metric(label=":point_down: Completed", value="Yes", delta="")
            else:
                st.metric(label=":point_down: Completed", value="No", delta="")

    if home_switch_value1 and home_switch_value2 and home_switch_value3 and home_switch_value4:
        st.success('Overall Status: :point_right: Completed', icon="✅")
        st.date_input(":point_right: Execution Completed Date", datetime.date(2024, 4, 5))
    elif not home_switch_value1 and not home_switch_value2 and not home_switch_value3 and not home_switch_value4:
        st.warning('Overall Status: :point_right: Not Started', icon="⚠️")
    else:
        st.info('Overall Status: :point_right: In Progress', icon="ℹ️")

    st.write("\n")
    st.write("\n")
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
    st.title("Workflow: System Preparation & Initial Deployment")
    #st.markdown(html_temp, unsafe_allow_html=True)

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
    #st.markdown(html_temp, unsafe_allow_html=True)
    st.title("Workflow: Update Configuration")

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
    #st.markdown(html_temp, unsafe_allow_html=True)
    st.title("Workflow: Uninstallation")
    hide_footer_style = """
    <style>
    .reportview-container .main footer {visibility: hidden;}    
    """
    st.markdown(hide_footer_style, unsafe_allow_html=True)
    
    create_workflow_stages("Uninstallation")

# Create navigation
with st.sidebar:
    #st.image('./Logo.png', caption='')
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