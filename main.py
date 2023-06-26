todolist = []

print("Make your own To Do List:")
while True:
    entry = input("Give an entry (end with empty string): ")
    if entry == "":
        break
    
    todolist.append(entry)
    print(f"Added {entry} in the list")
print("")

print("Your own To Do List:")
index = 1
for entry in todolist:
    print(f"{index}. {entry}")
    index += 1