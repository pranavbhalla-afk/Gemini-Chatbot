import chainlit as cl
import requests

OLLAMA_URL = "PASTE YOUR API KEY HERE"

@cl.on_message
async def on_message(message: cl.Message):
    # Send the user message to Ollama
    response = requests.post(OLLAMA_URL, json={
        "model": "gemini",
        "prompt": message.content,
        "stream": False
    })

    reply = response.json().get("response", "No reply received.")
    
    # Show reply in the Chainlit UI
    await cl.Message(content=reply).send()
