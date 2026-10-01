def no_shouting(my_list: list):
    new_list = []
    for word in my_list:
        if not word.isupper():
            new_list.append(word)
    return new_list
# Write your solution here

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)