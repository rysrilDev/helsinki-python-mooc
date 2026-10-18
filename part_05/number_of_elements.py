def count_matching_elements(my_matrix: list, element: int):
    count = 0
    for i in range(len(my_matrix)):
        for n in my_matrix[i]:
            if element == n:
                count += 1
    return count

# Write your solution here

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))