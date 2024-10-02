import streamlit as st  # type: ignore # noqa: E402
import os
import hmac

# Page configuration
st.set_page_config(
    layout="wide", 
    page_title="Formal Execution Status", 
    page_icon="✍️"
)

def check_password():
    """Returns `True` if the user has entered a correct password."""
    
    def login_form():
        """Form with widgets to collect user information."""
        with st.form("Credentials"):
            st.text_input("👤 Username", key="username")
            st.text_input("🔑 Password", type="password", key="password")
            st.form_submit_button("🔓 Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets["passwords"] and hmac.compare_digest(
            st.session_state["password"], st.secrets.passwords[st.session_state["username"]]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the username or password.
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if st.session_state.get("password_correct", False):
        return True

    st.title("🔒 Servat Execution Status Tool")
    st.write("\n")
    login_form()

    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False

def main():
    """Main function to run the application."""
        
    if not check_password():
        st.stop()       

    # Sidebar content
    st.sidebar.title("📈 Execution Tool ")
    st.sidebar.markdown("**Version:** `1.0.0`")
    st.sidebar.markdown("**Developed by:** Servat Team")    

    # Navigation pages
    pages = {
        "🏠 Home" :[
            st.Page("home.py", icon="🏠", title="Home")
        ],
        "🥇 Components" : [
            st.Page("components/cups-v-1-2-1.py", icon="🖨️", title="CUPS-V1.2.1"),
            st.Page("components/cups-v-1-3-0.py", icon="🖨️", title="CUPS-V1.3.0"),
            st.Page("components/cups-v-1-4-0.py", icon="🖨️", title="CUPS-V1.4.0"),
            st.Page("components/logcollection-v-1-1-2.py", icon="📝", title="LC-V1.1.2"),
            st.Page("components/logcollection-v-1-2-0.py", icon="📝", title="LC-V1.2.0"),
            st.Page("components/metrics_collection.py", icon="📊", title="Metrics Collection"),
        ],
        "🥈 SaaS" : [
            st.Page("saas/azure_saas.py", icon="☁️", title="Azure SaaS"),
            st.Page("saas/aws_saas.py", icon="☁️", title="AWS SaaS")
        ],
        "🥉 Provisioner" : [
            st.Page("provisioners/azure_provisioner.py", icon="🔧", title="Azure Provisioner"),
            st.Page("provisioners/openstack_provisioner.py", icon="🔧", title="OpenStack Provisioner"),
        ],
        "🤖 Support" : [
            st.Page("servatbot/bot.py", icon="🤖", title="Bot"),
        ]
    }

    # Navigation logic
    pg = st.navigation(pages)
    
    pg.run()

if __name__ == "__main__":    
    main()
