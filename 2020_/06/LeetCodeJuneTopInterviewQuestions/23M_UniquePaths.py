import numpy as np

#Runtime: 28 ms, faster than 79.72% of Python3 online submissions for Unique Paths.
#Memory Usage: 13.8 MB, less than 52.20% of Python3 online submissions for Unique Paths.
#dp solution

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(m-1):
            for j in range(n-1):
                dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j]
        print(np.matrix(dp))
        return dp[-1][-1]
sol = Solution()
print(sol.uniquePaths(3, 7))