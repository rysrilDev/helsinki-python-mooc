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

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number

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

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)