import streamlit as st

# Title of the app
st.title("🤖 Simple Chatbot")

# Instructions
st.write("Welcome to the chatbot! 🗣️ Ask me about the tool and its execution status. Here's an example question you can ask:")

# Default question and answer
default_question = "What is this tool about?"
default_answer = (
    "🔍 **This tool is designed to provide detailed execution statuses** of various components and processes. "
    "It helps track the progress and status of the tool's operations, ensuring everything runs smoothly. "
    "You can ask about specific components, prerequisites, and execution details! 📊"
)

# Display the default question and answer
st.write(f"**Example Question:** {default_question}")
st.write(f"**Bot's Response:** {default_answer}")

# User input
user_input = st.text_input("You:", "")

# Responses based on user input
if user_input:
    if "what is this tool about" in user_input.lower():
        response = default_answer
    else:
        response = (
            "🤔 Sorry, I didn't catch that. I can help with information about the tool's execution status. "
            "Feel free to ask me anything related to the tool's operations or prerequisites! 💬"
        )
    
    # Display the response
    st.write("Bot:", response)