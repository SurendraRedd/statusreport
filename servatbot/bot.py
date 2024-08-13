import streamlit as st
from streamlit_chat import message

# Initialize session state for storing history
if 'history' not in st.session_state:
    st.session_state.history = []

# Title of the app
st.title("🤖 Servat Execution Status Bot")

# Instructions
st.write("Welcome to the Servat Execution Status Bot! 🌟 Feel free to ask me anything about the tool and its execution status. Here are some example questions you can ask:")

# List of supported questions and answers
questions_and_answers = {
    "What is this tool about?": (
        "🔍 **This tool is designed to provide detailed execution statuses** of various components and processes. "
        "It helps you track the progress and status of different operations, ensuring everything runs smoothly. "
        "You can inquire about specific components, prerequisites, and execution details! 📊✨"
    ),
    "What is the version of the tool?": "🔢 The current version of the tool is **1.0.0**. 📦🚀",
    "What platform components will it support?": "🖥️ The tool provides execution details of various platform components such as CUPS, Logging Collection & Metrics Collection. 🌐💻",
    "What provisioners will it support?": "🔧 The tool provides execution details of provisioners including Azure provisioner and Open Stack Provisioner. ⚙️🚀",
    "What SaaS will it support?": "☁️ The tool provides execution details of Azure SaaS, AWS SaaS servat executions and workflows. 🌟📈",
    "Where can I refer to the execution status of each component, provisioner, or SaaS?": (
        "📈 You can check the execution status in the navigation of each version `https://status.streamlit.app/cups-v-1-2-1`. "
        "It provides real-time updates and detailed logs for each component, provisioner, and SaaS. 📊🔍"
    ),
    "What is the process of execution?": (
        "🔄 The execution process consists of several stages: prerequisites, signatures, test executions, and review. "
        "Each stage ensures that the tool's operations are performed effectively and correctly. 🛠️✅"
    ),
    "What is the signature process?": (
        "✍️ The signature process involves reviewing and signing off on key documents and agreements. "
        "For detailed information, refer to the images in the `images` folder: `Signature_Details.png` and `Signature_Details-1.png`. 📜🖊️"
    ),
    "How many are released?": "✅ **Refer to the Home Page** for the release details.",
    "How many are in progress?": "🟡 **Refer to the Home Page** for the in-progress details.",
    "How many are upcoming?": "🔜 **Refer to the Home Page** for the upcoming details.",
    "Whom to contact?": "📧 For any inquiries, please contact the **Servat Team**."
}

# Display the list of questions
st.write("**Example Questions:** 🤔")
for question in questions_and_answers.keys():
    st.write(f"- {question}")

# User input
user_input = st.text_input("User:", "")

# Responses based on user input
if user_input:
    # Add the user input to the history
    st.session_state.history.append({"user": user_input})
    
    response = questions_and_answers.get(
        user_input,
        "🤔 Sorry, I didn't catch that. I can help with information about the tool's execution status. "
        "Feel free to ask one of the example questions or anything related to the tool's operations! 💬🔍"
    )

    # Add the bot response to the history
    st.session_state.history.append({"bot": response})

# Display chat history
for chat in st.session_state.history:
    if "user" in chat:
        message(chat["user"], is_user=True)
    elif "bot" in chat:
        message(chat["bot"])

# Clear chat history button
if st.button("Clear Chat History"):
    st.session_state.history.clear()
