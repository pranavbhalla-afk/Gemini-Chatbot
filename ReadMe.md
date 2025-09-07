# Gemini API Chatbot

## Project Overview
This project involves the development of a hybrid AI-powered chatbot that integrates **Gemini API** for general conversational queries, **Ollama** for technical and mathematical problem-solving, and **Chainlit** as the interactive front-end interface. The chatbot is designed to handle diverse user queries efficiently, combining the scalability of cloud-based models with the flexibility and speed of locally hosted models. A **keyword-based technique** is implemented to classify queries and route them to the appropriate model, ensuring high accuracy and contextual understanding.

## Features
- Handles **general conversational queries** using Gemini API.
- Processes **technical and mathematical queries** with Ollama.
- Interactive user interface powered by Chainlit.
- **Keyword-based query routing** for accurate model selection.
- Secure API key management using `.env` files.
- Python-based implementation for easy integration and scalability.

## Technology Stack
- **Programming Language:** Python
- **Cloud AI Model:** Gemini API (via Google AI Studio)
- **Local AI Model:** Ollama (locally hosted large language model)
- **Front-end Framework:** Chainlit
- **Libraries Used:** requests, dotenv, json, os

## Installation

1. Clone the repository:

git clone <repository-url>


2. Navigate to the project directory:

cd gemini-chatbot


3. Install dependencies:

pip install -r requirements.txt


4. Set up the .env file and add your Gemini API key:

GEMINI_API_KEY=<your_api_key>


5. Start the Ollama server locally:

ollama serve


6. Run the chatbot using chainlit:

chainlit run main.py


