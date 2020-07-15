from typing import List
#Runtime: 176 ms, faster than 59.71% of Python3 online submissions for Majority Element.
#Memory Usage: 15.1 MB, less than 75.23% of Python3 online submissions for Majority Element.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        #xd
        nums.sort()
        for i in range(len(nums)):
            if nums[(i + (n//2)) % n] == nums[i]:
                return nums[i]


print(Solution().majorityElement([3,2,3]))