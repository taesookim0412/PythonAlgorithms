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