from typing import List
import sys


# 05-20-2020_
# Runtime: 60 ms, faster than 93.54% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 14.8 MB, less than 5.69% of Python3 online submissions for Maximum Subarray.
# TODO: Revisit for Divide and Conquer approach, busy at the moment

class Solution:
    # dp array: O(n) runtime, O(n) extra space
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        maxNeg = nums[0]
        maxNum = 0
        for i, a in enumerate(nums):
            num = dp[i - 1] + a
            dp[i] = num if num > 0 else 0
            if dp[i] > maxNum: maxNum = dp[i]
            if maxNum == 0:
                if nums[i] > maxNeg: maxNeg = nums[i]

        return maxNum if maxNum != 0 else maxNeg

    # O(n^2) space and runtime
    def maxSubArrayMatrix(self, nums: List[int]) -> int:
        dp = [[0] * (len(nums) + 1) for _ in range(len(nums) + 1)]
        max = -sys.maxsize
        # cands = []
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                num = dp[i][j - 1] + nums[j]
                dp[i][j] = num
                # if num >= max: cands.append(dp[i])
                if num >= max: max = num
        return max

    def __init__(self):
        print(self.maxSubArray([1, -1, 4, -2]))
        print(self.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
        print(self.maxSubArray([-2, -1]))


Solution()
