# Copy here code of line function from previous exercise
def line(integer, string):
    word = string
    if string == "":
        print(integer * "*")
    elif len(string) > 1:
        print(integer * string[0])
    else:
        print(integer * string)

def square_of_hashes(size):
    # You should call function line here with proper parameters
    number = 0
    while number < size:
        number += 1
        line(size, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
