import streamlit as st

# Title of the app
st.title("🤖 Servat Execution Status Bot")

# Instructions
st.write("Welcome to the Servat Execution Status Bot! 🗣️ Here are some questions you can ask about the tool and its execution status:")

# List of supported questions and answers
questions_and_answers = {
    "What is this tool about?": (
        "🔍 **This tool is designed to provide detailed execution statuses** of various components and processes. "
        "It helps track the progress and status of the tool's operations, ensuring everything runs smoothly. "
        "You can ask about specific components, prerequisites, and execution details! 📊"
    ),
    "What is the version of the tool?": "🔢 The current version of the tool is 1.0.0. 📦",
    "What platform components will it support?": "🖥️ The tool supports various platform components including servers, databases, and storage solutions. 🌐",
    "What provisioners will it support?": "🔧 The tool supports provisioners like Terraform, Ansible, and Puppet for efficient deployment and management. 🚀",
    "What SaaS will it support?": "☁️ The tool supports popular SaaS platforms including AWS, Azure, and Google Cloud. 🌟",
    "Where can I refer to the execution status of each component, provisioner, or SaaS?": (
        "📈 You can refer to the execution status on the dedicated dashboard available at `http://example.com/dashboard`. "
        "It provides real-time updates and detailed logs for each component, provisioner, and SaaS."
    ),
    "What is the process of execution?": (
        "🔄 The execution process involves several stages: planning, deployment, monitoring, and review. "
        "Each stage ensures that the tool's operations are performed efficiently and correctly."
    ),
    "What is the signature process?": (
        "✍️ The signature process includes reviewing and signing off on key documents and agreements. "
        "For details, refer to the images in the `images` folder: Signature_Details.png and Signature_Details-1.png."
    )
}

# Display the list of questions
st.write("**Example Questions:**")
for question in questions_and_answers.keys():
    st.write(f"- {question}")

# User input
user_input = st.text_input("You:", "")

# Responses based on user input
if user_input:
    response = questions_and_answers.get(user_input, 
        "🤔 Sorry, I didn't catch that. I can help with information about the tool's execution status. "
        "Please choose from the example questions or ask something related to the tool's operations! 💬"
    )
    
    # Display the response
    st.write("Bot:", response)