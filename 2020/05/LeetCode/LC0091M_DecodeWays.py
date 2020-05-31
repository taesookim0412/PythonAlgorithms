class Solution:
    #Pairing fundamentals
    #Runtime: 28 ms, faster than 88.39% of Python3 online submissions for Decode Ways.
    ##Memory Usage: 14.1 MB, less than 12.00% of Python3 online submissions for Decode Ways.
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        #base case
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(1, len(s)):
            if 1 <= int(s[i]) <= 9:
                dp[i+1] = dp[i]
            if 10 <= int(s[i-1:i+1]) <= 26:
                dp[i+1] += dp[i-1]
        print(dp)
        return dp[-1]



    #Attempt at pairing:
    # def numDecodings(self, s: str) -> int:
    #     dp = [0] * (len(s) + 1)
    #     accumStr = "0"
    #     for i in range(len(s)):
    #         accumStr += s[i]
    #         if int(accumStr) > 100: accumStr = s[i]
    #         print(int(accumStr))
    #         if 1 <= int(accumStr) <= 9:
    #             dp[i+1] += dp[i] + 1
    #         elif 10 <= int(accumStr) <= 26:
    #             dp[i+1] += min(dp[i-1] + dp[i] + 1, dp[i] + 2)
    #         else:
    #             dp[i+1] = dp[i]
    #     print(dp)
    #     return dp[-1]



    #Objective: Find the total number of interpolations that a string of ascii integers can represent
    # def numDecodings(self, s: str) -> int:
    #     dp = [[0] * (len(s) + 1) for _ in range(len(s)+1)]
    #     for i in range(len(s)):
    #         accumStr = ""
    #         for j in range(i, i+2):
    #             if j >= len(s): continue
    #             accumStr += s[j]
    #             if 1 <= int(accumStr) <= 26:
    #                 dp[i+1][j+1] = max(max(dp[i][j] + 1, dp[i+1][j]+1), dp[i][j+1])
    #                 #last res addtn'l pair
    #                 #pairing is disfunctional in R^2 unless make some addtn'l assertions
    #                 #if i== len(s)-1 and j== len(s)-1: dp[i+1][j+1] += 1
    #             else:
    #                 dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    #     print(np.asmatrix(dp))
    #     return dp[-1][-1]
import numpy as np
s = Solution()
print(s.numDecodings("226") == 3)
print(s.numDecodings("12") == 2)
print(s.numDecodings("1234") == 3)
print(s.numDecodings("1212") == 5)
#20 21, 20, 2, 1 == 2
print(s.numDecodings("2021") == 2)


    #Inc: Find the total number of decodings in a string
    # def numDecodings(self, s: str) -> int:
    #     #65-A
    #     offset = 65
    #     singleDecodings = {}
    #     multiDecodings = {}
    #
    #     ctDecodings = 0
    #     passed = False
    #     for i, c in enumerate(s):
    #         if passed:
    #             passed = not passed
    #             continue
    #         critStr = str(c)
    #         if 0 < int(critStr) <= 26:
    #             self.putKey(critStr, singleDecodings)
    #             ctDecodings += 1
    #         elif i+1 < len(s):
    #             sndStr = critStr + s[i+1]
    #             if 0 < int(sndStr) <= 26:
    #                 self.putKey(sndStr, multiDecodings)
    #                 ctDecodings += 1
    #                 passed = True
    #     print(singleDecodings, multiDecodings)
    #     print(ctDecodings)
    #     return ctDecodings
    #
    #
    # def putKey(self, critStr, decodings):
    #     if critStr not in decodings:
    #         decodings[critStr] = 1
    #     else:
    #         decodings[critStr] += 1



