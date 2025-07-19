from tkinter import *
import pyperclip
import random

app = Tk()
app.geometry("400x400")

generated_password = StringVar()
password_length = IntVar()
password_length.set(0)

def create_password():
    chars = ('abcdefghijklmnopqrstuvwxyz'
             'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
             '1234567890 !@#$%^&amp;*()')
    
    new_password = "".join(random.choice(chars) for _ in range(password_length.get()))
    generated_password.set(new_password)

def copy_password():
    pyperclip.copy(generated_password.get())

Label(app, text="Password Generator", font="calibri 20 bold").pack()
Label(app, text="Enter password length").pack(pady=3)
Entry(app, textvariable=password_length).pack(pady=3)
Button(app, text="Generate", command=create_password).pack(pady=7)
Entry(app, textvariable=generated_password).pack(pady=3)
Button(app, text="Copy", command=copy_password).pack()

app.mainloop()