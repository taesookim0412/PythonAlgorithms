import numpy as np
#56.82
#46.23
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(n-1):
            for j in range(m-1):
                dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j]
        print(np.asmatrix(dp))
        return dp[-1][-1]







#Woops this is shortest path.
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[i-1 for i in range(m+1)] for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j]) + 1
        print(np.asmatrix(dp))
        return dp[-1][-1]


s = Solution()
print(s.uniquePaths(7, 3))