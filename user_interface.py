from generator import generate_password
import tkinter as tk
from tkinter import Checkbutton, Label, W
from tkinter import ttk
from tkinter import messagebox


def checkbox_change():
    
    """
    Checkbox in tkinter allows user to pick and choose which condition they want to add.
    If a checkbox is not selected, then their default states return a "False" boolean.
    Whereas, a selected checkbox will return a "True" boolean.
    """

    select_letters = False
    select_numbers = False
    select_symbols = False

    if letters.get():
        select_letters = True
    if numbers.get():
        select_numbers = True
    if symbols.get():
        select_symbols = True

    return select_letters, select_numbers, select_symbols

def submit():
    """
    The submit button allow the user to submit their option after selecting a checkbox.
    This function uses selected option and the chosen length of the password to generate 
        a random string of password.

    After the password is generated, a copy will appear to let the user copy the result into
        their clipboard.
    
    User can simply re-generate the password again by clicking on the "Generate" button.

    """
    select_letters, select_numbers, select_symbols = checkbox_change() # Stores checkbox boolean into a variable
    password_length = length_var.get() # Get length from tkinter object

    if password_length < 8 or password_length > 50:
        messagebox.showerror("Input Error", "Length out of range. Must be within 8-50")
        return

    # Call function from generator.py to generate the password
    password = generate_password(password_length, include_letters=select_letters, include_numbers=select_numbers,
                      include_symbols=select_symbols)
    result.config(text=password) # display generated password in result display

    copy_result.grid(row=7, column=0, padx=10, pady=10, sticky="ew") # display the copy button

def copy_result():
    """
    The copy button allow user to copy the password from the result display into their clipboard.
    This button only show itself once the "submit" or "generate" button is pressed.
    """

    # Store the label text into a variable
    text = result["text"]

    # Copy result into your clipboard
    window.clipboard_clear() # Clear user clipboard before copying.
    window.clipboard_append(text)

    messagebox.showinfo("Copied", "Text copied to clipboard!")

def validate_length(value):
    """
    Function to check the length that user input in the spinbox. Range: 8-50
    """
    if value == "":
        return True
    try:
        # Convert value to an integer and check if it's in the allowed range
        val = int(value)
        return val > 0
    except ValueError:
        # If conversion fails, return False (invalid input)
        return False

# Create window object
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
# Create a validation command
vcmd = window.register(validate_length)

label = Label(window, text="Length of password")
label.grid(row=3, column=0)
length_var = tk.IntVar(value=8) # Initial value is set to 8
length = ttk.Spinbox(window, from_=8, to_=50, textvariable=length_var, wrap=True, validate="all", validatecommand=(vcmd, '%P'))
length.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

# generate submit button
submit = tk.Button(window, text='Generate', width=25, command= submit)
submit.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

# output
result = ttk.Label(window, text="")
result.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

# make copy button
copy_result = tk.Button(window, text='Copy', width = 25, command=copy_result)

window.mainloop()




