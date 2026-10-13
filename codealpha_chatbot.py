
import random
import datetime
import math

print("================================")
print("       WELCOME TO CHATBOT")
print("================================")
print("Type 'help' to see commands.")
print("Type 'bye' to exit.")

name = input("\nChatbot: What is your name? ")
print("Chatbot: Hello,", name + "! Nice to meet you.")

while True:
    user = input("\nYou: ").lower().strip()

    if user in ["bye", "exit", "quit"]:
        print("Chatbot: Goodbye,", name + "! Have a nice day.")
        break

    elif user in ["hello", "hi", "hey", "good morning", "good evening"]:
        responses = [
            "Hello! How can I help you?",
            "Hi! Nice to talk to you.",
            "Hey! What would you like to know?"
        ]
        print("Chatbot:", random.choice(responses))

    elif "your name" in user:
        print("Chatbot: I am a Python chatbot.")

    elif "how are you" in user:
        print("Chatbot: I am fine! Thank you for asking.")

    elif "python" in user or "pythin" in user or "pyhton" in user:
        print("Chatbot: Python is a simple and powerful programming language.")

    elif user == "what is ai" or "artificial intelligence" in user:
        print("Chatbot: AI means Artificial Intelligence. It helps machines")
        print("perform tasks that normally require human intelligence.")

    elif "machine learning" in user or user == "what is ml":
        print("Chatbot: Machine Learning is a branch of AI that allows")
        print("computers to learn patterns from data.")

    elif "chatbot" in user:
        print("Chatbot: A chatbot is a program that communicates with users.")

    elif "joke" in user:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why was the computer cold? Because it left its Windows open!",
            "Why did the programmer quit? Because they did not get arrays!"
        ]
        print("Chatbot:", random.choice(jokes))

    elif "motivation" in user or "quote" in user:
        quotes = [
            "Believe in yourself and keep learning!",
            "Small steps every day lead to big results.",
            "Never give up. Every expert was once a beginner."
        ]
        print("Chatbot:", random.choice(quotes))

    elif "study tip" in user or "study tips" in user:
        print("Chatbot: Study in short sessions, take breaks, and practice")
        print("coding every day.")

    elif "date" in user:
        today = datetime.datetime.now().strftime("%d-%m-%Y")
        print("Chatbot: Today's date is", today)

    elif "time" in user:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print("Chatbot: The current time is", current_time)

    elif "calculate" in user or user.startswith("math "):
        try:
            expression = input("Chatbot: Enter a calculation: ")
            expression = expression.strip()
            allowed = set("0123456789+-*/(). %")
            if not expression or not all(c in allowed for c in expression):
                print("Chatbot: Please enter a valid arithmetic expression.")
            else:
                result = eval(expression, {"__builtins__": {}}, {})
                print("Chatbot: Result =", result)
        except Exception:
            print("Chatbot: Invalid calculation. Please try again.")

    elif "happy" in user:
        print("Chatbot: That's wonderful! Keep smiling.")

    elif "sad" in user:
        print("Chatbot: I am sorry you feel sad. Take care of yourself.")

    elif "thank" in user:
        print("Chatbot: You're welcome!")

    elif user == "help":
        print("\nChatbot Commands:")
        print("1. hello")
        print("2. what is python")
        print("3. what is ai")
        print("4. what is machine learning")
        print("5. tell me a joke")
        print("6. motivation")
        print("7. study tips")
        print("8. date")
        print("9. time")
        print("10. calculate")
        print("11. bye")

    else:
        print("Chatbot: Sorry, I don't understand that yet.")
        print("Try typing 'help' to see what I can do.")
