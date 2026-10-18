# Write your solution here
contacts = {}

while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 3:
        break

    name = str(input("name: "))

    if command == 2:
        number = input("number: ")

        if name not in contacts:
            contacts[name] = []

        contacts[name].append(number)
        print("ok!")
    elif command == 1:
        if name in contacts:
            for number in contacts[name]:
                print(number)
        else:
            print("no number")
print("quitting...")
# Write your solution here