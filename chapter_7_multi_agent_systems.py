# Step 2: Set up AI agent functions

import openai
openai.api_key = "your-api-key"

# AI Agent 1: Inquiry Handling
def inquiry_agent(customer_query):
    print(f" Inquiry Received: {customer_query}")
    return customer_query

# AI Agent 2: Generate Response
def response_agent(query):
    response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": query}]
            )
    reply = response["choices"][0]["message"]["content"]
    print(f" AI Response: {reply}")
    return reply

# AI Agent 3: Analyze Customer Feedback
def feedback_agent(feedback):
    sentiment = "Positive" if "thank" in feedback.lower() else "Negative"
    print(f "Feedback Sentiment: {sentiment}")
    return sentiment

# Step 3: Run the multi-agent system

# Customer Inquiry
customer_query = "What are your business hours?"
# AI Agents Working Together
query = inquiry_agent(customer_query)
reply = response_agent(query)
feedback = feedback_agent("Thanks! That was helpful.")
