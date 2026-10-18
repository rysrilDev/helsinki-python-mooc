def times_ten(start_index: int, end_index: int):
    d = {}
    for number in range(start_index, end_index + 1):
        d[number] = number * 10
    return d

# Write your solution here

if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)