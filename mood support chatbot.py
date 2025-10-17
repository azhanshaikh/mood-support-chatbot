import tkinter as tk
from tkinter import scrolledtext

def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return

    chat_area.insert(tk.END, "You: " + user_input + "\n")
    entry.delete(0, tk.END)

    bot_reply = respond(user_input.lower())
    chat_area.insert(tk.END, "Bot: " + bot_reply + "\n\n")
    chat_area.yview(tk.END)

def respond(user_input):
    if any(word in user_input for word in ["sad", "depressed", "upset", "low"]):
        return "I'm sorry you're feeling that way. Try deep breathing or a short walk. Want a motivational quote?"
    elif any(word in user_input for word in ["stress", "anxiety", "tension", "overthinking"]):
        return "Stress is tough. Try writing your thoughts or drinking some water. Need relaxation tips?"
    elif any(word in user_input for word in ["happy", "good", "excited", "fine"]):
        return "That's great to hear! Keep doing what makes you feel good. Want a positivity tip?"
    elif "quote" in user_input:
        return "Here's one: 'Tough times never last, but tough people do.' Want another?"
    elif "tips" in user_input or "help" in user_input:
        return "You can try meditation, music, journaling, or a short nap. Which one interests you?"
    elif "bye" in user_input:
        return "Take care of yourself! I’m always here to talk 🌿"
    else:
        return "Talk to me about how you're feeling – happy, sad, anxious, anything. I'm here to listen."
    
    # 🔹 Greetings
    if any(word in user_input for word in ["hello", "hi", "hey", "good morning", "good evening"]):
        return "Hello! How are you feeling today? 😊"

    elif any(word in user_input for word in ["how are you", "how r u", "what's up", "whats up"]):
        return "I'm just a chatbot, but I'm here to help you! How about you? How are you feeling?"

    # 🔹 Asking user preference / goals
    elif any(word in user_input for word in ["what can you do", "what do you do", "what you can do"]):
        return (
            "I can chat with you, suggest mood boosters, give motivational quotes, "
            "or provide relaxation tips. What would you like me to do today?"
        )

    # 🔹 User states mood
    elif any(word in user_input for word in ["sad", "depressed", "upset", "low"]):
        return "I'm sorry to hear that. Would you like a motivational quote, a calming activity, or just to talk?"

    elif any(word in user_input for word in ["happy", "good", "excited", "fine"]):
        return "That's great! Want me to share a positivity tip or a fun suggestion?"

    # 🔹 Stress / Anxiety
    elif any(word in user_input for word in ["stress", "anxiety", "tense", "overthinking"]):
        return "Stress can be tough. Want quick relaxation exercises or a motivational quote?"

    # 🔹 Asking about user wants
    elif any(word in user_input for word in ["i want", "can you", "please"]):
        return "Sure! Tell me exactly what you want, and I'll do my best to help."

    # 🔹 Gratitude / Thanks
    elif any(word in user_input for word in ["thank", "thanks", "appreciate"]):
        return "You're welcome! 😊 I'm always here if you want to chat."

    # 🔹 Bye / Exit
    elif any(word in user_input for word in ["bye", "exit", "see you"]):
        return "Take care! Talk to you soon 🌿"

    # 🔹 Default fallback
    else:
        return (
            "I’m here to chat about your mood, motivation, or anything you want. "
            "Try asking me about quotes, stress relief, or just say hi!"
        )


# GUI
root = tk.Tk()
root.title("Mood Support Chatbot")
root.geometry("430x500")

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
chat_area.pack(pady=10)

entry = tk.Entry(root, width=35)
entry.pack(side=tk.LEFT, padx=10, pady=10)

send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack(side=tk.LEFT, pady=10)

root.mainloop()
