import streamlit as st
from streamlit_feedback import streamlit_feedback

# Header template
# st.markdown("""
#     <style>
#     body {background-color: #f4f4f4;}
#     .reportview-container .main header {background-color: #007BFF; padding: 10px;}
#     h3 {color: white; text-align: center;}
#     </style>
#     <div style="background-color:#007BFF;padding:10px">
#     <h3>🏠 Home Page</h3>
#     </div>
# """, unsafe_allow_html=True)

# Hide Streamlit footer
st.markdown("""
<style>
.reportview-container .main footer {visibility: hidden;}    
</style>
""", unsafe_allow_html=True)

content = """
# Servat Execution Details 📋

Servat Formal executions of the following,

- **Components** 🧩
- **Provisioners** 🔧
- **SaaS** ☁️

## Prerequisites ✔️

The formal execution will begin once the following prerequisites are completed.

1. **Signatures of OSM** ✍️
2. **Signature of System Requirements** 📊
3. **Signature of Installation Guide** 📚
4. **Signature of Installation Specification** 📜
5. **A Test Iteration SCR with all required task and subtasks are created** ✅

Refer the signature process which is documented below,

"""

st.markdown(content)
with st.expander("Details"):
    st.image("images/Signature_Details.png")
    st.image("images/Signature_Details-1.png")

with st.expander("Feedback"):
    feedback = streamlit_feedback(
    feedback_type="thumbs",
    optional_text_label="[Optional] Please provide an explanation",
)
    st.markdown("**Any suggestions or improvements of the tool?**")
    feedback[0].get("text", "")