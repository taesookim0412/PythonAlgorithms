from typing import List

#Runtime: 144 ms, faster than 57.21% of Python3 online submissions for Missing Number.
#Memory Usage: 15 MB, less than 84.12% of Python3 online submissions for Missing Number.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums2 = [False for _ in range(len(nums) +1)]
        for i in range(len(nums)):
            nums2[nums[i]] = True
        return [i for i in range(len(nums2)) if nums2[i] == False][0]

#Runtime: 144 ms, faster than 57.21% of Python3 online submissions for Missing Number.
#Memory Usage: 15.6 MB, less than 6.32% of Python3 online submissions for Missing Number.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsSet = set(nums)
        for i in range(len(nums)+1):
            if i not in numsSet:
                return i


print(Solution().missingNumber([3,0,1]))
print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))