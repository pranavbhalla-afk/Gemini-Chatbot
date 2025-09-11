import google.generativeai as genai

# Replace this with your actual API key from Makersuite
GOOGLE_API_KEY = "PASTE YOUR API KEY HERE"
genai.configure(api_key=GOOGLE_API_KEY)

# ✅ Use the correct model name for public access
model = genai.GenerativeModel("gemini-1.5-flash")

chat_history = []

def send_message(user_input):
    global chat_history
    print("[DEBUG] Sending input:", user_input)
    chat_history.append({"role": "user", "parts": [user_input]})

    try:
        chat = model.start_chat(history=chat_history)
        response = chat.send_message(user_input)
        chat_history.append({"role": "model", "parts": [response.text]})
        print("[DEBUG] Response received.")
        return response.text
    except Exception as e:
        print("[ERROR]", e)
        return "⚠️ Error occurred while connecting to Gemini API."

def main():
    print("🤖 Gemini Chatbot (with memory)\nType 'exit' to quit.")
    while True:
        print("You: ", end="")
        user_input = input()
        if user_input.lower() == "exit":
            break
        response = send_message(user_input)
        print("Gemini:", response)

if __name__ == "__main__":
    main()

