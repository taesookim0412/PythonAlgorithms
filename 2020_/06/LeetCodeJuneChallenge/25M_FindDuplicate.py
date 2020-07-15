from typing import List

#Runtime: 80 ms, faster than 33.43% of Python3 online submissions for Find the Duplicate Number.
#Memory Usage: 16.4 MB, less than 36.52% of Python3 online submissions for Find the Duplicate Number.
#
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast
#
#43 / 53 test cases passed.
class Solution5:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        slow=nums[0]

        return nums[fast]

s = Solution()
print(s.findDuplicate([1,3,4,2,2]))
print(s.findDuplicate([3,1,3,4,2]))
