# ToDo List text-based version
# GUI also uses these functions
import json
from datetime import datetime, timezone

# Load list from a file
# Returns loaded list
def load_from_file():
    with open("ToDo.json") as file:
        data = json.load(file)
        todo_list = [e for e in data]

    return todo_list

# Save list to a file
def save_to_file(todo_list):
    with open("ToDo.json", "w") as file:
        data = json.dumps(todo_list, indent=4)
        file.write(data)

# Make an entry
def add_entry(todo_list, title):
    entry = {
        "state": False,
        "title": title,
        "creation_time": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "completion_time": None
    }

    todo_list.append(entry)
    print(f"Added '{entry['title']}' in the list")

# Change an entry status
def change_status(todo_list, index):
    if todo_list[index]["state"] == False:
        todo_list[index]["state"] = True
        todo_list[index]["completion_time"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
        print(f"'{todo_list[index]['title']}' completed!")
    else:
        todo_list[index]["state"] = False
        todo_list[index]["completion_time"] = None
        print(f"'{todo_list[index]['title']}' completion reverted")

# Change an entry title
def change_title(index, new_title):
    old_title = todo_list[index]["title"]
    todo_list[index]["title"] = new_title
    print(f"'{old_title}' changed to '{new_title}'")

# Delete an entry
def delete_entry(index):
    print(f"Deleted '{todo_list[index]['title']}' from the list")
    del todo_list[index]

# Timezone offset
def timezone_convert(date):
    utc_offset = datetime.now() - datetime.utcnow()
    return date + utc_offset

# View timeline
def entry_timeline(index):
    print(f"'{todo_list[index]['title']}' timeline:")
    creation_time = timezone_convert(datetime.fromisoformat(todo_list[index]["creation_time"])).strftime("%d/%Y/%m %H:%M")
    print(f"Created: {creation_time}")

    if todo_list[index]['completion_time'] != None:
        completion_time = timezone_convert(datetime.fromisoformat(todo_list[index]["completion_time"])).strftime("%d/%Y/%m %H:%M")
        print(f"Completed: {completion_time}")

# Print list
def display():
    print("Your To Do list:")
    for index, entry in enumerate(todo_list):
        checkmark = "x" if entry['state'] == True else " "
        print(f"{index + 1}. [{checkmark}] {entry['title']}")

# Print UI
def ui():
    print("Choose action:")
    print("1. Add task")
    print("2. Complete task")
    print("3. Change task title")
    print("4. Delete task")
    print("5. Print To Do list")
    print("6. View task timeline")
    print("0. End program & save to file")


if __name__ == "__main__":
    # Main loop
    first = True
    while True:
        if first:
            todo_list = load_from_file()
            display()
            print()
            first = False
        ui()

        choice = input("Input: ")
        if choice == "1":
            add_entry(todo_list, input("Task title: "))
        elif choice == "2":
            change_status(todo_list, int(input("Entry index: ")) - 1)
        elif choice == "3":
            change_title(int(input("Entry index: ")) - 1, input("New title: "))
        elif choice == "4":
            delete_entry(int(input("Delete entry index: ")) - 1)
        elif choice == "5":
            print()
            display()
        elif choice == "6":
            entry_timeline(int(input("Entry index: ")) - 1)
        elif choice == "0":
            save_to_file(todo_list)
            break
        else:
            print("Invalid Input!")
        print()