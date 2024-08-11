import streamlit as st

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
    "What platform components will it support?": "🖥️ The tool supports various platform components such as servers, databases, and storage solutions. 🌐💻",
    "What provisioners will it support?": "🔧 The tool supports several provisioners including Terraform, Ansible, and Puppet for efficient deployment and management. ⚙️🚀",
    "What SaaS will it support?": "☁️ The tool is compatible with popular SaaS platforms like AWS, Azure, and Google Cloud. 🌟📈",
    "Where can I refer to the execution status of each component, provisioner, or SaaS?": (
        "📈 You can check the execution status on our dedicated dashboard at `http://example.com/dashboard`. "
        "It provides real-time updates and detailed logs for each component, provisioner, and SaaS. 📊🔍"
    ),
    "What is the process of execution?": (
        "🔄 The execution process consists of several stages: planning, deployment, monitoring, and review. "
        "Each stage ensures that the tool's operations are performed effectively and correctly. 🛠️✅"
    ),
    "What is the signature process?": (
        "✍️ The signature process involves reviewing and signing off on key documents and agreements. "
        "For detailed information, refer to the images in the `images` folder: `Signature_Details.png` and `Signature_Details-1.png`. 📜🖊️"
    )
}

# Display the list of questions
st.write("**Example Questions:** 🤔")
for question in questions_and_answers.keys():
    st.write(f"- {question}")

# User input
user_input = st.text_input("You:", "")

# Responses based on user input
if user_input:
    response = questions_and_answers.get(user_input, 
        "🤔 Sorry, I didn't catch that. I can help with information about the tool's execution status. "
        "Feel free to ask one of the example questions or anything related to the tool's operations! 💬🔍"
    )
    
    # Display the response
    st.write("Bot:", response)