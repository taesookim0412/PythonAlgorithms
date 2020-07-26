import collections
import numpy as np
from typing import List

#45/126

class Solution:
    def minSteps(self, n: int) -> int:
        if n <= 1: return 0
        if 2 <= n <= 3: return n
        memo = [0 for _ in range(n + 1)]
        memo[0] = 1
        memo[1] = 1
        memo[2] = 2
        memo[3] = 3

        def dp(i):
            if i == n:
                return i
            if i <= n:
                memo[i] = max(memo[i - 2] * 2, i)
                if memo[i] == n:
                    return i
                else:
                    return dp(i + 1)
        ans = dp(1)
        print(memo)
        return ans




s = Solution()
print(s.minSteps(8))