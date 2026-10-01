def no_vowels(sentence: str):
    vowels = ["a", "e", "o", "i", "u"]
    for char in sentence:
        if char in vowels:
            sentence = sentence.replace(char, "")
    return sentence

# Write your solution here

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))