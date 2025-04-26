#Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and Backtracking for n-queens problem or a graph coloring problem.
def is_safe(board, row, col, N):
    # Check for queen in the same column and diagonals
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens_backtracking(board, row, N):
    if row == N:
        print_board(board, N)
        return True
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            if solve_nqueens_backtracking(board, row + 1, N):
                return True
            board[row] = -1  # Backtrack
    return False

def print_board(board, N):
    for i in range(N):
        row = ['Q' if board[i] == j else '.' for j in range(N)]
        print(" ".join(row))
    print()

def nqueens_backtracking(N):
    board = [-1] * N
    if not solve_nqueens_backtracking(board, 0, N):
        print("Solution does not exist.")

nqueens_backtracking(4)
