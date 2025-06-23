# Step 1: Set Up an AI Chatbot for FAQs

import openai
openai.api_key = "your-api-key"

def customer_support_bot(user_query):
    response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_query}]
            )
    return response['choices'][0]['message']['content']

# Test the chatbot
query = "How do I reset my password?"
response = customer_support_bot(query)
print(response)

# Step 2: Automate Customer Onboarding with Email Sequences

import google.generativeai as genai
genai.configure(api_key="your-gemini-api-key")
def generate_onboarding_email(user_name, product_name):
    response = genai.generate_text(
            model="gemini-pro",
            prompt=f"Write a friendly onboarding email for {user_name} using {product_name}."
        )
    return response.text

email = generate_onboarding_email("Sarah", "ProjectFlow")
print(email)

# Step 3: AI-Powered Sales Automation

def sales_email_generator(lead_name, product):
    response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": f"Write a sales email for {lead_name} about {product}."}]
            )
    return response['choices'][0]['message']['content']

email = sales_email_generator("John", "AI-Powered CRM")
print(email)
