
def mean(my_list: list):
    added = sum(my_list)
    mean_of_list = added / len(my_list)
    return mean_of_list
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [1, 2, 3]
    result = mean(my_list)
    print(result)