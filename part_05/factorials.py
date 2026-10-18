def factorials(n: int):
    k = {}
    mult = 1
    for number in range(1, n + 1):
        mult *= number
        k[number] = mult
    return k
# Write your solution here

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])