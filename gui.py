from tkinter import *

# Create the Tkinter application window
root = Tk()
root.title("ToDo List")

# Create a Label "ToDo List" in row 0
title = Label(root, text="ToDo List")
title.grid(row=0)

# Store entries here
todo_list = []

row_number = 3
total_label = None
# Function adds new entries to to do list
def add_entry():
    global row_number
    global total_label
    
    # Removes old total_label when it exist
    if total_label != None:
        total_label.grid_forget()
    
    # Create a new checkbutton
    var = IntVar()
    checkbox = Checkbutton(root, text=entrybox.get(), variable=var)
    checkbox.grid(row=row_number)
    entrybox.delete(0, END)
    # Add the new checkbutton to todo_lsit
    todo_list.append((checkbox, var))

    # Get stat numbers from todo_list list and var variable
    count_completed = 0
    count_total = 0
    for i in todo_list:
        count_completed += i[1].get()
        count_total += 1
    # Print out stats
    total_label = Label(root, text=f"Total%: {count_completed}/{count_total}")
    total_label.grid(row=row_number+1)

    row_number += 1

# Create a entrybox which allows users to enter new entries to application
entrybox = Entry(root, width=30, borderwidth=5)
entrybox.grid(row=1)

# Create a button, which submits entrybox
button = Button(root, text="New Entry", command=add_entry)
button.grid(row=2)

# Keeps application looping
root.mainloop()