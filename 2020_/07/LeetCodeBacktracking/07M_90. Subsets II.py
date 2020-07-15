import collections
import numpy as np
from typing import List




# Runtime: 40 ms, faster than 92.00% of Python3 online submissions for Subsets II.
# Memory Usage: 14.2 MB, less than 7.83% of Python3 online submissions for Subsets II.
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        def backtrack(path, j):
            res.append(path)
            for i in range(j, n):
                if i > j and nums[i] == nums[i-1]:
                    continue
                backtrack([*path, nums[i]], i+1)
        #got a 32 with path=()
        backtrack([], 0)
        return res

#
# Runtime: 44 ms, faster than 40.59% of Python3 online submissions for Subsets II.
# Memory Usage: 14.2 MB, less than 13.91% of Python3 online submissions for Subsets II.
class Solution1:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        def backtrack(path, j):
            res.append(path)
            for i in range(j+1, n):
                if j+1 < i and nums[i] == nums[i-1]:
                    continue
                backtrack([*path, nums[i]], i)
        backtrack([], -1)
        return res

#
# Runtime: 48 ms, faster than 31.55% of Python3 online submissions for Subsets II.
# Memory Usage: 14 MB, less than 57.10% of Python3 online submissions for Subsets II.
class Solution2:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)
        nums.sort()
        def backtrack(path, j):
            if path not in res:
                res.update([path])
            for i in range(j+1, n):
                backtrack((*path, nums[i]), i)
        backtrack((), -1)
        return list(res)

s = Solution()
print(s.subsetsWithDup([4,4,4,1,4]))
