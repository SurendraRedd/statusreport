import streamlit as st
import json
import os
from streamlit_feedback import streamlit_feedback

# File path for persistent storage
FEEDBACK_FILE = "feedback_data.json"

# Function to load feedback data from file
def load_feedback():
    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "r") as file:
            return json.load(file)
    return []

# Function to save feedback data to file
def save_feedback(data):
    with open(FEEDBACK_FILE, "w") as file:
        json.dump(data, file)

# Load feedback data
feedback_data = load_feedback()

# Content Display
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
5. **A Test Iteration SCR with all required tasks and subtasks created** ✅

Refer to the signature process which is documented below,

"""
st.markdown(content)
with st.expander("Details"):
    st.image("images/Signature_Details.png")
    st.image("images/Signature_Details-1.png")

st.write("---")

# Feedback Section
with st.expander("Feedback"):
    feedback = streamlit_feedback(
        feedback_type="thumbs",
        optional_text_label="[Optional] Please provide an explanation",
    )
    
    if feedback:
        new_feedback = {
            "S.No": len(feedback_data) + 1,
            "Feedback": feedback[0].get("text", ""),
            "Status": "Submitted",
            "Comments": feedback[0].get("optional_text", "")
        }
        feedback_data.append(new_feedback)
        save_feedback(feedback_data)
    
    # Display Feedback Table
    st.write("### Feedback Received")
    if feedback_data:
        st.table(feedback_data)
    else:
        st.write("No feedback received yet.")
