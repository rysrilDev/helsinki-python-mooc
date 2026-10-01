# Write your solution here

my_list = []

while True:
    print(f"The list is now {my_list}")
    choice = input("a(d)d, (r)emove or e(x)it: ")
    length = len(my_list)
    if choice == "x":
        break
    elif choice == "d":
        my_list.append(length + 1)
    elif choice == "r":
        my_list.pop(length - 1)
print("Bye!")