import collections
import numpy as np
from typing import List

#86%
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        if len(nums) == 2: return nums.index(max(nums))
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r -l ) // 2
            if nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid
        return l

class Solution2:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r -l ) // 2
            if nums[r] < nums[l]:
                while r != l :
                    if nums[r-1] > nums[r]:
                        return r-1
                    r-=1
            if nums[mid] > nums[l]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid - 1


s = Solution()
print(s.findPeakElement([1, 2, 3, 1]))
print(s.findPeakElement([1,2,1,3,5,6,4]))