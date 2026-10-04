import math

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    # rows, cols, diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]!= " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]!= " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2]!= " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]!= " ":
        return board[0][2]
    return None

def is_full(board):
    return all(cell!= " " for row in board for cell in row)

def minimax(board, is_max):
    winner = check_winner(board)
    if winner == "O": return 1
    if winner == "X": return -1
    if is_full(board): return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = max(best, minimax(board, False))
                    board[i][j] = " "
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = min(best, minimax(board, True))
                    board[i][j] = " "
        return best

def best_move(board):
    best_val = -math.inf
    move = (-1,-1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                val = minimax(board, False)
                board[i][j] = " "
                if val > best_val:
                    best_val = val
                    move = (i,j)
    return move

# Game Loop
board = [[" "]*3 for _ in range(3)]
print("Tic Tac Toe - You are X, AI is O")
print_board(board)

while True:
    # User move
    r = int(input("Enter row (0-2): "))
    c = int(input("Enter col (0-2): "))
    if board[r][c]!= " ":
        print("Invalid move!")
        continue
    board[r][c] = "X"
    print_board(board)
    if check_winner(board) or is_full(board):
        break

    # AI move
    print("AI's turn...")
    r,c = best_move(board)
    board[r][c] = "O"
    print_board(board)
    if check_winner(board) or is_full(board):
        break

winner = check_winner(board)
if winner:
    print(f"Winner is {winner}!")
else:
    print("It's a Draw!")
