#  .\venv\Scripts\activate
import streamlit as st
import cohere
# co = cohere.Client('lCfJvB4eP3XPXwx5RJ9QkBWGU8xSc4rOHJfftuPm')
# Function to validate the Cohere API key
def validate_cohere_key(api_key):
    try:
        # Temporary client to check the validity
        co_temp = cohere.Client(api_key)
        # Perform a minimal generate call to check if the key works
        test_response = co_temp.generate(
            model='command-r-plus',  # Use the smallest model for test purposes
            prompt='Hello',
            max_tokens=1,
            temperature=0
        )
        return True
    except Exception as e:
        # Log the exception for debugging purposes
        print(f"Failed to validate API key: {e}")
        return False

# Set up page configuration for a better UI experience
st.set_page_config(page_title="AI Chatbot with Cohere", layout="wide", initial_sidebar_state="collapsed")

# Title of the chatbot
st.title("AI Chatbot with Cohere")

# Check API key validity
api_key = st.sidebar.text_input("Enter your Cohere API key:", type="password")
validate_key_button = st.sidebar.button("Validate Key")

if validate_key_button:
    if validate_cohere_key(api_key):
        st.sidebar.success("API Key is valid! You can now use the chatbot.")
        co_client = cohere.Client(api_key)  # Initialize Cohere client
        st.session_state['co_client'] = co_client  # Save client in session state
    else:
        st.sidebar.error("Invalid API key. Please try again.")

# Using containers to better manage layout
chat_container = st.container()
input_container = st.container()

# Persistent state for chat history
if 'history' not in st.session_state:
    st.session_state['history'] = []

if 'co_client' in st.session_state:
    with input_container:
        # User input section
        user_input = st.text_input("Say something to the bot:", key="user_input", placeholder="Type here and hit enter...")
        submit_button = st.button("Send", key="send_button")

    def get_llm_response(history, user_input):
        prompt_text = '\n'.join(history) + '\nBot:'
        response = st.session_state['co_client'].generate(
            model='command-r-plus',  # choose from different model sizes
            prompt=prompt_text,
            max_tokens=150,  
            temperature=0.9  # Higher for more creative responses, lower for more deterministic
        )
        return response.generations[0].text

    # When input is received, respond and update history
    if submit_button and user_input:
        st.session_state['history'].append("You: " + user_input)
        response = get_llm_response(st.session_state['history'], user_input)
        st.session_state['history'].append("Bot: " + response)

    # Display chat history
    with chat_container:
        st.write("### Conversation History")
        # Create dynamic chat bubbles
        for index, message in enumerate(st.session_state.history):
            # Alternate alignment for bot and user
            is_user = message.startswith("You:")
            key = f"message_{index}"
            col1, col2, col3 = st.columns([1, 8, 1]) if is_user else st.columns([1, 8, 1])
            
            with col2:
                if is_user:
                    st.info(message)
                else:
                    st.success(message)
