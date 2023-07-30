from tkinter import *
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
    for entry in todo_list:
        if entry[1].get() == True:
            count_completed += 1
        count_total += 1

    # Print out stats
    total_label = Label(root, text=f"Total%: {count_completed}/{count_total}")
    total_label.grid(row=row_number+1)

# Load entries from a file
# Also store future files here
todo_list_temp = main.load_from_file()
todo_list = []

# Grid entries from file to the application
# Change format to form gui uses and append it to todo_list
for entry in todo_list_temp:
    var = BooleanVar()
    var.set(entry["state"])
    checkbox = Checkbutton(root, text=entry["title"], variable=var)
    checkbox.grid(row=row_number)
    todo_list.append((checkbox, var))

    row_number += 1
# Print stats
total_stats()

# Function adds new entries to to do list
def add_entry():
    global row_number

    # Create a new checkbutton
    var = BooleanVar()
    checkbox = Checkbutton(root, text=entrybox.get(), variable=var)
    checkbox.grid(row=row_number)
    entrybox.delete(0, END)
    # Add the new checkbutton to todo_lsit
    todo_list.append((checkbox, var))
    # Print stats
    total_stats()

    row_number += 1

# Create a entrybox which allows users to enter new entries to application
entrybox = Entry(root, width=30, borderwidth=3)
entrybox.grid(row=1)

# Create a button, which submits entrybox
button = Button(root, text="New Entry", command=add_entry)
button.grid(row=2)

# Keeps application looping
root.mainloop()