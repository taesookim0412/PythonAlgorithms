import collections
import numpy as np
from typing import List


#Such that min(S) + max(S) <= k

class Solution:
    def numberOfSubsetsn2(self, nums, k):
        nums.sort()
        ct = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] > k:
                    break
                if nums[i] + nums[j] <= k:
                    ct += 2**(j-1-i if j > i else 0)
        return ct

    def numberOfSubsets(self, nums, k):
        nums.sort()
        lo = 0
        hi = len(nums)-1
        res = 0
        while lo < hi:
            total = nums[lo] + nums[hi]
            if total <= k:
                res = 2 ** (hi+1-lo)
                break
            if total > k:
                hi-=1
        for i in range(lo, hi+1):
            for j in range(i, hi+1):
                if nums[i] + nums[j] > k:
                    res -= 2 **(j-i-1 if j > i else 0)
        return res - 1
#2*2
s= Solution()
#5
print(s.numberOfSubsets([2,4,5,7],8))

print(s.numberOfSubsets([2,4,2,5,7],10))

print(s.numberOfSubsets([1,4,3,2],8))

print(s.numberOfSubsets([1,2,3,4],5))

print(s.numberOfSubsetsn2([1,2,3,4],5))

print(s.numberOfSubsetsn2([2,4,5,7],8))

print(s.numberOfSubsetsn2([2,4,2,5,7],10))

print(s.numberOfSubsetsn2([1,4,3,2],8))

#[1,2,3,4]
#k = 6