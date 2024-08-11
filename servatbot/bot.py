import streamlit as st

# Title of the app
st.title("Simple Chatbot")

# Instructions
st.write("Ask me about the tool and its executions status.")

# User input
user_input = st.text_input("You:", "")

# Responses based on user input
if user_input:
    if "what is this tool about" in user_input.lower():
        response = "It is about the executions status of the tool."
    else:
        response = "Sorry, I don't understand that question. Please ask about the tool's execution status."
    
    # Display the response
    st.write("Bot:", response)
