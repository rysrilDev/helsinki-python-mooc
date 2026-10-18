# Write your solution here
contacts = {}

while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 3:
        break

    name = str(input("name: "))

    if command == 2:
        number = input("number: ")
        
        contacts[name] = number
        print("ok!")
    elif command == 1:
        if name in contacts:
            print(contacts[name])
        else:
            print("no number")
print("quitting...")