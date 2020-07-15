import collections
import numpy as np
from typing import List

# Runtime: 348 ms, faster than 17.40% of Python3 online submissions for Binary Search.
# Memory Usage: 15 MB, less than 56.62% of Python3 online submissions for Binary Search.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid -1
            else: left = mid + 1
        return -1
s = Solution()
#$
print(s.search([-1,0,3,5,9,12],9))
#1
print(s.search([-1,0,3,5,9,12],0))
