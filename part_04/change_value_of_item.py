# Write your solution here
my_list = [1, 2, 3, 4, 5]

while True:
    number = int(input("Index: "))

    if number < 0:
        break
    elif number >= 0:
        new_value = int(input("New Value: "))
        my_list[number] = new_value
        print(my_list)

