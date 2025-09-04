# chat.py
from ai import smart_ai

def start_chat():
    print("🤖 Smart AI Chatbot (gõ 'quit' để thoát)")
    while True:
        user_input = input("Bạn: ")
        if user_input.lower() in ["quit", "exit"]:
            print("AI: Tạm biệt 👋")
            break
        response = smart_ai(user_input)
        print("AI:", response)
