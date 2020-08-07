import collections
import numpy as np
from typing import List

#Runtime: 212 ms, faster than 44.79% of Python3 online submissions for Count Binary Substrings.
#Memory Usage: 14.2 MB, less than 77.78% of Python3 online submissions for Count Binary Substrings.

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        dp = [1]
        for i in range(1,len(s)):
            if s[i-1] != s[i]:
                dp.append(1)
            else:
                dp[-1] += 1
        res = 0
        for i in range(1,len(dp)):
            res += min(dp[i-1], dp[i])
        return res