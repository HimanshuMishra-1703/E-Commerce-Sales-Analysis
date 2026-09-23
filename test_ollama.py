from ollama import chat

response = chat(
    model='llama3.2:3b',
    messages=[
        {
            'role': 'user',
            'content': 'Explain what e-commerce analytics is in 2 sentences.'
        }
    ]
)

print(response.message.content)