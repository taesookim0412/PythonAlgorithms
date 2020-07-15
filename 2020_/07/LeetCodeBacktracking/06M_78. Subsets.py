import collections
import numpy as np
from typing import List
import time


#24ms, faster than 98.72%
class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def backtrack(path, j):
            if path not in res:
                res.update([path])
            for i in range(j+1, len(nums)):
                backtrack((*path, nums[i]), i)
        backtrack((),-1)
        return list(res)

#36ms
class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def backtrack(path, j):
            res.update([path])
            for i in range(j+1, len(nums)):
                backtrack((*path, nums[i]), i)
        backtrack((),-1)
        return list(res)

# Runtime: 64 ms, faster than 5.25% of Python3 online submissions for Subsets.
# Memory Usage: 14 MB, less than 63.34% of Python3 online submissions for Subsets.
class Solution3:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def backtrack(path, j):
            res.update([tuple(path)])
            for i in range(j+1, len(nums)):
                backtrack([*path, nums[i]], i)
        backtrack([],-1)
        return list(res)

s = Solution2()
print(Solution2().subsets([1,2,3]))
