# gui.py
import tkinter as tk
from ai import smart_ai

class ChatWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AI Chatbot 🤖")
        self.root.geometry("500x500")

        # Khung hiển thị chat
        self.chat_area = tk.Text(self.root, wrap="word", state="disabled", bg="#f5f5f5")
        self.chat_area.pack(padx=10, pady=10, fill="both", expand=True)

        # Ô nhập
        self.entry = tk.Entry(self.root, font=("Arial", 12))
        self.entry.pack(padx=10, pady=5, fill="x")
        self.entry.bind("<Return>", self.send_message)

        # Nút gửi
        self.send_button = tk.Button(self.root, text="Gửi", command=self.send_message)
        self.send_button.pack(pady=5)

    def send_message(self, event=None):
        user_input = self.entry.get()
        if not user_input.strip():
            return
        self.display_message(f"Bạn: {user_input}")
        self.entry.delete(0, tk.END)

        response = smart_ai(user_input)
        self.display_message(f"AI: {response}")

    def display_message(self, message):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.config(state="disabled")
        self.chat_area.see(tk.END)

    def run(self):
        self.root.mainloop()
