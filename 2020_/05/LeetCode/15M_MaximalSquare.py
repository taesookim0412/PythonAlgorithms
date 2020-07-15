from typing import List
import numpy as np

#05-26-2020_
#Runtime: 212 ms, faster than 47.24% of Python3 online submissions for Maximal Square.
#Memory Usage: 14.4 MB, less than 9.09% of Python3 online submissions for Maximal Square.

#Yep saw the dp didn't quite get there fully.
#Hopefully can just finish the 30day challenge this month and switch onto
#dynamic programming exercises.

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #dp solution
        #print(np.matrix(matrix))
        if len(matrix) == 0 or len(matrix[0]) == 0: return 0
        maxsqrlen = 0
        dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == "1":
                    dp[i+1][j+1] = int(min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1)
                    maxsqrlen = max(maxsqrlen, dp[i+1][j+1])
                    #print(np.matrix(dp))

        #print(np.matrix(dp))
        return maxsqrlen * maxsqrlen

a = Solution()
print(a.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(a.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(a.maximalSquare([]))