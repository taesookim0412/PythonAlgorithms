import collections
import numpy as np
from typing import List


# Runtime: 972 ms, faster than 26.32% of Python3 online submissions for Count Square Submatrices with All Ones.
# Memory Usage: 15.9 MB, less than 59.33% of Python3 online submissions for Count Square Submatrices with All Ones.

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(matrix[0])+1)] for _ in range(2)]
        blankRow = [0 for _ in range(len(matrix[0])+1)]
        res = 0
        for i in range(len(matrix)):
            dp[(i+1)&1] = blankRow.copy()
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    dp[(i+1)&1][j+1] = 1 + min(dp[i&1][j], dp[i&1][j+1], dp[(i+1)&1][j])
                    res += dp[(i+1)&1][j+1]
        return res


#Runtime: 752 ms, faster than 56.70% of Python3 online submissions for Count Square Submatrices with All Ones.
#Memory Usage: 16 MB, less than 36.59% of Python3 online submissions for Count Square Submatrices with All Ones.

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(matrix[0])+1)] for _ in range(2)]
        res = 0
        for i in range(len(matrix)):
            dp[(i+1)&1] = [0 for _ in range(len(matrix[0])+1)]
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    dp[(i+1)&1][j+1] = 1 + min(dp[i&1][j], dp[i&1][j+1], dp[(i+1)&1][j])
                    res += dp[(i+1)&1][j+1]
        return res

#Runtime: 1000 ms, faster than 23.44% of Python3 online submissions for Count Square Submatrices with All Ones.
#Memory Usage: 16.1 MB, less than 17.57% of Python3 online submissions for Count Square Submatrices with All Ones.
class Solution2:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    dp[i+1][j+1] = 1 + min(dp[i][j], dp[i][j+1], dp[i+1][j])
                    res += dp[i+1][j+1]
        print(np.asmatrix(dp))
        return res

s= Solution2()
print(s.countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]))
#13
print(s.countSquares([[0,1,1,1],[1,1,0,1],[1,1,1,1],[1,0,1,0]]))
s= Solution()
print(s.countSquares([[0,1,1,1],[1,1,0,1],[1,1,1,1],[1,0,1,0]]))
