"""
This application contains the code related to the
Azure SaaS Release - Round 2 Status Details dashboard.
"""

import streamlit as st  # type: ignore # noqa: E402
import datetime  # noqa: E402
import streamlit_shadcn_ui as ui  # type: ignore # noqa: E402
import base64
import os
from streamlit_star_rating import st_star_rating  # type: ignore # noqa: E402
from streamlit_option_menu import option_menu # type: ignore
from streamlit_extras.stodo import to_do # type: ignore
import hmac
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(layout="wide", page_title="Azure SaaS Release - Round 2 Status", page_icon=":writing_hand:")

# Get the path to the static folder
static_folder = os.path.join(os.path.dirname(__file__), 'static')


# Todo: Future implementation
# with open('config.yaml') as file:
#     config = yaml.load(file, Loader=SafeLoader)

# authenticator = stauth.Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days'],
#     config['pre-authorized']
# )

# name, authentication_status, username = authenticator.login()

# if st.session_state["authentication_status"]:
#     authenticator.logout('Logout', 'main')
#     st.write(f'Welcome *{st.session_state["name"]}*')
# elif st.session_state["authentication_status"] == False:
#     st.error('Username/password is incorrect')
# elif st.session_state["authentication_status"] == None:
#     st.warning('Please enter your username and password')

def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets[
            "passwords"
        ] and hmac.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the username or password.
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    st.title("Servat Execution Status")
    st.write("\n")
    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False


def load_gif(workflow_name):
    """load gif method

    Args:
        workflow_name (string): Name of the workflow
    """
    file_path = {
        "System Preparation & Initial Deployment": "systemprep_deploy.gif",
        "Update Configuration": "update_config.gif",
        "Uninstallation": "uninstall.gif"
    }.get(workflow_name, None)

    if file_path:
        full_path = os.path.join(static_folder, file_path)
        with open(full_path, "rb") as file_:
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")

        with st.expander("See workflow below"):
            st.markdown(
                f'<img src="data:image/gif;base64,{data_url}" alt="{workflow_name} gif">',
                unsafe_allow_html=True,
            )

# Define function to create stages for each workflow
def create_workflow_stages(workflow_name):
    """workflow stages

    Args:
        workflow_name (string): workflow name
    """
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
                st.date_input(":point_right: Execution Completed Date", datetime.date(2024, 4, 3))
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
                st.date_input(":point_right: Execution Completed Date", datetime.date(2024, 4, 4))
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
                un_switch_value1 = ui.switch(default_checked=False, label="Update Config SEQ (Yes/No)", key="unswitch1")
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
                un_switch_value3 = ui.switch(default_checked=False, label="Uninstallation SEQ (Yes/No)", key="unswitch3")
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
                st.date_input(":point_right: Execution Completed Date", datetime.date(2024, 4, 5))
            elif not un_switch_value1 and not un_switch_value2 and not un_switch_value3 and not un_switch_value4:
                st.warning('Overall Status: :point_right: Not Started', icon="⚠️")
            else:
                st.info('Overall Status: :point_right: In Progress', icon="ℹ️")


# Define the main function for each page
def home():
    """ main function
    Args: NA
    """
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

    st.subheader("Prerequisites")
    to_do([(st.write, "OSM Signature Completion")],"1",)
    to_do([(st.write, "Installation Specification Signature Completion")],"2",)
    st.markdown("---")

    st.date_input(":point_right: Execution Start Date", datetime.date(2024, 4, 2))
    st.subheader("Workflows")
    st.write("\n")

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

    txt = st.text_area("Notes", "")

    if home_switch_value1 and home_switch_value2 and home_switch_value3 and home_switch_value4:
        st.success('Overall Status: :point_right: Completed', icon="✅")
        st.date_input(":point_right: Execution Completed Date", datetime.date(2024, 4, 5))
    elif not home_switch_value1 and not home_switch_value2 and not home_switch_value3 and not home_switch_value4:
        st.warning('Overall Status: :point_right: Not Started', icon="⚠️")
    else:
        st.info('Overall Status: :point_right: In Progress', icon="ℹ️")

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


def main():
    
    if not check_password():
        st.stop()

    with st.sidebar:
        #st.image(static_folder+'/logo.png', caption='')
        st.subheader("Components/SaaS Execution Tool")
        mainmenu = option_menu(None, ["Azure SaaS", "Logging Collection", "CUPS"], 
            icons=['cloud-upload', 'list-task', 'gear'], 
            menu_icon="cast", default_index=2
            )     
    
        
    if mainmenu == "Azure SaaS":
        # Create navigation
        azuresaas_menu = option_menu(None, ["Home", "System Prep + Initial Deployment", "Update Configuration", 'Uninstallation'], 
            icons=['house', 'cloud-upload', "list-task", 'gear'],
            styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "green"},
        }, 
            menu_icon="cast", default_index=0,orientation="horizontal")

        # Display selected page
        if azuresaas_menu == "Home":
            home()
        elif azuresaas_menu == "System Prep + Initial Deployment":
            workflow1()
        elif azuresaas_menu == "Update Configuration":
            workflow2()
        elif azuresaas_menu == "Uninstallation":
            workflow3()


    if mainmenu == "Logging Collection":
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

        st.title(":point_down: Logging Collection Release - :blue[Execution Details]")
        st.markdown("---")

        st.subheader("Prerequisites")
        with st.expander("Details", expanded=True):
            to_do([(st.write, "OSM Signature Completed ?")],"1",)
            to_do([(st.write, "System Requirements Signature Completed ?")],"2",)
            to_do([(st.write, "Installation Guide Signature Completed ?")],"3",)
            to_do([(st.write, "Installation Specification Signature Completed ?")],"4",)

        st.subheader("Workflows")
        st.date_input(":point_right: Execution Start Date", datetime.date(2024, 5, 22))
        st.write("\n")

        tab1, tab2 = st.tabs(["AKS Execution Details", "OCP Execution Details"])

        with tab1:

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
                    home_switch_value1 = ui.switch(default_checked=False, label="Installation (Yes/No)", key="homeswitch1")
                    if home_switch_value1:
                        st.metric(label=":point_down: Completed", value="Yes", delta="")
                    else:
                        st.metric(label=":point_down: Completed", value="No", delta="")

            with col2:
                st.subheader("Installation with PVC")
                with st.expander("Details", expanded=True):
                    to_do([(st.write, "Installation SEQ Signature Completed?")],"9",)
                    to_do([(st.write, "Installation Plan & Report Signature Completed?")],"10",)
                    to_do([(st.write, "Installation with PVC SEQ Signature Completed?")],"11",)
                    to_do([(st.write, "Servat Execution Completed?")],"12",)
                    home_switch_value2 = ui.switch(default_checked=False, label="Installation with PVC (Yes/No)", key="homeswitch2")
                    if home_switch_value2:
                        st.metric(label=":point_down: Completed", value="Yes", delta="")
                    else:
                        st.metric(label=":point_down: Completed", value="No", delta="")

            with col3:
                st.subheader("Uninstallation")
                with st.expander("Details", expanded=True):
                    to_do([(st.write, "Installation with PVC SEQ Signature Completed?")],"13",)
                    to_do([(st.write, "Uninstallation Plan & Report Signature Completed?")],"14",)
                    to_do([(st.write, "Uninstallation SEQ Signature Completed?")],"15",)
                    to_do([(st.write, "Servat Execution Completed?")],"16",)
                    home_switch_value3 = ui.switch(default_checked=False, label="Uninstallation (Yes/No)", key="homeswitch3")
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

        with tab2:

            # Create three columns
            col1, col2, col3 = st.columns(3)

            # Status in each column
            with col1:
                st.subheader("Installation")
                with st.expander("Details", expanded=True):
                    to_do([(st.write, "Initial SEQ Signature Completed?")],"17",)
                    to_do([(st.write, "Installation Plan & Report Signature Completed?")],"18",)
                    to_do([(st.write, "Installation SEQ Signature Completed?")],"19",)
                    to_do([(st.write, "Servat Execution Completed?")],"20",)
                    home_switch_value4 = ui.switch(default_checked=False, label="Installation (Yes/No)", key="homeswitch4")
                    if home_switch_value4:
                        st.metric(label=":point_down: Completed", value="Yes", delta="")
                    else:
                        st.metric(label=":point_down: Completed", value="No", delta="")

            with col2:
                st.subheader("Installation with PVC")
                with st.expander("Details", expanded=True):
                    to_do([(st.write, "Installation SEQ Signature Completed?")],"21",)
                    to_do([(st.write, "Installation Plan & Report Signature Completed?")],"22",)
                    to_do([(st.write, "Installation with PVC SEQ Signature Completed?")],"23",)
                    to_do([(st.write, "Servat Execution Completed?")],"24",)
                    home_switch_value5 = ui.switch(default_checked=False, label="Installation with PVC (Yes/No)", key="homeswitch5")
                    if home_switch_value5:
                        st.metric(label=":point_down: Completed", value="Yes", delta="")
                    else:
                        st.metric(label=":point_down: Completed", value="No", delta="")

            with col3:
                st.subheader("Uninstallation")
                with st.expander("Details", expanded=True):
                    to_do([(st.write, "Installation with PVC SEQ Signature Completed?")],"25",)
                    to_do([(st.write, "Uninstallation Plan & Report Signature Completed?")],"26",)
                    to_do([(st.write, "Uninstallation SEQ Signature Completed?")],"27",)
                    to_do([(st.write, "Servat Execution Completed?")],"28",)
                    home_switch_value6 = ui.switch(default_checked=False, label="Uninstallation (Yes/No)", key="homeswitch6")
                    if home_switch_value6:
                        st.metric(label=":point_down: Completed", value="Yes", delta="")
                    else:
                        st.metric(label=":point_down: Completed", value="No", delta="")           

            txt1 = st.text_area("Observations", "")

            if home_switch_value4 and home_switch_value5 and home_switch_value6:
                st.success('Overall Status: :point_right: Completed', icon="✅")
                st.date_input(":point_right: Execution Completed Date", datetime.date(2024, 23, 5))
            elif not home_switch_value4 and not home_switch_value5 and not home_switch_value6:
                st.warning('Overall Status: :point_right: Not Started', icon="⚠️")
            else:
                st.info('Overall Status: :point_right: In Progress', icon="ℹ️")

    st.write("\n")
    st.write("---")

if __name__ == "__main__":    
    main()
