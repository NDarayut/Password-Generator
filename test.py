import tkinter as tk
from tkinter import ttk

# Function to handle checkbox state change
def on_checkbox_change():
    selected_options = []
    if option1_var.get():
        selected_options.append("Option 1")
    if option2_var.get():
        selected_options.append("Option 2")
    if option3_var.get():
        selected_options.append("Option 3")
    return selected_options

# Function to handle submit button click
def on_submit():
    selected_options = on_checkbox_change()
    selected_number = spinbox_var.get()
    if selected_options:
        result_label.config(text=f"Selected options: {', '.join(selected_options)}, Number: {selected_number}")
    else:
        result_label.config(text=f"No options selected, Number: {selected_number}")

# Create the main window
root = tk.Tk()
root.title("Tkinter GUI Example")

# Create a frame for the checkboxes
checkbox_frame = ttk.LabelFrame(root, text="Select Options")
checkbox_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Create variables to hold the checkbox states
option1_var = tk.BooleanVar()
option2_var = tk.BooleanVar()
option3_var = tk.BooleanVar()

# Create checkboxes
checkbox1 = ttk.Checkbutton(checkbox_frame, text="Option 1", variable=option1_var, command=on_checkbox_change)
checkbox1.grid(row=0, column=0, sticky="w")
checkbox2 = ttk.Checkbutton(checkbox_frame, text="Option 2", variable=option2_var, command=on_checkbox_change)
checkbox2.grid(row=1, column=0, sticky="w")
checkbox3 = ttk.Checkbutton(checkbox_frame, text="Option 3", variable=option3_var, command=on_checkbox_change)
checkbox3.grid(row=2, column=0, sticky="w")

# Create a Spinbox for number selection
spinbox_var = tk.IntVar(value=8)  # Initialize with the starting value
number_spinbox = ttk.Spinbox(root, from_=8, to=50, textvariable=spinbox_var, wrap=True)
number_spinbox.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# Create a submit button
submit_button = ttk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

# Create a label to display results
result_label = ttk.Label(root, text="")
result_label.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

# Run the application
root.mainloop()
