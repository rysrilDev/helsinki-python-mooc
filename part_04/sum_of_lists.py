# Write your solution here
def list_sum(a, b):
    results = []
    for i in range(len(a)):
        results.append(a[i] + b[i])
        print(a[i] + b[i])
    return results



if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]