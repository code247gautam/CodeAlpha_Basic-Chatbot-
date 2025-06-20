import ttkbootstrap as tb
from ttkbootstrap.constants import *
import tkinter as tk
# --- Reply Logic ---
def get_bot_reply(user_input):
    user_input = user_input.lower().strip()
    if user_input in ["hello", "hi", "hey"]:
        return "Hi there! 😊"
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm doing great, thanks! How can I help you?"
    elif user_input in ["bye", "goodbye", "see you"]:
        return "Goodbye! 👋 Have a nice day!"
    else:
        return "Sorry, I didn't understand that."
# --- Send Handler ---
def handle_send():
    user_text = user_entry.get()
    if user_text.strip() == "":
        return
    chat_display.insert("end", f"You: {user_text}\n")
    bot_reply = get_bot_reply(user_text)
    chat_display.insert("end", f"Bot: {bot_reply}\n\n")
    chat_display.see("end")
    user_entry.delete(0, 'end')
# --- Clear Chat ---
def clear_chat():
    chat_display.delete(1.0, 'end')
# --- Setup Window ---
app = tb.Window(themename="flatly")
app.title("🤖 ChatBot")
app.geometry("700x500")
app.minsize(400, 400)
# --- Configure Grid ---
app.columnconfigure(0, weight=1)
app.rowconfigure(1, weight=1)
# --- Title Label ---
title_label = tb.Label(app, text="Simple Rule-Based ChatBot by gautam", font=("Poppins", 18, "bold"))
title_label.grid(row=0, column=0, pady=10, sticky="n")
# --- Chat Display Area ---
chat_display = tk.Text(app, wrap="word", font=("Poppins", 10))
chat_display.grid(row=1, column=0, padx=20, sticky="nsew")
# --- Entry Frame (bottom) ---
entry_frame = tb.Frame(app)
entry_frame.grid(row=2, column=0, sticky="ew", padx=20, pady=10)
entry_frame.columnconfigure(0, weight=1)
user_entry = tb.Entry(entry_frame, font=("Poppins", 10))
user_entry.grid(row=0, column=0, sticky="ew", padx=(0, 10))
send_button = tb.Button(entry_frame, text="Send", command=handle_send, bootstyle="purple")
send_button.grid(row=0, column=1)
# --- Clear Button ---
clear_btn = tb.Button(app, text="🧹 Clear Chat", command=clear_chat, bootstyle="secondary")
clear_btn.grid(row=3, column=0, pady=10)
app.mainloop()