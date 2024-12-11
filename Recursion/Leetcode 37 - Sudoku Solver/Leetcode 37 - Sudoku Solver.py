# https://leetcode.com/problems/sudoku-solver

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(row, col, digit):
            """Checks if placing 'digit' at (row, col) is valid."""
            for i in range(9):
                # Check row
                if board[row][i] == digit:
                    return False
                # Check column
                if board[i][col] == digit:
                    return False
                # Check 3x3 box
                if board[3 * (row // 3) + (i // 3)][3 * (col // 3) + (i % 3)] == digit:
                    return False
            return True

        def helper():
            """Recursively solves the Sudoku board."""
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for digit in '123456789':
                            if isValid(i, j, digit):
                                board[i][j] = digit
                                if helper():
                                    return True
                                board[i][j] = '.'
                        return False
            return True
        helper()


        
# Time Complexity: O(9^(n*n))
# Space Complexity: O(n*n)