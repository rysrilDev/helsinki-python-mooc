def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_sudoku = []
    for row in sudoku:
        new_sudoku.append(row[:])

    new_sudoku[row_no][column_no] = number
    return new_sudoku

def print_sudoku(sudoku: list):
    for r in range(9):
        for c in range(9):
            val = sudoku[r][c]
            
            # Print "_" for 0, otherwise print the number
            if val == 0:
                print("_", end=" ")
            else:
                print(f"{val}", end=" ")
            
            # Extra space after columns at index 2 and 5 (the 3rd and 6th numbers)
            if c == 2 or c == 5:
                print(" ", end="")
        
        # Move to the next line after finishing a row
        print()
        
        # Extra blank line after rows at index 2 and 5 (the 3rd and 6th rows)
        if r == 2 or r == 5:
            print()

# Write your solution here

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)