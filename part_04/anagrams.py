def anagrams(word1, word2: str):
    list1 = []
    list2 = []
    for char in word1:
        list1.append(char)
        ordered1 = sorted(list1)
    for char2 in word2:
        list2.append(char2)
        ordered2 = sorted(list2)
    if ordered1 == ordered2:
        return True
    else:
        return False

if __name__ == "__main__":
    anagrams("tame", "meta")
    anagrams("python", "java")
    anagrams("house","esuoh")
    anagrams('house', 'mouse')