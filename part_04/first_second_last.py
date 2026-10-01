# Write your solution here
def first_word(sentence: str) -> str:
    # Find the index of the first space
    end_index = sentence.find(" ")
    return sentence[:end_index]


def second_word(sentence: str) -> str:
    # Find the end of the first word
    first_space = sentence.find(" ")
    # Cut off the first word
    remaining = sentence[first_space + 1 :]

    # Look for a space after the second word
    second_space = remaining.find(" ")

    # If there are no more spaces, the remaining string IS the second word
    if second_space == -1:
        return remaining

    return remaining[:second_space]


def last_word(sentence: str) -> str:
    # Scan backward from the end to find the start of the last word
    i = len(sentence) - 1
    while i >= 0:
        if sentence[i] == " ":
            return sentence[i + 1 :]
        i -= 1
    return sentence
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))