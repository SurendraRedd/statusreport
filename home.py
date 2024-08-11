import streamlit as st

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

