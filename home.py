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
st.markdown("# Servat Execution Details 📋")
st.markdown(card_style, unsafe_allow_html=True)

# Expander for Released (Expanded by default)
with st.expander("✅ Released", expanded=False):
    cols = st.columns(5)
    with cols[0]:
        st.markdown("""
        <div class="card released">
        <h4>CUPS</h4>
        <p>V1.2.1</p>
        </div>
        """, unsafe_allow_html=True)
    with cols[1]:
        st.markdown("""
        <div class="card released">
        <h4>CUPS</h4>
        <p>V1.3.0</p>
        </div>
        """, unsafe_allow_html=True)
    with cols[2]:
        st.markdown("""
        <div class="card released">
        <h4>Logging Collection</h4>
        <p>V1.1.2</p>
        </div>
        """, unsafe_allow_html=True)
    with cols[3]:
        st.markdown("""
        <div class="card released">
        <h4>Metrics Collection</h4>
        <p>V1.1.0</p>
        </div>
        """, unsafe_allow_html=True)

    with cols[4]:
        st.markdown("""
        <div class="card released">
        <h4>Metrics Collection</h4>
        <p>V1.1.1</p>
        </div>
        """, unsafe_allow_html=True)

# Expander for In-Progress (Expanded by default)
with st.expander("🚧 In-Progress", expanded=True):
    cols = st.columns(1)
    with cols[0]:
        st.markdown("""
        <div class="card inprogress">
        <h4>Logging Collection</h4>
        <p>V1.2.0</p>
        </div>
        """, unsafe_allow_html=True)

# Expander for Upcoming (Expanded by default)
with st.expander("🔜 Upcoming", expanded=False):
    cols = st.columns(1)
    with cols[0]:
        st.markdown("""
        <div class="card upcoming">
        <h4>Open Stack Provisioner</h4>
        <p>V1.0.0</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown(content)
with st.expander("Details"):
    st.image("images/Signature_Details.png")
    st.image("images/Signature_Details-1.png")

# Feedback section
with st.expander("Feedback"):
    feedback = streamlit_feedback(
        feedback_type="thumbs",
        optional_text_label="[Optional] Please provide an explanation",
    )
    st.markdown("**Any suggestions or improvements of the tool?**")
    feedback