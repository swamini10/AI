#Develop an elementory chatbot for any suitable interaction application.
import random
import time

responses = {
    "hello": ["Hi", "Hello!", "Hey there!", "Greetings!"],
    "how are you": ["I'm doing great, thank you!", "I'm doing well, how about you?", "I'm good, thanks for asking!"],
    "bye": ["Goodbye!", "See you later!", "Take care!", "Bye!"],
    "ur name": ["I am your friendly chatbot!", "I'm the bot here to chat with you! Call me Chatbot!"]
}

def get_response(user_input):
    """Match the user input with predefined responses."""
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "Sorry, I didn't understand that."

def chat():
    print("Chatbot: Hi! I'm here to chat with you. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a nice day!")
            break
        print("Chatbot is thinking...")
        time.sleep(1)
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
