import collections
from typing import List

#Original solution
#Runtime: 96 ms, faster than 87.20% of Python3 online submissions for Valid Sudoku.
#Memory Usage: 14 MB, less than 10.09% of Python3 online submissions for Valid Sudoku.

class Solution:
    def isValidSudoku(self, board) -> bool:
        seen = set()
        ct = 0
        for i, a in enumerate(board):
            for j, b in enumerate(a):
                if b != '.':
                    ct += 1
                    entry = [(b, i), (j, b), (b, i//3, j//3)]
                    seen.update(entry)
        print(seen)
        return len(seen) == ct * 3



#Runtime: 88 ms, faster than 98.64% of Python3 online submissions for Valid Sudoku.
#Memory Usage: 13.8 MB, less than 62.18% of Python3 online submissions for Valid Sudoku.

class Solution2:
    def isValidSudoku(self, board) -> bool:
        seen = sum(([(c, i), (j, c), (i // 3, j // 3, c)]
             for i, row in enumerate(board)
             for j, c in enumerate(row)
             if c != '.'), [])
        print(seen)
        print(len(seen))
        return len(seen) == len(set(seen))




s = Solution()
print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))