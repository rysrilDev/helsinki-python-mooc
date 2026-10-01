# Write your solution here
def same_chars(word, num1, num2):
    if len(word) - 1 < num2 or len(word) - 1 < num1:
        return False
    elif word[num1] != word[num2]:
        return False
    else:
        return True
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))    