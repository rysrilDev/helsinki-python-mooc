def histogram(word: str):
    letters = {}
    for letter in word:
        if letter not in letters:
            letters[letter] = 0
        letters[letter] += 1

    for letter in letters:
        print(f"{letter} {letters[letter] * '*'}")

# Write your solution here

if __name__ == "__main__":
    histogram("abab")
    histogram("statistically")