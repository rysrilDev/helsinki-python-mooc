# Write your solution here
words = []

while True:
    word = input("Word: ")

    if word in words:
        break
    else:
        words.append(word)
        lenght = len(words)
print(f"You typed in {lenght} different words")