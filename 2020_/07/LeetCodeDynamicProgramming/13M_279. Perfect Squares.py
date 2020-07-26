import collections
import numpy as np
from typing import List

#585/588 TLE

class Solution:
    def numSquares(self, n: int) -> int:
        memo = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            minFound = 999999
            j = 1
            while j*j <= i:
                minFound = min(memo[i-j*j] +1, minFound)
                j+=1
            memo[i] = minFound
        return memo[-1]

s = Solution()
print(s.numSquares(12))