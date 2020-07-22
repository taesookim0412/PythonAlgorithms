import collections
import numpy as np
from typing import List

#https://leetcode.com/problems/divisor-game/discuss/748412/python-dynamic-programming
#Runtime: 16 ms, faster than 99.90% of Python3 online submissions for Divisor Game.
#Memory Usage: 13.7 MB, less than 91.08% of Python3 online submissions for Divisor Game.

class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [0 for i in range(N)]
        dp[0]=1
        for i in range(3,N+1):
            K = i & 1
            #Odd: 1, Even:0
            K -= 2
            #Odd: -1, Even: -2
            dp[i-1] = -(dp[i+K]-1)
            print(i,i+K)
        print(dp)
        return dp[-1] == 0
s = Solution()
print(s.divisorGame(3))
print(s.divisorGame(5))
print(s.divisorGame(6))
print(s.divisorGame(7))
print(s.divisorGame(22))