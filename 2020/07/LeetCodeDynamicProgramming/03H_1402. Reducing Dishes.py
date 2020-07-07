import collections
import numpy as np
from typing import List

for i in range(10):
    print(i&1)
    print((i+1)&1)



# class Solution:
#     def maxSatisfaction(self, satisfaction: List[int]) -> int:
#         dp = [[0 for _ in range(len(satisfaction)+1)] for _ in range(2)]
#         satisfaction.sort()
#         for i in range(len(satisfaction)):
#             for j in range(len(satisfaction)):
#                 dp[i&1][j+1] = dp[(i-1)&1][j] + (i-1)&1 * satisfaction[j]
#                 if j == len(satisfaction)-1:
#                     dp[(i+1)&1][j+1] = max(dp[i&1][j] + (i+1)&1 * satisfaction[j], dp[i&1][j+1])
#         print(dp)
#         return dp[-1][-1] if dp[-1][-1] > 0 else 0


#Problem 1: Max of a negative number
#Problem 2: Should terminate when reaches max
#
#Runtime: 956 ms, faster than 5.10% of Python3 online submissions for Reducing Dishes.
#Memory Usage: 23.6 MB, less than 5.33% of Python3 online submissions for Reducing Dishes.

#(i+1)&1: i == 0: 0

#Runtime: 792 ms, faster than 5.03% of Python3 online submissions for Reducing Dishes.
#Memory Usage: 14 MB, less than 24.16% of Python3 online submissions for Reducing Dishes.
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        dp = [[0 for _ in range(len(satisfaction)+1)] for _ in range(2)]
        satisfaction.sort()
        for i in range(len(satisfaction)):
            for j in range(len(satisfaction)):
                dp[(i+1)&1][j+1] = dp[i&1][j] + (i+1) * satisfaction[j]
                if j == len(satisfaction)-1:
                    dp[(i+1)&1][j+1] = max(dp[i&1][j] + (i+1) * satisfaction[j], dp[i&1][j+1])
        res = dp[len(satisfaction)&1][-1]
        return res if res > 0 else 0



class Solution2:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        dp = [[0 for _ in range(len(satisfaction)+1)] for _ in range(len(satisfaction)+1)]
        satisfaction.sort()
        res = []
        for i in range(len(satisfaction)):
            for j in range(len(satisfaction)):
                dp[i+1][j+1] = dp[i][j] + (i+1) * satisfaction[j]
                if j == len(satisfaction)-1:
                    dp[i+1][j+1] = max(dp[i][j] + (i+1) * satisfaction[j], dp[i][j+1])
        return dp[-1][-1] if dp[-1][-1] > 0 else 0

s = Solution2()
#14
print(s.maxSatisfaction([-1,-8,0,5,-7]))
#55
print(s.maxSatisfaction([1,2,3,4,5]))
print(s.maxSatisfaction([1,2,3,4,5,6]))