from typing import List
import numpy as np

#Your runtime beats 98.24 % of python3 submissions.
#Your memory usage beats 77.13 % of python3 submissions.
#Runtime: 72 ms, faster than 87.06% of Python3 online submissions for Dungeon Game.
#Memory Usage: 14.8 MB, less than 56.74% of Python3 online submissions for Dungeon Game.
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[999999 for _ in range(n+1)] for _ in range(m + 1)]
        dp[m-1][n], dp[m][n-1] = 1,1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = max((1, min(dp[i][j+1], dp[i+1][j]) + -1*dungeon[i][j]))
        return dp[0][0]



#how are these two different? How can the bottom-up pass and this wont?
#THe i-1 and j-1th entries are conflicting in this test case.
#Unsure how a bottoms-up aproach corrects this problem. There must be a case where it won't pass
class Solution2:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[9999999 for _ in range(n+1)] for _ in range(m + 1)]
        dp[0][1], dp[1][0] = 1, 1
        for i, a in enumerate(dungeon):
            for j, b in enumerate(a):
                dp[i+1][j+1] = max(1, min(dp[i][j+1], dp[i+1][j]) - (dungeon[i][j]))
        print(np.asmatrix(dp))
        return dp[-1][-1]







s = Solution()
print(s.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))