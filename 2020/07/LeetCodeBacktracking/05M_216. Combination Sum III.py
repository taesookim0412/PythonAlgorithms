import collections
import numpy as np
from typing import List

# Runtime: 48 ms, faster than 17.13% of Python3 online submissions for Combination Sum III.
# Memory Usage: 14 MB, less than 16.94% of Python3 online submissions for Combination Sum III.

class Solution:
    #k numbers, target = n
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        res = []
        def backtrack(path, j, total):
            if len(path)==k and total == target:
                res.append(path.copy())
            elif len(path)>k or total > target:
                return
            for i in range(j, 10):
                backtrack([*path, i], i+1, total + i)
        backtrack([], 1, 0)
        return res

s = Solution()
print(s.combinationSum3(3, 7))
print(s.combinationSum3(3, 9))

