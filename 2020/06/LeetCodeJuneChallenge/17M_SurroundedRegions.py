from typing import List
#Runtime: 144 ms, faster than 78.53% of Python3 online submissions for Surrounded Regions.
#Memory Usage: 15.2 MB, less than 62.60% of Python3 online submissions for Surrounded Regions.
#Border traversal then DFS replace elements. Double n^2 pass to convert inner O's.
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0: return
        self.board = board
        m = len(board)
        n = len(board[0])
        for i in range(len(board)):
            for j, a in enumerate(board[i]):
                if a=='O' and (i==0 or i == m-1 or j == 0 or j == n-1):
                    self.dfs(i, j, m, n)
        for i in range(len(board)):
            for j, b in enumerate(board[i]):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '*':
                    board[i][j] = 'O'
        return board

    def dfs(self, i, j, m, n):
        board = self.board
        if i < 0 or i == m: return
        if j < 0 or j == n: return
        if board[i][j] == "*" or board[i][j] == "X": return
        if board[i][j] == 'O':
            board[i][j] = '*'
        self.dfs(i - 1, j, m, n)
        self.dfs(i + 1, j, m, n)
        self.dfs(i, j - 1, m, n)
        self.dfs(i, j + 1, m, n)

import numpy as np
s = Solution()
print(s.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))

