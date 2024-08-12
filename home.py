import streamlit as st
from streamlit_feedback import streamlit_feedback

# Hide Streamlit footer
st.markdown("""
<style>
.reportview-container .main footer {visibility: hidden;}    
</style>
""", unsafe_allow_html=True)

# Content header
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
5. **A Test Iteration SCR with all required tasks and subtasks are created** ✅

Refer to the signature process which is documented below:
"""

st.markdown(content)
with st.expander("Details"):
    st.image("images/Signature_Details.png")
    st.image("images/Signature_Details-1.png")

# Feedback section
feedback = streamlit_feedback(
    feedback_type="thumbs",
    optional_text_label="[Optional] Please provide an explanation",
)

# Feedback table with S.No, Feedback, Status, Comments
if feedback:
    st.sidebar.write("Any suggestions or improvements for the tool?")
    st.sidebar.write(feedback)

    st.sidebar.markdown("### Feedback Summary")
    with st.sidebar.expander("View Feedback Details", expanded=True):
        st.write(f"| S.No | Feedback | Status | Comments |")
        st.write(f"| ---- | -------- | ------ | -------- |")

        for i, item in enumerate(feedback):
            feedback_text = item.get('text', 'N/A')
            feedback_status = "Positive" if item['rating'] == 1 else "Negative"
            feedback_comments = item.get('comments', 'N/A')
            st.write(f"| {i + 1} | {feedback_text} | {feedback_status} | {feedback_comments} |")
