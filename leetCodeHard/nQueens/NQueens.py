class NQueens:

    def __init__(self, nqueens):
        self.n = nqueens

    def is_safe(self, board, row, col):
        # Check the column
        for i in range(row):
            if board[i][col] == "Q":
                return False

        # Check the diagonal (/) to the right
        for i,j in zip(range(row-1,-1,-1), range(col + 1, self.n)):
            if board[i][j] == "Q":
                return False

        # Check the diagonal (\) to the left
        for i, j in zip(range(row-1,-1,-1), range(col-1,-1,-1)):
            if board[i][j] == "Q":
                return False

        return True

    def place_queens(self, row, board, sol):
        n = len(board)
        # Reached the last row when all queens are placed, so this is a valid solution
        if row == n:
            results = []
            for i in range(n):
                results.append(''.join(board[i]))
            sol.append(results)

        # Check column by column
        for col in range(n):
            if self.is_safe(board, row, col):
                board[row][col] = "Q"
                # Check the next row
                if self.place_queens(row + 1, board, sol):
                    return True
                board[row][col] = "."
                # Backtrack
        return False

    # Solve for nqueens using basic backtracking
    def nqueens_basic(self):
        sol = []
        board = [["."] * self.n for i in range(self.n)]
        self.place_queens(0, board, sol)
        return sol


    # optimize by considering how diagonals work
    def nqueens_v2(self):
        pass