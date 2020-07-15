from typing import List

#Runtime: 208 ms, faster than 60.71% of Python3 online submissions for Coin Change 2.
#Memory Usage: 14 MB, less than 65.82% of Python3 online submissions for Coin Change 2.

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for i in coins:
            for j in range(1, amount+1):
                if j >= i:
                    dp[j] += dp[j-i]
        print(dp)
        return dp[amount]

sol = Solution()
print(sol.change(4, [1, 2, 5]))