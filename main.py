import json
from datetime import datetime, timezone

# Load list from file
with open("ToDo.json") as file:
    data = json.load(file)
    todolist = [e for e in data]

# Make an entry
def add_entry(title):
    entry = {
        "state": False,
        "title": title,
        "creation_time": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "completion_time": None
    }

    todolist.append(entry)
    print(f"Added '{entry['title']}' in the list")

# Change an entry status
def change_status(index):
    if todolist[index]["state"] == False:
        todolist[index]["state"] = True
        todolist[index]["completion_time"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
        print(f"'{todolist[index]['title']}' completed!")
    else:
        todolist[index]["state"] = False
        todolist[index]["completion_time"] = None
        print(f"'{todolist[index]['title']}' completion reverted")

# Delete an entry
def delete_entry(index):
    print(f"Deleted '{todolist[index]['title']}' from the list")
    del todolist[index]

# View timeline
def entry_timeline(index):
    print(f"'{todolist[index]['title']}' timeline:")

    creation_time = datetime.fromisoformat(todolist[index]["creation_time"]).strftime("%d/%Y/%m %H:%M")
    print(f"Created: {creation_time}")

    if todolist[index]['completion_time'] != None:
        completion_time = datetime.fromisoformat(todolist[index]["completion_time"]).strftime("%d/%Y/%m %H:%M")
        print(f"Completed: {completion_time}")

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
    print("5. View task timeline")
    print("0. End program & save to file")

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
        change_status(int(input("Entry index: ")) - 1)
    elif choice == "3":
        delete_entry(int(input("Delete entry index: ")) - 1)
    elif choice == "4":
        print()
        display()
    elif choice == "5":
        entry_timeline(int(input("Entry index: ")) - 1)
    elif choice == "0":
        break
    else:
        print("Invalid Input!")
    print()

# Save to file
with open("ToDo.json", "w") as file:
    data = json.dumps(todolist, indent=4)
    file.write(data)