from typing import List


#Runtime: 120 ms, faster than 9.62% of Python3 online submissions for Best Time to Buy and Sell Stock.
#Memory Usage: 15.2 MB, less than 41.68% of Python3 online submissions for Best Time to Buy and Sell Stock.

#O(n)
#It works because it's one pass.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 999999
        maxProfit = 0
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            else:
                maxProfit = max(prices[i] - minPrice, maxProfit)
        return maxProfit

#TLE
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                diff = prices[j] - prices[i]
                if diff > maxProfit: maxProfit = diff
        #print(np.asmatrix(dp))
        return maxProfit

#199/200
#OMG MY FIRST STRAIGHT SHOT DP SOLUTION!!!
#except time limit exceeded cus it's n^2
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0 for _ in range(len(prices)+1)] for _ in range(len(prices)+1)]
        for i in range(len(prices)):
            for j in range(len(prices)):
                if j > i:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], prices[j]-prices[i])
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        #print(np.asmatrix(dp))
        return dp[-1][-1]
import numpy as np
s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))