import collections
import numpy as np
from typing import List
#Runtime: 32 ms, faster than 69.36% of Python3 online submissions for House Robber.
#Memory Usage: 13.9 MB, less than 22.68% of Python3 online submissions for House Robber.

#pretty simple some good indexing practice
#kinda just glad there are no negative numbers
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums)==1: return nums[0]
        dp = [0 for _ in range(len(nums)+1)]
        dp[1], dp[2] = nums[0], nums[1]
        for i in range(3,len(nums)+1):
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i-1]
        return max(dp[-1],dp[-2])