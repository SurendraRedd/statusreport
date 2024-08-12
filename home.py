import streamlit as st
from streamlit_feedback import streamlit_feedback

# Hide Streamlit footer
st.markdown("""
<style>
.reportview-container .main footer {visibility: hidden;}    
</style>
""", unsafe_allow_html=True)

# Content section
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

# Expander for details
with st.expander("Details"):
    st.image("images/Signature_Details.png")
    st.image("images/Signature_Details-1.png")

# Feedback section
st.markdown("---")
st.subheader("User Feedback")

# Collect feedback
feedback = streamlit_feedback(
    feedback_type="thumbs",
    optional_text_label="[Optional] Please provide an explanation",
)

# Display feedback in a table
if feedback:
    st.markdown("### Feedback Summary")
    feedback_table = [
        {"S.No": i + 1, "Feedback": item.get('label', 'N/A'), "Status": item.get('score', 'N/A'), "Comments": item.get('text', 'N/A')}
        for i, item in enumerate(feedback)
    ]

    st.table(feedback_table)