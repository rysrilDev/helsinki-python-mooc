alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

layers = int(input("Layers: "))
size = 2 * layers - 1

for row in range(size):
    line = ""
    for col in range(size):
        d = min(row, col, size - 1 - row, size - 1 - col)
        line += alphabet[layers - 1 - d]
    print(line)