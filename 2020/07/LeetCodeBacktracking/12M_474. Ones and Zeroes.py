import collections
import numpy as np
from typing import List

#bruh
class Solution:
    def findMaxForm(self, strs: List[str], m, n) -> int:
        dp = [[ 0 for _ in range(n+1)] for _ in range(m+1)]
        for s in strs:
            zeros, ones = s.count('0'), s.count('1')
            for i in range(m, zeros -1, -1):
                for j in range(n, ones -1, -1):
                    dp[i][j] = max(1 + dp[i-zeros][j-ones], dp[i][j])
        print(np.asmatrix(dp))
        return dp[-1][-1]




















#Time Limit Exceeded (Knapsack Approach)
#9
#80

class Solution2:
    def findMaxForm(self, strs: List[str], m, n) -> int:
        maxCt = [0]
        strsZeros = collections.defaultdict(int)
        strsOnes = collections.defaultdict(int)
        for i in range(len(strs)):
            strsZeros[i] += strs[i].count('0')
            strsOnes[i] += strs[i].count('1')
        def backtrack(path, j, oneCt, zeroCt):
            if oneCt > n or zeroCt > m:
                return
            if len(path) > maxCt[-1] and oneCt <= n and zeroCt <= m:
                maxCt[-1] = len(path)
            for i in range(j, len(strs)):
                temp_1Ct = strsOnes[i]
                temp_0Ct = strsZeros[i]
                backtrack([*path, strs[i]],
                          i+1,
                          oneCt + temp_1Ct,
                          zeroCt + temp_0Ct)
        backtrack([], 0, 0, 0)
        return maxCt[-1]

s = Solution()
#4
print(s.findMaxForm(["10","0001","111001","1","0"],
5,
3))
#3
print(s.findMaxForm(["10","0001","111001","1","0"],
3,
4))
print(s.findMaxForm(["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"]
,9
,80))