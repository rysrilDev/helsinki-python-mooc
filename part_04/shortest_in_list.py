# Write your solution here
def shortest(my_list: list):
    shortest = ""
    for name in my_list:
        if len(name) > len(shortest):
            shortest = name
    for i in my_list:
        if len(i) < len(shortest):
            shortest = i

    return shortest

# def shortest(names: list):
    result = ""
 
    for nimi in names:
        if result == "" or len(nimi) < len(result):
            result = nimi
 
    return result

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']