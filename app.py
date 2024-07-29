#  .\venv\Scripts\activate
import streamlit as st

# Title of the chatbot
st.title("Simple Echo Chatbot")

# Persistent state for chat history
if 'history' not in st.session_state:
    st.session_state['history'] = []

# Ask user for input message
user_input = st.text_input("Say something to the bot:")

# When input is received, respond and update history
if user_input:
    response = f"Thank you for telling me {user_input}"
    st.session_state['history'].append("You: " + user_input)
    st.session_state['history'].append("Bot: " + response)

# Display chat history
for message in st.session_state['history']:
    st.text(message)