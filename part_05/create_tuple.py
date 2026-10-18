def create_tuple(x: int, y: int, z: int):
    smallest = min([x, y, z])
    biggest = max([x, y, z])
    add = sum([x, y, z])
    tuple = (smallest, biggest, add)
    return tuple

# Write your solution here

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))