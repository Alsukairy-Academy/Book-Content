# Step 1: Set Up an AI Chatbot for the Metaverse

# pip install openai web3

# Step 2: Create a Simple AI Store Assistant

import openai
openai.api_key = "your-api-key"

def metaverse_shop_assistant(user_query):
    response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_query}]
            )
    return response['choices'][0]['message']['content']

# Test AI Assistant
query = "What are the latest digital fashion trends in the Metaverse?"
response = metaverse_shop_assistant(query)
print(response)
