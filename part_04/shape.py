# Copy here code of line function from previous exercise and use it in your solution
def line(integer, string):
    word = string
    if string == "":
        print(integer * "*")
    elif len(string) > 1:
        print(integer * string[0])
    else:
        print(integer * string)

def shape(size1, char1, size2, char2):
    # You should call function line here with proper parameters
    number = 0
    while number < size1:
        number += 1
        line(number, char1)
    while size2 > 0:
        size2 -= 1
        line(size1, char2)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")