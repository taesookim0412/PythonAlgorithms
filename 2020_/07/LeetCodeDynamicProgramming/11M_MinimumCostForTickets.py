import collections
import numpy as np
from typing import List

#TODO: Window variant

#Runtime: 52 ms, faster than 52.18% of Python3 online submissions for Minimum Cost For Tickets.
#Memory Usage: 14.3 MB, less than 15.83% of Python3 online submissions for Minimum Cost For Tickets.

class Solution2:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        daysSet = set(days)
        memo = [None for _ in range(366)]
        def dp(i):
            if i > 365: return 0
            if memo[i] is not None:
                return memo[i]
            if i in daysSet:
                res = min(dp(i+1) + costs[0], dp(i+7) + costs[1], dp(i+30) + costs[2])
            else:
                res = dp(i+1)
            memo[i] = res
            return memo[i]
        return dp(1)

s = Solution()
print(s.mincostTickets([1,4,6,7,8,20],[2,7,15]))





















class Solution5:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        daysSet = set(days)
        memo = [0 for _ in range(366)]

        def dp(i):
            if i > 365: return 0
            if memo[i] != 0:
                return memo[i]
            if i in daysSet:
                ans = min(dp(i + 1) + costs[0], dp(i + 7) + costs[1], dp(i + 30) + costs[2])
            else:
                ans = dp(i+1)
            memo[i] = ans
            return ans
        print(dp(1))
        print(memo)
s = Solution5()
print(s.mincostTickets([1,4,6,7,8,20],[2,7,15]))