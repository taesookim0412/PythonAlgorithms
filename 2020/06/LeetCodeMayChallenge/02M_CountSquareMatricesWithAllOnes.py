from typing import List

import numpy as np
#Runtime: 644 ms, faster than 92.08% of Python3 online submissions for Count Square Submatrices with All Ones.
#Memory Usage: 15.8 MB, less than 86.04% of Python3 online submissions for Count Square Submatrices with All Ones.

#TODO: Create time In The Future to Make Algorithm without altering Matrix also practice dynamic programming !!do this!!

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i ==0 or j==0:
                        res += 1
                    else:
                        matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + matrix[i][j]
                        res += matrix[i][j]
        return res

print(Solution().countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]))