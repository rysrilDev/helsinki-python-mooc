# Write your solution here
def spruce(size):
    i = 1
    print("a spruce!")
    while i <= size:
        spaces = (size - i) * " "
        stars = (2 * i - 1) * "*"
        print(spaces + stars)
        i += 1
    print(((size - 1) * " ") + "*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)