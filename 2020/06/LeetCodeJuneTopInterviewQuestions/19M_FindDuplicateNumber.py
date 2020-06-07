from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow =nums[0]
        fast = nums[slow]
        while (slow != fast):
            slow = nums[slow]
            print(f"Fast: {nums[fast]}")
            fast = nums[nums[fast]]
            print(slow)
            print(fast)
        

sol = Solution()
print(sol.findDuplicate([1, 2, 3, 4 ,2]))