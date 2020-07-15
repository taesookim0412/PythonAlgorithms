import collections
import numpy as np
from typing import List

# Runtime: 112 ms, faster than 5.69% of Python3 online submissions for Min Cost Climbing Stairs.
# Memory Usage: 14 MB, less than 36.51% of Python3 online submissions for Min Cost Climbing Stairs.

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for _ in range(len(cost)+1)]
        dp[1] = cost[0]
        dp[2] = cost[1]
        for i in range(2, len(cost)):
            dp[i+1] = min(dp[i-1] + cost[i], dp[i] + cost[i])
        return min(dp[-1], dp[len(dp)-2])
s = Solution()
print(s.minCostClimbingStairs([1,2,1,2]))
print(s.minCostClimbingStairs([10,15,20]))
print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
