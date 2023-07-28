from tkinter import *

# Create the Tkinter application window
root = Tk()
root.title("ToDo List")

# Create a Label "ToDo List" in row 0
title = Label(root, text="ToDo List")
title.grid(row=0)

# Function adds new entries to to do list
row_count = 3
def add_entry():
    global row_count
    checkbox = Checkbutton(root, text=entrybox.get())
    checkbox.grid(row=row_count, column=0)
    entrybox.delete(0, END)
    row_count += 1

# Create a entrybox which allows users to enter new entries to application
entrybox = Entry(root, width=30, borderwidth=5)
entrybox.grid(row=1)

# Create a button, which submits entrybox
button = Button(root, text="New Entry", command=add_entry)
button.grid(row=2)

# Keeps application looping
root.mainloop()