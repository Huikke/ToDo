# Gui for ToDo List program
from tkinter import *
from tkinter import messagebox
import main

# Create the Tkinter application window
root = Tk()
root.title("ToDo List")

# Create a Label "ToDo List" in row 0
title = Label(root, text="ToDo List")
title.grid(row=0, columnspan=2)

# Variable used to print entries in vacant row
row_number = 3

# Get stat numbers from todo_list list and var variable
# Grid the stat to the bottom of the application
total_label = None
def total_stat():
    global total_label
    # Remove old total_label from the application
    if total_label != None:
        total_label.grid_forget()

    # Count entries
    count_completed = 0
    count_total = 0
    for entry in todo_list_gui:
        if entry[1].get() == True:
            count_completed += 1
        count_total += 1

    # Print out stats
    total_label = Label(root, text=f"Stats: {count_completed}/{count_total} Done")
    total_label.grid(row=row_number+1, columnspan=2, sticky = E)

# Activated every time a checkbox state changes
def update_checkbox():
    # Sync GUI checkbox status with backend 
    for index, entry in enumerate(todo_list_backend):
        if entry["state"] != todo_list_gui[index][1].get():
            main.change_status(todo_list_backend, index)
            break
    # Update total_stat value
    total_stat()

# Load entries from a file
# Also store future files here
todo_list_backend = main.load_from_file()
todo_list_gui = []

# Grid entries from file to the application
# Change format to form gui uses and append it to todo_list
for entry in todo_list_backend:
    var = BooleanVar()
    var.set(entry["state"])
    checkbox = Checkbutton(root, text=entry["title"], variable=var, command=update_checkbox)
    checkbox.grid(row=row_number, columnspan=2)
    todo_list_gui.append((checkbox, var))

    row_number += 1
# Print stats
total_stat()

# Function adds new entries to to do list
def add_entry():
    global row_number
    entry_title = entrybox.get()

    # Pop up error when entrybox is empty
    if entry_title == "":
        messagebox.showerror("Error", "Empty entry")
        return

    # Create a new checkbutton
    var = BooleanVar()
    checkbox = Checkbutton(root, text=entry_title, variable=var, command=update_checkbox)
    checkbox.grid(row=row_number, columnspan=2)
    entrybox.delete(0, END)
    # Add the new checkbutton to todo_list
    todo_list_gui.append((checkbox, var))
    # Add the entry to todo_list_backend using main.py add_entry
    main.add_entry(todo_list_backend, entry_title)
    # Print stats
    total_stat()

    row_number += 1

# Save changes to file using main.py function
def save_to_file():
    main.save_to_file(todo_list_backend)
    messagebox.showinfo("Info", "Changes saved successfully")

# Create a entrybox which allows users to enter new entries to application
entrybox = Entry(root, width=30, borderwidth=3)
entrybox.grid(row=1, columnspan=2)

# Create a button, which submits entrybox
add_entry_button = Button(root, text="New Entry", width=10, command=add_entry)
add_entry_button.grid(row=2)
# Create a button,, which saves list to file
save_button = Button(root, text="Save", width=10, command=save_to_file)
save_button.grid(row=2, column=1)

# Keeps application looping
root.mainloop()