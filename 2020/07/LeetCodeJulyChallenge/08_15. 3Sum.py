import collections
import numpy as np
from typing import List


#dang i tried this a year ago, got TLE
#tried this again, still got TLE.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sums = collections.defaultdict(list)
        res = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                summation = nums[i] + nums[j]
                sums[summation] += i, j,
        for i in range(len(nums)):
            sumList = sums[-nums[i]]
            for j in range(0,len(sumList), 2):
                if i != sumList[j] and i != sumList[j+1] and sumList[j] != sumList[j+1]:
                    res.update([tuple(sorted([nums[i], nums[sumList[j]], nums[sumList[j+1]]]))])
        return list(res) if len(res) > 0 else []


        # for i in range(nums):
        #     diff = -nums[i]
        #     if sums[diff]:
        #         res.append([i, *sums[diff]])
        #     sums[diff] +=
        print(sums)
s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([0,0,0]))
print(s.threeSum([0,0]))