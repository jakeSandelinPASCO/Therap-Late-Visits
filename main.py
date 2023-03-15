import tkinter as tk
from tkinter import ttk

# Define functions for the button actions
def upload():
    print("Upload")

def email():
    print("Email")

def cancel():
    root.destroy()  # Close the entire GUI

# Create the GUI window
root = tk.Tk()
root.title("Microsoft Teams Style GUI")
root.configure(bg="#1f1e1e")

# Set the style of the buttons
style = ttk.Style()
style.configure('TButton', font=('Segoe UI', 12), foreground='black', background='#6264a7', padding=10)
style.map('TButton', background=[('active', '#4d4e8e')])

# Create the buttons
upload_button = ttk.Button(root, text="Upload", command=upload)
upload_button.grid(row=0, column=0, padx=10, pady=10)

email_button = ttk.Button(root, text="Email", command=email)
email_button.grid(row=0, column=1, padx=10, pady=10)

cancel_button = ttk.Button(root, text="Cancel", command=cancel)
cancel_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Set the style of the cancel button to be different
style.configure('CancelButton.TButton', font=('Segoe UI', 12), foreground='black', background='#c23636')
style.map('CancelButton.TButton', background=[('active', '#a72525')])

cancel_button.configure(style='CancelButton.TButton')

# Run the GUI
root.mainloop()
