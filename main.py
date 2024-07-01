import streamlit as st  # type: ignore # noqa: E402
import os
import hmac

st.set_page_config(layout="wide", page_title="Formal Execution Status", page_icon=":writing_hand:")

# Get the path to the static folder
#static_folder = os.path.join(os.path.dirname(__file__), 'static')


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

def main():
    """ main function
    Args: NA
    """

    if not check_password():
        st.stop()

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

    #st.page_link("home.py", label="Home", icon="🏠")

    pages = {
        "🏠 Home" :[
            st.Page("home.py",icon=':material/home:',title="Home")
        ],

        "🥇Components" : [
            st.Page("components/cups.py", icon= ':material/print:', title="CUPS"),
            st.Page("components/logging_collection.py", icon= ':material/description:', title="Logging Collection"),
            st.Page("components/metrics_collection.py", icon= ':material/monitoring:',title="Metrics Collection"),
        ],
        "🥈 SaaS" : [
            st.Page("saas/azure_saas.py", icon= ':material/cloud:',title="Azure SaaS"),
            st.Page("saas/aws_saas.py", icon= ':material/cloud:', title="AWS SaaS")
        ],
        "🥉 Provisioner" : [
            st.Page("provisioners/azure_provisioner.py", title="Azure provisioner"),
            st.Page("provisioners/openstack_provisioner.py", title="Openstack provisioner"),
        ]
    }

    pg = st.navigation(pages)
    pg.run()


if __name__ == "__main__":    
    main()