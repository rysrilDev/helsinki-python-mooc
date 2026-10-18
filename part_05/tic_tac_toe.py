def play_turn(game_board: list, x: int, y: int, piece: str):

    if (x in range(0, 3)) and (y in range(0, 3)):
        place = game_board[y][x]
        if place == "":
            game_board[y][x] = piece
            return True
        else:
            return False
    else:
        return False

# Write your solution here

if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)