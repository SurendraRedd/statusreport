import streamlit as st
from streamlit_feedback import streamlit_feedback

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
5. **A Test Iteration SCR with all required tasks and subtasks created** ✅

Refer to the signature process, which is documented below:
"""

st.markdown(content)
with st.expander("Details"):
    st.image("images/Signature_Details.png")
    st.image("images/Signature_Details-1.png")

# Expander for Released
with st.expander("Released"):
    cols = st.columns(3)
    with cols[0]:
        st.markdown("""
        <div style="background-color:#e7f3e7;padding:10px;border-radius:5px;">
        <h4>Component 1</h4>
        <p>Description of Component 1</p>
        </div>
        """, unsafe_allow_html=True)
    with cols[1]:
        st.markdown("""
        <div style="background-color:#e7f3e7;padding:10px;border-radius:5px;">
        <h4>Component 2</h4>
        <p>Description of Component 2</p>
        </div>
        """, unsafe_allow_html=True)
    with cols[2]:
        st.markdown("""
        <div style="background-color:#e7f3e7;padding:10px;border-radius:5px;">
        <h4>Component 3</h4>
        <p>Description of Component 3</p>
        </div>
        """, unsafe_allow_html=True)

# Expander for In-Progress
with st.expander("In-Progress"):
    cols = st.columns(3)
    with cols[0]:
        st.markdown("""
        <div style="background-color:#fff3e6;padding:10px;border-radius:5px;">
        <h4>Component 4</h4>
        <p>Description of Component 4</p>
        </div>
        """, unsafe_allow_html=True)
    with cols[1]:
        st.markdown("""
        <div style="background-color:#fff3e6;padding:10px;border-radius:5px;">
        <h4>Component 5</h4>
        <p>Description of Component 5</p>
        </div>
        """, unsafe_allow_html=True)
    with cols[2]:
        st.markdown("""
        <div style="background-color:#fff3e6;padding:10px;border-radius:5px;">
        <h4>Component 6</h4>
        <p>Description of Component 6</p>
        </div>
        """, unsafe_allow_html=True)

# Expander for Upcoming
with st.expander("Upcoming"):
    cols = st.columns(3)
    with cols[0]:
        st.markdown("""
        <div style="background-color:#e6e6ff;padding:10px;border-radius:5px;">
        <h4>Component 7</h4>
        <p>Description of Component 7</p>
        </div>
        """, unsafe_allow_html=True)
    with cols[1]:
        st.markdown("""
        <div style="background-color:#e6e6ff;padding:10px;border-radius:5px;">
        <h4>Component 8</h4>
        <p>Description of Component 8</p>
        </div>
        """, unsafe_allow_html=True)
    with cols[2]:
        st.markdown("""
        <div style="background-color:#e6e6ff;padding:10px;border-radius:5px;">
        <h4>Component 9</h4>
        <p>Description of Component 9</p>
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