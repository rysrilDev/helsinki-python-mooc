def longest_series_of_neighbours(my_list):
    longest = 1
    current = 1
    for i in range(1, len(my_list)):
        diff = my_list[i] - my_list[i - 1]
        if diff == -1 or diff == 1:
            current += 1
            if current > longest:
                longest = current
        else:
            current = 1
    return longest

# next time I can use max(longest, current) and abs(difference) it gives the absoulete value

# Write your solution here

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))