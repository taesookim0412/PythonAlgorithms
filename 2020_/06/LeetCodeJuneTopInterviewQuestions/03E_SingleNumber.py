from typing import List

#06-01-2020_
#Runtime: 84 ms, faster than 84.28% of Python3 online submissions for Single Number.
#Memory Usage: 16.2 MB, less than 6.56% of Python3 online submissions for Single Number.

class Solution:
    #want no extra memory usage
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        nums.sort()
        return [nums[i] for i in range(len(nums) -1, -1, -2) if nums[i-1] != nums[i]][0]

        # for i in range(len(nums) -1, -1, -2):
        #     if nums[i] != nums[i-1]:
        #         return nums[i]


        #return [nums[i] for i in range(1, len(nums)+1, 2) if nums[i] != nums[i-1]]

#print(Solution().singleNumber([2, 2, 1]))
print(Solution().singleNumber([2, 2, 1, 1, 1]))

print(Solution().singleNumber([4, 1, 2, 1, 2]))