from typing import List

#Floyd's Algorithm
#https://en.wikipedia.org/wiki/The_Tortoise_and_the_Hare
#Runtime: 132 ms, faster than 10.73% of Python3 online submissions for Find the Duplicate Number.
#Memory Usage: 16.5 MB, less than 20.03% of Python3 online submissions for Find the Duplicate Number.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast
        

sol = Solution()
print(sol.findDuplicate([1, 2, 3, 4 ,2]))