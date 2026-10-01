def most_common_character(word):
    letter = word[0]
    for i in word:
        if word.count(i) > word.count(letter):
            letter = i
    return letter

# Write your solution here

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))