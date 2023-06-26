todolist = []

# Load list from file
with open("ToDo.txt") as file:
    for entry in file:
        todolist.append(entry.strip())

# Make entries
print("Make your own To Do List:")
while True:
    entry = input("Give an entry (end with empty string): ")
    if entry == "":
        break
    
    todolist.append(entry)
    print(f"Added {entry} in the list")
print("")

# Print list
print("Your own To Do List:")
for index, entry in enumerate(todolist):
    print(f"{index + 1}. {entry}")

# Save to file
with open("ToDo.txt", "w") as file:
    for index, entry in enumerate(todolist):
        file.write(entry)
        if index + 1 != len(todolist):
            file.write("\n")