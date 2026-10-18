def invert(dictionary: dict):
    inverted = {}
    for key, value in dictionary.items():
        inverted[value] = key
    dictionary.clear()
    dictionary.update(inverted) 
# Write your solution here

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)