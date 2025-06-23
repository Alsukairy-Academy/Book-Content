# Using AI to tell a story

import openai
openai.api_key = "your-api-key"

def generate_story(prompt):
    response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
            )
    return response['choices'][0]['message']['content']

story = generate_story("Write a short sci-fi story about an AI Agent who gains emotions.")
print(story)

# Using AI for Personal Growth

def daily_productivity_plan():
    response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": "Create a personalized productivity plan for today."}]
            )
    return response['choices'][0]['message']['content']

print(daily_productivity_plan())
