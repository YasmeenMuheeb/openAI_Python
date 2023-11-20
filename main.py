Copy code
import openai

# Set your API key here (replace 'YOUR_API_KEY' with your actual API key)
api_key = 'YOUR_API_KEY'
openai.api_key = api_key

# Define a function to interact with the ChatGPT model
def chat_with_gpt(prompt, model="text-davinci-003", max_tokens=100):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens
    )
    return response.choices[0].text.strip()

# Example conversation
print("You are having a conversation with ChatGPT. Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        break
    
    # Get GPT-3's response
    gpt_response = chat_with_gpt(user_input)
    print("ChatGPT:", gpt_response)
