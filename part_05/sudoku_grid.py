def row_correct(sudoku: list, row_no: int):
    for number in sudoku[row_no]:
        if (sudoku[row_no].count(number) > 1) and (number > 0):
            return False
    return True

def column_correct(sudoku: list, column_no: int):
    numbers = []
    for row in sudoku:
        if row[column_no] in numbers:
            return False
        elif row[column_no] > 0:
            numbers.append(row[column_no])
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for r_number in range(row_no, row_no + 3):
        for c_number in range(column_no, column_no + 3):
            number = sudoku[r_number][c_number]
            if number > 0:
                if number in numbers:
                    return False
                numbers.append(number)
    return True

def sudoku_grid_correct(sudoku: list):
    for i in range(len(sudoku)):
        if not row_correct(sudoku, i):
            return False
        if not column_correct(sudoku, i):
            return False

    for r in range(0, len(sudoku), 3):
        for c in range(0, len(sudoku), 3):
            if not block_correct(sudoku, r, c):
                return False
    return True

        
# Write your solution here

if __name__ == "__main__":
    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 4, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))
