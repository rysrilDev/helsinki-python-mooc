# Write your solution here
def palindromes(word: str):
    return word == word[::-1]
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

while True:
    palin = input("Please type in a palindrome: ")
    if palindromes(palin):
        print(f"{palin} is a palindrome!")
        break
    print("that wasn't a palindrome")
