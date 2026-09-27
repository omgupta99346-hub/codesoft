# CODSOFT AI Internship - Task 1: Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "your name" in user_input:
        return "I'm CODSOFT Chatbot, created as part of AI Internship."
    elif "python" in user_input:
        return "Python is a powerful language for AI!"
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that."

print("CODSOFT Chatbot: Hello! Type 'bye' to exit.")
while True:
    user = input("You: ")
    response = chatbot_response(user)
    print(f"Bot: {response}")
    if "bye" in user.lower():
        break