# Write your solution here
def line(integer, string):
    word = string
    if string == "":
        print(integer * "*")
    elif len(string) > 1:
        print(integer * string[0])
    else:
        print(integer * string)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")