import tkinter as tk
import pymongo

# MONGO DB SETUP
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["PyChat"]
messages_collection = db["messages"]

root = tk.Tk()
root.title("PyThonChatApplication")
root.geometry("800x800")

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

def send_message():
    if entry.get():
        messages_collection.insert_one({"text": entry.get()})
        entry.delete(0, tk.END)


send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)


message_label = tk.Label(root, text="Messages: ", justify="left")
message_label.pack()


def fetch_messages():
    messages = messages_collection.find().sort("_id")
    message_label.config(text="Messages: \n" + "\n".join(f" - {m['text']}" for m in messages))
    root.after(2000, fetch_messages)


#mongodb+srv://admin:123456robin@robinsapi.8jc0x.mongodb.net/?retryWrites=true&w=majority&appName=RobinsAPI

fetch_messages()
root.mainloop()