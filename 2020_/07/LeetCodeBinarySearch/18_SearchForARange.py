import collections
import numpy as np
from typing import List

#92.26%

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0 , len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[l] == nums[r] == target:
                return [l, r]
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[l] != target:
                l += 1
            elif nums[r] != target:
                 r-= 1
        return [-1, -1]
s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))
print(s.searchRange([1,2,3,5,6],4))
print(s.searchRange([1,3],1))
print(s.searchRange([0],0))
print(s.searchRange([2,2],1))
print(s.searchRange([5,7,7,8,8,10],6))
print(s.searchRange([1,2], 0))
print(s.searchRange([1,2,3],2))