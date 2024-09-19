# https://leetcode.com/problems/n-queens

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isValid(row, col, board) -> bool:
            # horizontal
            c = 0
            while c < col:
                if board[row][c] == 'Q':
                    return False
                c = c + 1

            # vertical - no need to check

            # diagonal - check upper left
            r,c = row, col
            while r >= 0 and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r = r - 1
                c = c - 1
            
            # diagonal - lower left
            r,c = row, col
            while r < n and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r = r + 1
                c = c - 1

            return True

        def helper(col: int, board: List[str], res: List[List[str]]):
            # base condition
            if col == n:
                res.append([''.join(row) for row in board])
                return

            # placing Q in all rows of the current col
            for row in range(n):
                if isValid(row, col, board):
                    board[row][col] = 'Q'
                    helper(col+1, board, res)
                    board[row][col] = '.'
        
        if n == 1:
            return [["Q"]]
        if n == 2 or n == 3:
            return []

        res: List[List[str]] = []
        board = [['.']*n for i in range(n)]

        helper(0, board, res)
        return res
    
# Time Complexity: O(n!)
# Space Complexity: O(n^2)