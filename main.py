from tkinter import *
from tkinter import messagebox
import random
text = 'abcdefghijklmnopqrstuvwxyz0123456789'
root = Tk()
root.title("Python Captcha Verification Example")
root.geometry("400x200")
captcha = StringVar()
input = StringVar()
def create_captcha():
    c = random.choices(text, k = 6)
    captcha.set(''.join(c))
def check():
    if captcha.get() == input.get():
        messagebox.showinfo('Results', 'Captcha  Verification Success..')
    else:
        messagebox.showerror('Results', 'Captcha Verification failed')
    input.set('')
    create_captcha()
Label(root, textvariable=captcha, font="ariel 16 bold").pack(padx=5, pady=5)
Entry(root, textvariable=input, bg='white', font="ariel 12 bold").pack(padx=5, pady=5)
Button(root, text="verify", font="ariel 15 bold", bg='gray', command=check).pack(padx=5, pady=5)
create_captcha()
root.mainloop()