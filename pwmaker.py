"""Password Generator with GUI"""

from tkinter import *
from tkinter import ttk
import random

def display():
    return Label(window, text = pw(ent.get()), fg = "black").grid()
def pw(n):
    characters = 'abcdefghijklmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVWYXZ1234567890.'
    n = int(n)
    password= ''
    for i in range(n):
        password += random.choice(characters)
    return password

window = Tk()
window.geometry("400x400")
window.title("password generator")
title = Label(window, text = "Length").grid(row = 0, column = 0)
ent = Entry(window)
ent.grid(row = 0, column = 1)
but1 = Button(window, text = "create", command = display).grid(row = 1, column = 1)
window.mainloop()
