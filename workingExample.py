import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import ttk

# Create a sample dataframe
data = {'Name': ['Bob, Smith', 'Jen, Smith', 'Tony, Dith',],
        'Service Provider': ['Billian, Smith', 'Jenny, Doth', 'Tony, Blithin',],
        'Phone Number': ['1234567890', '1234567890', '1234567890',],
        'Email Address': ['theBigBob@BoblovesTrucks.com', 'AmyWhineWhiner@IWhineALot.com', 'emailGuy@anon.com',],         
        'Contact?': [True, False, True]}
df = pd.DataFrame(data)

# Toggle Row True or False
def toggle_value(row_num):
    # Get the current value
    current_val = df.at[row_num, 'Contact?']
    # Toggle the value
    df.at[row_num, 'Contact?'] = not current_val
    # Update the GUI
    update_gui()

# Update the frame with the new value
def update_gui():
    # Clear the current GUI
    for widget in second_frame.winfo_children():
        widget.destroy()

    # Add a label for each row of the dataframe
    for index, row in df.iterrows():
        label = tk.Label(second_frame, text=row['Name'])
        label.grid(row=index+1, column=0)

        label = tk.Label(second_frame, text=row['Service Provider'])
        label.grid(row=index+1, column=1)

        label = tk.Label(second_frame, text=row['Phone Number'])
        label.grid(row=index+1, column=2)

        label = tk.Label(second_frame, text=row['Email Address'])
        label.grid(row=index+1, column=3)

        # Add a button to toggle the value in Contact? for this row
        button_text = 'True' if row['Contact?'] else 'False'
        button = tk.Button(second_frame, text=button_text, command=lambda row_num=index: toggle_value(row_num))
        button.grid(row=index+1, column=4)

    # Add headers for the columns
    name_label = tk.Label(second_frame, text='Client Name')
    name_label.grid(row=0, column=0)

    provider_label = tk.Label(second_frame, text='Servicer Provider')
    provider_label.grid(row=0, column=1)

    phone_label = tk.Label(second_frame, text='Phone Number')
    phone_label.grid(row=0, column=2)

    email_label = tk.Label(second_frame, text='Email Address')
    email_label.grid(row=0, column=3)

    Contact_label = tk.Label(second_frame, text='Contact?')
    Contact_label.grid(row=0, column=4)

    # Add a submit button to save the results to a new dataframe
    submit_button = tk.Button(second_frame, text='Submit', command=save_results)
    submit_button.grid(row=len(df)+2, column=0, columnspan=2)

# Define a function to save the results to a new dataframe
def save_results():
    # Create a new dataframe to store the results
    results_data = {'Name': [],'Service Provider': [],'Phone Number': [],'Email Address': [],'Contact?': []}
    results_df = pd.DataFrame(results_data)

    # Iterate over the rows of the original dataframe and append the results to the new dataframe
    for index, row in df.iterrows():
        results_df = results_df.append({'name': row['Name'],'provider': row['Service Provider'],'phone number': row['Phone Number'],'email address': row['Email Address'], 'Contact?': row['Contact?']}, ignore_index=True)

    # Print the new dataframe to the console
    print(results_df)

# Create the GUI
root = tk.Tk()

# Add a frame to hold the labels and buttons
frame = tk.Frame(root)
frame.pack(fill=BOTH, expand=1)

#add canvas
canvas = Canvas(frame)
canvas.pack(side=LEFT, fill=BOTH, expand=1)

#add scrollbar
myScroll = ttk.Scrollbar(frame, orient = VERTICAL, command = canvas.yview)
myScroll.pack(side=RIGHT, fill=Y)

#configure the canvas
canvas.configure(yscrollcommand=myScroll.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion= canvas.bbox("all")))

#another frame in the canvas
second_frame = Frame(canvas)

#Add second frame to window in canvas
canvas.create_window((0,0),window=second_frame, anchor="nw")

# Update the GUI based on the initial state of the dataframe
update_gui()

# Start the main event loop
root.mainloop()
