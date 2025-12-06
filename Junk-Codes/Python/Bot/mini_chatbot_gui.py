import tkinter as tk


def respond():
    txt = entry.get()
    chat.insert(tk.END, "You: " + txt + "\nBot: I heard you\n\n")


root = tk.Tk()
chat = tk.Text(root, width=40, height=15)
chat.pack()
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Send", command=respond).pack()
root.mainloop()
