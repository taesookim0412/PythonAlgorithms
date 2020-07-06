import collections
import numpy as np
from typing import List

# Runtime: 220 ms, faster than 26.95% of Python3 online submissions for Permutations II.
# Memory Usage: 14.1 MB, less than 27.51% of Python3 online submissions for Permutations II.

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def backtrack(path, size):
            if size == 1:
                res.update([tuple(path)])
                return
            for i in range(size):
                backtrack(path, size-1)
                if size&1:
                    path[0], path[size-1] = path[size-1], path[0]
                else:
                    path[i], path[size-1] = path[size-1], path[i]
        backtrack(nums, len(nums))
        return list(res)

s = Solution()
print(s.permuteUnique([1,1,2]))