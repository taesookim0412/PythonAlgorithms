import collections
import numpy as np
from typing import List

#95.46%

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        if nums[-1] > nums[0]: return nums[0]
        while l < r:
            mid = l+(r-l)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                l = mid + 1
            # or elif nums[mid] < nums[-1]:
            elif nums[mid] < nums[0]:
                r = mid
            elif nums[mid]==nums[-1]:
                r-=1
                if nums[r-1] > nums[r] < nums[r+1]:
                    return nums[r]
            elif nums[mid]==nums[0]:
                l+=1
        return nums[l]


s = Solution()
print(s.findMin([10, 1, 10, 10, 10]))
print(s.findMin([3,3,3,1]))
print(s.findMin([3,3,3,3,3,3,3,3,1,3]))