import streamlit as st
from streamlit_feedback import streamlit_feedback

# Hide Streamlit footer
st.markdown("""
<style>
.reportview-container .main footer {visibility: hidden;}    
</style>
""", unsafe_allow_html=True)

# Main content
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

Refer to the signature process, which is documented below:
"""

st.markdown(content)
with st.expander("Details"):
    st.image("images/Signature_Details.png")
    st.image("images/Signature_Details-1.png")

# Styling for dark mode compatibility and card colors
card_style = """
<style>
    .card {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 5px;
        padding: 10px;
        color: #f0f0f0; /* Light gray text for visibility in dark mode */
    }
    .card h4 {
        margin-bottom: 5px;
    }
    .card p {
        margin: 0;
    }
    .released .card { background-color: rgba(34, 177, 76, 0.2); } /* Green for Released */
    .inprogress .card { background-color: rgba(255, 165, 0, 0.2); } /* Orange for In-Progress */
    .upcoming .card { background-color: rgba(0, 162, 232, 0.2); } /* Blue for Upcoming */
</style>
"""

st.markdown(card_style, unsafe_allow_html=True)

# Expander for Released (Expanded by default)
with st.expander("✅ Released", expanded=True):
    cols = st.columns(3)
    with cols[0]:
        st.markdown("""
        <div class="card released">
        <h4>Component 1</h4>
        <p>Completed successfully</p>
        </div>
        """, unsafe_allow_html=True)
    with cols[1]:
        st.markdown("""
        <div class="card released">
        <h4>Component 2</h4>
        <p>Completed successfully</p>
        </div>
        """, unsafe_allow_html=True)
    with cols[2]:
        st.markdown("""
        <div class="card released">
        <h4>Component 3</h4>
        <p>Completed successfully</p>
        </div>
        """, unsafe_allow_html=True)

# Expander for In-Progress (Expanded by default)
with st.expander("🚧 In-Progress", expanded=True):
    cols = st.columns(3)
    with cols[0]:
        st.markdown("""
        <div class="card inprogress">
        <h4>Component 4</h4>
        <p>Currently being worked on</p>
        </div>
        """, unsafe_allow_html=True)
    with cols[1]:
        st.markdown("""
        <div class="card inprogress">
        <h4>Component 5</h4>
        <p>Currently being worked on</p>
        </div>
        """, unsafe_allow_html=True)
    with cols[2]:
        st.markdown("""
        <div class="card inprogress">
        <h4>Component 6</h4>
        <p>Currently being worked on</p>
        </div>
        """, unsafe_allow_html=True)

# Expander for Upcoming (Expanded by default)
with st.expander("🔜 Upcoming", expanded=True):
    cols = st.columns(3)
    with cols[0]:
        st.markdown("""
        <div class="card upcoming">
        <h4>Component 7</h4>
        <p>Planned for future release</p>
        </div>
        """, unsafe_allow_html=True)
    with cols[1]:
        st.markdown("""
        <div class="card upcoming">
        <h4>Component 8</h4>
        <p>Planned for future release</p>
        </div>
        """, unsafe_allow_html=True)
    with cols[2]:
        st.markdown("""
        <div class="card upcoming">
        <h4>Component 9</h4>
        <p>Planned for future release</p>
        </div>
        """, unsafe_allow_html=True)

st.write("---")

# Feedback section
with st.expander("Feedback"):
    feedback = streamlit_feedback(
        feedback_type="thumbs",
        optional_text_label="[Optional] Please provide an explanation",
    )
    st.markdown("**Any suggestions or improvements of the tool?**")
    feedback