import collections
import numpy as np
from typing import List

#Runtime: 148 ms, faster than 36.92% of Python3 online submissions for Range Sum Query - Immutable.
#Memory Usage: 17.5 MB, less than 27.65% of Python3 online submissions for Range Sum Query - Immutable.

class NumArray:

    def __init__(self, nums: List[int]):
        if not nums: return None
        self.dp = [0 for _ in range(len(nums)+1)]
        dp = self.dp
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = dp[i-1] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        dp = self.dp
        return dp[j]-(dp[i-1] if i > 0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

s = NumArray([1,2,3])
print(s.sumRange(1, 2))
