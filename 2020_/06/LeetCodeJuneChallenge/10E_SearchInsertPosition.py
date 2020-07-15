from typing import List
#Runtime: 28 ms, faster than 79.72% of Python3 online submissions for Unique Paths.
#Memory Usage: 13.8 MB, less than 52.20% of Python3 online submissions for Unique Paths.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] > target or nums[i] == target: return i
        return len(nums)