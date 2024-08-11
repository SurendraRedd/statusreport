import streamlit as st
import extra_streamlit_components as stx


content = """
# Servat Execution Details 📋

This page provides detailed information on the servat executions of the following,

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

Refer the signature process is documented below,

"""

st.markdown(content)
st.image("images/Signature_Details.png")