import collections
from typing import List

#SKIP i dont play board games
class Solution:
    def isValidSudoku(self, board):
        seen = sum(([(c, i), (j, c), (i / 3, j / 3, c)]
             for i, row in enumerate(board)
             for j, c in enumerate(row)
             if c != '.'), [])
        return len(seen) == len(set(seen))

s = Solution()
print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))