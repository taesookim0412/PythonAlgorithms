#Runtime: 128 ms, faster than 59.48% of Python3 online submissions for Contains Duplicate.
#Memory Usage: 19.3 MB, less than 34.06% of Python3 online submissions for Contains Duplicate.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
        #nums.sort();return True if len([i for i in range(1, len(nums)) if nums[i] == nums[i-1]]) > 0 else False