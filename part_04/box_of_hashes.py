# Copy here code of line function from previous exercise
def line(integer, string):
    word = string
    if string == "":
        print(integer * "*")
    elif len(string) > 1:
        print(integer * string[0])
    else:
        print(integer * string)

def box_of_hashes(height):
    # You should call function line here with proper parameters
    while height > 0:
        height -= 1
        line(10, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
