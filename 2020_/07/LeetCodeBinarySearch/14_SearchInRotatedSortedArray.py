import collections
import numpy as np
from typing import List

#31.81%
#23.86%

#Two-pointer for pivot then binary search
#Faster than merge sort thus its runtime may be faster than O(Log(N))
#TODO: BS W/O TP
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            mid_Element = nums[mid]
            print(l, r, mid_Element)

            if mid_Element == target:
                return mid
            if target > nums[r]:
                r -=1
                continue
            elif target < nums[l]:
                l +=1
                continue
            if mid_Element < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

s = Solution()
#4
print(s.search([4,5,6,7,8,1,2,3],8))