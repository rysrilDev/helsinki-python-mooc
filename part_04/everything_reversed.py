def everything_reversed(list1: list):
    new_list = []
    list1 = list1[::-1]
    
    for words in list1:
        new_list.append(words[::-1])
    return new_list
# Write your solution here

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)