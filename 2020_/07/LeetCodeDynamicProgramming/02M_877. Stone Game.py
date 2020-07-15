import collections
import numpy as np
from typing import List

#Runtime: 56 ms, faster than 61.05% of Python3 online submissions for Stone Game.
#Memory Usage: 13.6 MB, less than 99.37% of Python3 online submissions for Stone Game.
#The objective of the game is to end with the most stones
#Here's my post:
#https://leetcode.com/problems/stone-game/discuss/720080/Python-double-pass-DP
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        for h in range(2):
            p2 = piles.copy()
            dp = [0 for _ in range(len(piles)+2)]
            dp[2] = p2.pop(-h)
            for i in range(1, len(p2)):
                if p2[-1] >= p2[0]:
                    dp[i+2] = dp[i] + p2[-1]
                    p2.pop(-1)
                    continue
                dp[i+2] = dp[i] + p2[0]
                p2.pop(0)
            print(dp)
            if dp[-2] > dp[-1]: return True
        return False



s = Solution()
print(s.stoneGame([5,3,4,5]))
print(s.stoneGame([3,2,10,4]))