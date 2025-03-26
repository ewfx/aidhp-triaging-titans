import tkinter as tk
from tkinter import PhotoImage
import requests
import uuid

user_id = str(uuid.uuid4())

def send_message():
    user_input = user_entry.get()
    response = requests.post('http://127.0.0.1:5000/chat', json={'user_id': user_id, 'text': user_input})
    try:
        result = response.json()
    except requests.exceptions.JSONDecodeError:
        bot_response = "Error: Unable to get a valid response from the server."
    else:
        responses = result.get('responses', ["Sorry, I don't understand that."])
        bot_response = ', '.join(responses)
    
    chat_log.config(state=tk.NORMAL)
    chat_log.image_create(tk.END, image=user_icon)
    chat_log.insert(tk.END, " You: " + user_input + "\n", "user")
    chat_log.image_create(tk.END, image=bot_icon)
    chat_log.insert(tk.END, " Bot: " + bot_response + "\n", "bot")
    chat_log.config(state=tk.DISABLED)
    chat_log.yview(tk.END)  # Scroll to the end
    user_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Chatbot")

chat_frame = tk.Frame(root)
chat_frame.pack(padx=10, pady=10)

scrollbar = tk.Scrollbar(chat_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

chat_log = tk.Text(chat_frame, state=tk.DISABLED, width=80, height=20, bg="light yellow", fg="black", font=("Arial", 12), yscrollcommand=scrollbar.set)
chat_log.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=chat_log.yview)

chat_log.tag_config("user", foreground="blue")
chat_log.tag_config("bot", foreground="purple")

# Load and resize images
user_icon = PhotoImage(file="./Hackathon2025/user_icon.png").subsample(17, 17)
bot_icon = PhotoImage(file="./Hackathon2025/bot_icon.png").subsample(10, 10)

# Display welcome message
chat_log.config(state=tk.NORMAL)
chat_log.image_create(tk.END, image=bot_icon)
chat_log.insert(tk.END, " Bot: Welcome! How can I assist you today?\n", "bot")
chat_log.config(state=tk.DISABLED)

user_entry = tk.Entry(root, width=80, font=("Arial", 12))
user_entry.pack(padx=10, pady=10)
user_entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 12))
send_button.pack(pady=10)

root.mainloop()