import collections
import numpy as np
from typing import List

#Runtime: 124 ms, faster than 79.21% of Python3 online submissions for Minimum Falling Path Sum.
#Memory Usage: 14.1 MB, less than 95.21% of Python3 online submissions for Minimum Falling Path Sum.

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        m = len(A[0])
        n = len(A)
        dp = [0 for _ in range((m * n))]
        ctr = 0
        for i in range(n):
            for j in range(m):
                if i == 0:
                    dp[ctr] = A[i][j]
                    ctr += 1
                else:
                    l = j - 1 if j > 0 else 0
                    r = j + 1 if j < m - 1 else m - 1
                    prevRow = i - 1 if i > 0 else 0
                    l += (prevRow*m)
                    r += prevRow*m
                    dp[ctr] = min(dp[l:r + 1]) + A[i][j]
                    ctr += 1
        total = m * n
        return min(dp[total - m:])

s = Solution()
print(s.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))
print(s.minFallingPathSum([[-80,-13,22],[83,94,-5],[73,-48,61]]))