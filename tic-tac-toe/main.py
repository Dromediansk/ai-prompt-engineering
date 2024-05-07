AI_PLAYER = "O"
HUMAN_PLAYER = "X"

def evaluate(board):
    winner = check_win(board)
    if winner == AI_PLAYER:
        return +10
    elif winner == HUMAN_PLAYER:
        return -10
    else:
        return 0  # Draw

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def is_terminal_state(board):
    # A terminal state is when either a player has won or the board is full
    return evaluate(board) != 0 or is_board_full(board)

def generate_moves(board, player):
    moves = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            # If the current position is empty, it's a valid move
            if board[i][j] == " ":
                # Create a new board state with the current player's symbol in the position
                new_board = [row[:] for row in board]
                new_board[i][j] = player
                moves.append(new_board)
    return moves
    
def minimax(board, depth, is_maximizing_player):
    player = AI_PLAYER if is_maximizing_player else HUMAN_PLAYER
    if is_terminal_state(board):
        return evaluate(board)
    
    if is_maximizing_player:
        best_score = float('-inf')
        for move in generate_moves(board, player):
            score = minimax(move, depth + 1, False)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in generate_moves(board, player):
            score = minimax(move, depth + 1, True)
            best_score = min(score, best_score)
        return best_score

def print_board(board):
  for row in board:
    print(" | ".join(row))
    print("-" * 9)

def get_move(player, board):
    while True:
        move = input(f"Player {player}, enter your move (1-9): ")
        if move in [str(i) for i in range(1, 10)]:
            row, col = divmod(int(move) - 1, 3)
            if board[row][col] == " ":
                return int(move) - 1
            else:
                print("That spot is taken. Try again.")
        else:
            print("Invalid move. Try again.")

def get_ai_move(board):
    best_val = -1000
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_val = minimax(board, 0, False)
                board[i][j] = " "  # Undo move
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

def update_board(board, player, move):
    row, col = divmod(move, 3)
    if board[row][col] == " ":
        board[row][col] = player
    return board

def check_win(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]//3][condition[0]%3] == board[condition[1]//3][condition[1]%3] == board[condition[2]//3][condition[2]%3] != " ":
            return board[condition[0]//3][condition[0]%3]
    return None

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = HUMAN_PLAYER

    for i in range(9):
        print_board(board)
        if player == HUMAN_PLAYER:
            move = get_move(player, board)
        else:  # AI's turn
            move = get_ai_move(board)
            print(f"AI chose spot {move[0]*3 + move[1] + 1}")
        row, col = move if isinstance(move, tuple) else divmod(move, 3)
        board[row][col] = player
        if check_win(board):
            print(f"Player {player} wins!")
            print_board(board)
            return
        player = AI_PLAYER if player ==HUMAN_PLAYER else HUMAN_PLAYER

    print("It's a draw!")
    print_board(board)

tic_tac_toe()