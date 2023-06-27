todolist = []

# Load list from file
with open("ToDo.txt") as file:
    for entry in file:
        entry = [entry[3], entry[6:].strip()]
        todolist.append(entry)

# Make an entry
def add_entry(title):
    entry = [" ", title]
    todolist.append(entry)
    print(f"Added '{entry[1]}' in the list")

# Change an entry status between " " and "x"
def change_status(index):
    if todolist[index - 1][0] == " ":
        todolist[index - 1][0] = "x"
        print(f"'{todolist[index - 1][1]}' completed!")
    else:
        todolist[index - 1][0] = " "
        print(f"'{todolist[index - 1][1]}' completion reverted")

# Delete an entry
def delete_entry(index):
    print(f"Deleted '{todolist[index - 1][1]}' from the list")
    del todolist[index - 1]

# Print list
def display():
    print("Your To Do list:")
    for index, entry in enumerate(todolist):
        print(f"{index + 1}. [{entry[0]}] {entry[1]}")

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
        change_status(int(input("Entry index: ")))
    elif choice == "3":
        delete_entry(int(input("Delete entry index: ")))
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
        entry = f"- [{entry[0]}] {entry[1]}"
        file.write(entry)
        if index + 1 != len(todolist):
            file.write("\n")