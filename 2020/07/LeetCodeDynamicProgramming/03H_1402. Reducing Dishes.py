import collections
import numpy as np
from typing import List

#Problem 1: Max of a negative number
#Problem 2: Should terminate when reaches max
#
#Runtime: 956 ms, faster than 5.10% of Python3 online submissions for Reducing Dishes.
#Memory Usage: 23.6 MB, less than 5.33% of Python3 online submissions for Reducing Dishes.
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        dp = [[0 for _ in range(len(satisfaction)+1)] for _ in range(len(satisfaction)+1)]
        satisfaction.sort()
        res = []
        for i in range(len(satisfaction)):
            for j in range(len(satisfaction)):
                if i==0:
                    dp[i+1][j+1] = satisfaction[j]
                dp[i+1][j+1] = dp[i][j] + (i+1) * satisfaction[j]
                if j == len(satisfaction)-1:
                    dp[i+1][j+1] = max(dp[i][j] + (i+1) * satisfaction[j], dp[i][j+1])
        return dp[-1][-1] if dp[-1][-1] > 0 else 0

s = Solution()
#14
print(s.maxSatisfaction([-1,-8,0,5,-7]))
#55
print(s.maxSatisfaction([1,2,3,4,5]))