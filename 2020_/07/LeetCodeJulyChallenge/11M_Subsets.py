import collections
import numpy as np
from typing import List


#20%
#76%
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path, idx):
            res.append(path)
            for i in range(idx, len(nums)):
                backtrack([*path, nums[i]], i+1)
        backtrack([], 0)
        return res

s = Solution()
print(s.subsets([1,2,3]))