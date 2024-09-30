# import os
# print('lCfJvB4eP3XPXwx5RJ9QkBWGU8xSc4rOHJfftuPm')

import cohere

# Initialize the Cohere client
co = cohere.Client('lCfJvB4eP3XPXwx5RJ9QkBWGU8xSc4rOHJfftuPm')

# Example function to generate a response from the chatbot
def get_response(prompt):
    response = co.generate(
        model='command-r-plus',  # You can choose from different model sizes
        prompt=prompt,
        max_tokens=50,  # Adjust based on how lengthy you want the response to be
        temperature=0.9  # Higher for more creative responses, lower for more deterministic
    )
    return response.generations[0].text

# Chatbot interaction
user_input = "Hello, what color is the sky?"
chatbot_response = get_response(user_input)
print("Chatbot:", chatbot_response)
