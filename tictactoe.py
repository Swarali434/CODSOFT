import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))
    return empty_cells

def player_move(board):
    while True:
        try:
            row, col = map(int, input("Enter your move (row col): ").split())
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("That cell is already occupied. Try again.")
        except ValueError:
            print("Invalid input. Please enter two numbers separated by space.")

def ai_move(board):
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player_move(board)
        print_board(board)
        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

        print("its AI turn...")
        ai_row, ai_col = ai_move(board)
        board[ai_row][ai_col] = "O"
        print_board(board)
        if check_winner(board, "O"):
            print("AI wins! Better luck next time.")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
