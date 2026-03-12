import random
import string
import tkinter as tk

def generate_password():
    length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text=password)

app = tk.Tk()
app.title("Password Generator")
app.geometry("300x200")

title = tk.Label(app, text="Password Generator", font=("Arial", 14))
title.pack(pady=10)

generate_btn = tk.Button(app, text="Generate Password", command=generate_password)
generate_btn.pack(pady=10)

result_label = tk.Label(app, text="", font=("Arial", 12))
result_label.pack(pady=10)

app.mainloop()
