import random

def calculate_attacks(board):
    return sum(board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]) for i in range(len(board)) for j in range(i + 1, len(board)))

def print_board(board):
    for row in range(len(board)):
        print(" ".join("Q" if board[row] == col else "-" for col in range(len(board))))

def random_board(n):
    return random.sample(range(n), n)

def hill_climbing(n):
    board = random_board(n)
    current_attacks = calculate_attacks(board)
    while True:
        neighbor = board.copy()
        i, j = random.sample(range(n), 2)
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
        neighbor_attacks = calculate_attacks(neighbor)
        if neighbor_attacks < current_attacks:
            board, current_attacks = neighbor, neighbor_attacks
        else:
            break
    return board

solution = hill_climbing(8)
print("Solution (queen positions):", solution)
print("Chessboard:")
print_board(solution)
