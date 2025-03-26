import tkinter as tk
from tkinter import PhotoImage
import requests

# Define the base URL for the Flask API
BASE_URL = "http://127.0.0.1:5000"  # Update this if your Flask API runs on a different host/port

def get_customer_suggestion():
    # Get the customer ID from the user input
    customer_id = user_entry.get()
    if not customer_id.strip():
        update_chat_log("Bot", "Please enter a valid Customer ID.")
        return

    # Make a GET request to the Flask API
    try:
        response = requests.get(f"{BASE_URL}/customer/{customer_id}")
        if response.status_code == 200:
            data = response.json()
            if "suggestion" in data:
                update_chat_log("Bot", f"Suggestion for Customer {customer_id}: {data['suggestion']}")
            else:
                update_chat_log("Bot", f"No suggestion found for Customer {customer_id}.")
        else:
            update_chat_log("Bot", f"Error: {response.json().get('error', 'Unable to fetch data.')}")
    except Exception as e:
        update_chat_log("Bot", f"Error connecting to the server: {e}")

def update_chat_log(sender, message):
    """Update the chat log with messages from the user or bot."""
    chat_log.config(state=tk.NORMAL)
    if sender == "User":
        chat_log.image_create(tk.END, image=user_icon)  # Add user icon
        chat_log.insert(tk.END, f" You: {message}\n", "user")
    elif sender == "Bot":
        chat_log.image_create(tk.END, image=bot_icon)  # Add bot icon
        chat_log.insert(tk.END, f" Bot: {message}\n", "bot")
    chat_log.config(state=tk.DISABLED)
    chat_log.yview(tk.END)  # Scroll to the end

def send_message():
    """Handle user input and send a request to the chatbot."""
    user_input = user_entry.get()
    if not user_input.strip():
        update_chat_log("Bot", "Please enter a valid input.")
        return

    update_chat_log("User", user_input)
    get_customer_suggestion()
    user_entry.delete(0, tk.END)

# Create the main Tkinter window
root = tk.Tk()
root.title("Customer Suggestion Chatbot")

# Create a frame for the chat log
chat_frame = tk.Frame(root)
chat_frame.pack(padx=10, pady=10)

# Add a scrollbar to the chat log
scrollbar = tk.Scrollbar(chat_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create the chat log
chat_log = tk.Text(chat_frame, state=tk.DISABLED, width=80, height=20, bg="light yellow", fg="black", font=("Arial", 12), yscrollcommand=scrollbar.set)
chat_log.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=chat_log.yview)

# Configure tags for user and bot messages
chat_log.tag_config("user", foreground="blue")
chat_log.tag_config("bot", foreground="purple")

# Load and resize user and bot icons
user_icon = PhotoImage(file="./Hackathon2025/user_icon.png").subsample(17, 17)  # Adjust subsample to resize
bot_icon = PhotoImage(file="./Hackathon2025/bot_icon.png").subsample(10, 10)  # Adjust subsample to resize

# Display a welcome message
chat_log.config(state=tk.NORMAL)
chat_log.image_create(tk.END, image=bot_icon)  # Add bot icon
chat_log.insert(tk.END, " Bot: Welcome! Please enter a Customer ID to get suggestions.\n", "bot")
chat_log.config(state=tk.DISABLED)

# Create an entry widget for user input
user_entry = tk.Entry(root, width=80, font=("Arial", 12))
user_entry.pack(padx=10, pady=10)
user_entry.bind("<Return>", lambda event: send_message())

# Create a button to send the message
send_button = tk.Button(root, text="Get Suggestion", command=send_message, font=("Arial", 12), bg="lightblue", fg="black")
send_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()