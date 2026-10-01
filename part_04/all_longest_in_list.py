def all_the_longest(my_list: list) -> list:
    max_len = 0
    for item in my_list:
        if len(item) > max_len:
            max_len = len(item)

    result = []
    for item in my_list:
        if len(item) == max_len:
            result.append(item)

    return result


if __name__ == "__main__":

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result)  # ['dorothy', 'richard']