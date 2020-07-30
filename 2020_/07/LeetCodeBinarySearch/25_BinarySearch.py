import collections
import numpy as np
from typing import List

#Accepted
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = lo+(hi-lo)//2
            if nums[mid] == target:
                return mid
            if nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1


#Fails test case [-1,0,5]
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1: return 0 if nums[-1]==target else -1
        if len(nums)==2: return nums.index(target) if target in nums else -1
        lo, hi = 0, len(nums)-1
        while lo <hi:
            mid = lo+(hi-lo)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return -1