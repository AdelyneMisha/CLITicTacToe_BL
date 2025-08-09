def display_board(board):
    print("-------------")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("-------------")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("-------------")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("-------------")


def winner(board):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
        (0, 4, 8), (2, 4, 6)              # diagonal
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != " ":
            return board[combo[0]]
    return None


def is_draw(board):
    return " " not in board and winner(board) is None


def user_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid input. Try again.")
                continue
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("That spot is already taken. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")


def minimax(board, depth, is_maximizing):
    result = winner(board)
    if result == "O":
        return 1
    elif result == "X":
        return -1
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score


def computer_move(board):
    best_score = float('-inf')
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    if move is not None:
        board[move] = "O"
        print(f"Computer chooses position {move + 1}")



print("Welcome to Tic Tac Toe!")

board = [" " for _ in range(9)]


print("Board positions (for reference):")
position_board = [str(i + 1) for i in range(9)]
display_board(position_board)


while True:
    print("Your turn!")
    user_move(board)
    display_board(board)

    if winner(board) == "X":
        print("Congratulations! You win!")
        break
    if is_draw(board):
        print("It's a draw!")
        break

    print("Computer's turn!")
    computer_move(board)
    display_board(board)

    if winner(board) == "O":
        print("Computer wins! Better luck next time.")
        break
    if is_draw(board):
        print("It's a draw!")
        break
print("Thanks for playing Tic Tac Toe!")