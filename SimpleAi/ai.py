# ai.py
import re
import random

def smart_ai(user_input: str) -> str:
    user_input = user_input.lower().strip()

    # Chào hỏi
    if re.search(r"\b(hello|hi|xin chào)\b", user_input):
        return random.choice([
            "Chào bạn 👋",
            "Xin chào! Hôm nay bạn thế nào?",
            "Hello! Rất vui được nói chuyện với bạn."
        ])

    # Hỏi tên
    elif "tên" in user_input:
        return "Mình là AI Python 🤖. Còn bạn tên gì?"

    # Hỏi tuổi
    elif "tuổi" in user_input:
        return "Mình không có tuổi, nhưng mình mới được code ra thôi 😆"

    # Hỏi toán đơn giản
    elif re.search(r"(\d+)\s*[\+\-\*\/]\s*(\d+)", user_input):
        try:
            result = eval(user_input)
            return f"Kết quả là: {result}"
        except:
            return "Mình chưa tính được phép toán này 😅"

    # Tạm biệt
    elif "bye" in user_input or "tạm biệt" in user_input:
        return "Tạm biệt! Hẹn gặp lại bạn 👋"

    # Không hiểu
    else:
        return "Mình chưa hiểu câu hỏi này, bạn có thể hỏi lại cách khác không?"
