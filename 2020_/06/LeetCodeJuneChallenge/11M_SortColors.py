from typing import List

#Runtime: 36 ms, faster than 41.78% of Python3 online submissions for Sort Colors.
#Memory Usage: 13.7 MB, less than 85.75% of Python3 online submissions for Sort Colors.

#https://en.wikipedia.org/wiki/Dutch_national_flag_problem
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        k = len(nums) - 1
        while i <= k:
            num = nums[i]
            if num == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j+=1
            elif num == 2:
                nums[i], nums[k] = nums[k], nums[i]
                k-=1
                i-=1
            i+=1
        return nums

print(Solution().sortColors([2, 2, 1, 1, 0]))