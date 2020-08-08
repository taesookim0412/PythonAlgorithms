import collections
import numpy as np
from typing import List


# abc1234
# 4a1b2c3
# 1a2b3c4
# abc1
# a1bc
# If the absolute difference between the count of alphas and the count of integers is W such that 0 <= W <= 1 then we can find a permutation
# where S starts with the larger string

#Runtime: 44 ms, faster than 86.93% of Python3 online submissions for Reformat The String.
#Memory Usage: 14 MB, less than 25.03% of Python3 online submissions for Reformat The String.

class Solution:
    def reformat(self, s: str) -> str:
        alphas = []
        numbers = []
        for c in s:
            if c.isalpha():
                alphas += c,
            elif c.isnumeric():
                numbers += c,
        arrs = sorted([alphas, numbers], key=len)
        lesser = arrs[0]
        greater = arrs[1]
        absDiff = len(greater) - len(lesser)
        res = []
        if absDiff <= 1:
            for i in range(len(lesser)):
                res += greater.pop(),
                res += lesser.pop(),
            if len(greater) > 0:
                res += greater.pop(),
            return ''.join(res)
        return ""


s = Solution()
print(s.reformat("ab123"))