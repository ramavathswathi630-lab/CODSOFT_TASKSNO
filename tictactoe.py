import math

board = [' ' for _ in range(9)]

def print_board():
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def is_winner(b, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(b[spot] == player for spot in cond) for cond in win_conditions)

def is_board_full(b):
    return ' ' not in b

def minimax(b, depth, is_maximizing):
    if is_winner(b, 'O'): return 1
    if is_winner(b, 'X'): return -1
    if is_board_full(b): return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                max_eval = max(max_eval, minimax(b, depth + 1, False))
                b[i] = ' '
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                min_eval = min(min_eval, minimax(b, depth + 1, True))
                b[i] = ' '
        return min_eval

def play_game():
    print("❌ Tic-Tac-Toe AI (CodSoft Task 2) ⭕")
    print("You are 'X', AI is 'O'. Enter positions 0-8.")
    print_board()
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if board[move] != ' ':
                print("Spot taken! Try another.")
                continue
        except:
            print("Invalid input. Enter a number 0 to 8.")
            continue
        board[move] = 'X'
        if is_winner(board, 'X'):
            print_board(); print("You win!"); break
        if is_board_full(board):
            print_board(); print("It's a tie!"); break

        # AI move
        best_score = -math.inf; best_move = 0
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, 0, False)
                board[i] = ' '
                if score > best_score:
                    best_score = score; best_move = i
        board[best_move] = 'O'

        if is_winner(board, 'O'):
            print_board(); print("AI wins!"); break
        if is_board_full(board):
            print_board(); print("It's a tie!"); break
        print_board()

if __name__ == "__main__":
    play_game()