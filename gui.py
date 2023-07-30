# Gui for ToDo List program
from tkinter import *
from tkinter import messagebox
import main

# Create the Tkinter application window
root = Tk()
root.title("ToDo List")

# Create a Label "ToDo List" in row 0
title = Label(root, text="ToDo List")
title.grid(row=0)

# Variable used to print entries in vacant row
row_number = 3

# Get stat numbers from todo_list list and var variable
# Grid the stat to the bottom of the application
total_label = None
def total_stats():
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
    total_label = Label(root, text=f"Total%: {count_completed}/{count_total}")
    total_label.grid(row=row_number+1)

# Load entries from a file
# Also store future files here
todo_list_backend = main.load_from_file()
todo_list_gui = []

# Grid entries from file to the application
# Change format to form gui uses and append it to todo_list
for entry in todo_list_backend:
    var = BooleanVar()
    var.set(entry["state"])
    checkbox = Checkbutton(root, text=entry["title"], variable=var)
    checkbox.grid(row=row_number)
    todo_list_gui.append((checkbox, var))

    row_number += 1
# Print stats
total_stats()

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
    checkbox = Checkbutton(root, text=entry_title, variable=var)
    checkbox.grid(row=row_number)
    entrybox.delete(0, END)
    # Add the new checkbutton to todo_list
    todo_list_gui.append((checkbox, var))
    # Add the entry to todo_list_backend using main.py add_entry
    main.add_entry(entry_title, todo_list_backend)
    # Print stats
    total_stats()

    row_number += 1

# Save changes to file
def save_to_file():
    # Sync checkbox variable status to backend list status 
    for index, entry in enumerate(todo_list_backend):
        entry["state"] = todo_list_gui[index][1].get()
    # Save to file using main.py function
    main.save_to_file(todo_list_backend)

# Create a entrybox which allows users to enter new entries to application
entrybox = Entry(root, width=30, borderwidth=3)
entrybox.grid(row=1)

# Create a button, which submits entrybox
add_entry_button = Button(root, text="New Entry", command=add_entry)
add_entry_button.grid(row=2)
# Create a button,, which saves list to file
save_button = Button(root, text="Save", command=save_to_file)
save_button.grid(row=2, column=1)

# Keeps application looping
root.mainloop()