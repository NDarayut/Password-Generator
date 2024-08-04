from pass_gen import *
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk

def checkbox_change():
    selected_option = []
    if letters.get():
        selected_option.append(1)
    if numbers.get():
        selected_option.append(2)
    if symbols.get():
        selected_option.append(3)
    return selected_option

def submit():
    selected_option = checkbox_change()
    password_length = length_var.get()


window = tk.Tk()
window.title("Password Generator")

# check box for users to choose their type of password
letters = tk.BooleanVar()
Checkbutton(window, text='Letters', variable=letters, command=checkbox_change).grid(row=0, sticky=W)
numbers = tk.BooleanVar()
Checkbutton(window, text='Numbers', variable=numbers, command=checkbox_change).grid(row=1, sticky=W)
symbols = tk.BooleanVar()
Checkbutton(window, text='Symbols', variable=symbols, command=checkbox_change).grid(row=2, sticky=W)

# password length
label = Label(window, text="Length of password")
label.grid(row=3, column=0)
length_var = tk.IntVar(value=8)
length = ttk.Spinbox(window, from_=8, to_=50, textvariable=length_var, wrap=True)
length.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

# generate button
submit = tk.Button(window, text='Generate', width=25, command= submit)
submit.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

# output
result = ttk.Label(window, text="")
result.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

window.mainloop()




