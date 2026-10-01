# Write your solution here
item_count = int(input("How many items: "))
i = 1
my_list = []

while i <= item_count:
    items = int(input(f"Item {i}: "))
    my_list.append(items)
    i += 1
print(my_list)