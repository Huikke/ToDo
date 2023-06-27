todolist = []

# Load list from file
with open("ToDo.txt") as file:
    for entry in file:
        todolist.append(entry.strip())

# Make entries
def add_entry(title):
    entry = title
    todolist.append(entry)
    print(f"Added {entry} in the list")

# Print list
def display():
    print("Your To Do list:")
    for index, entry in enumerate(todolist):
        print(f"{index + 1}. {entry}")

# Print UI
def ui():
    print("Choose action:")
    print("1. Add task")
    print("2. Complete task")
    print("3. Delete task")
    print("4. Print To Do list")
    print("5. End program & save to file")

# Main loop
first = True
while True:
    if first:
        display()
        print()
        first = False
    ui()

    choice = input("Input: ")
    if choice == "1":
        add_entry(input("Task title: "))
    elif choice == "2":
        #TODO
        print("WIP")
    elif choice == "3":
        #TODO
        print("WIP")
    elif choice == "4":
        print()
        display()
    elif choice == "5":
        break
    else:
        print("Invalid Input!")
    print()

# Save to file
with open("ToDo.txt", "w") as file:
    for index, entry in enumerate(todolist):
        file.write(entry)
        if index + 1 != len(todolist):
            file.write("\n")