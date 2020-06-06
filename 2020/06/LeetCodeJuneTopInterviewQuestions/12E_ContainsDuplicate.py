#Runtime: 136 ms, faster than 24.97% of Python3 online submissions for Contains Duplicate.
#Memory Usage: 19 MB, less than 94.29% of Python3 online submissions for Contains Duplicate.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort();return True if len([i for i in range(1, len(nums)) if nums[i] == nums[i-1]]) > 0 else False