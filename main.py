import json

# Load list from file
with open("ToDo.json") as file:
    data = json.load(file)
    todolist = [e for e in data]

# Make an entry
def add_entry(title):
    entry = {"state": False, "title": title}
    todolist.append(entry)
    print(f"Added '{entry['title']}' in the list")

# Change an entry status
def change_status(index):
    if todolist[index - 1]["state"] == False:
        todolist[index - 1]["state"] = True
        print(f"'{todolist[index - 1]['title']}' completed!")
    else:
        todolist[index - 1]["state"] = False
        print(f"'{todolist[index - 1]['title']}' completion reverted")

# Delete an entry
def delete_entry(index):
    print(f"Deleted '{todolist[index - 1]['title']}' from the list")
    del todolist[index - 1]

# Print list
def display():
    print("Your To Do list:")
    for index, entry in enumerate(todolist):
        checkmark = "x" if entry['state'] == True else " "
        print(f"{index + 1}. [{checkmark}] {entry['title']}")

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
with open("ToDo.json", "w") as file:
    data = json.dumps(todolist)
    file.write(data)