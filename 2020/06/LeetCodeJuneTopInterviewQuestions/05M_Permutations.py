from typing import List
#Runtime: 36 ms, faster than 88.86% of Python3 online submissions for Permutations.
#Memory Usage: 14.1 MB, less than 5.36% of Python3 online submissions for Permutations.
#https://en.wikipedia.org/wiki/Heap%27s_algorithm
#Refer to the proof
#If the proof doesn't make sense then
#here dont you understand binary

#1,2,3,4,5 ... Original Array
# 4,1,2,3,5 ... 1st iteration (Permute subset/Rotate subset)
# 5,1,2,3,4 ... 1st iteration (Swap)
# 3,5,1,2,4 ... 2nd iteration (Permute subset/Rotate subset)
# 4,5,1,2,3 ... 2nd iteration (Swap)
# 2,4,5,1,3 ... 3rd iteration (Permute subset/Rotate subset)
# 3,4,5,1,2 ... 3rd iteration (Swap)
# 1,3,4,5,2 ... 4th iteration (Permute subset/Rotate subset)
# 2,3,4,5,1 ... 4th iteration (Swap)
# 5,2,3,4,1 ... 5th iteration (Permute subset/Rotate subset)
# 1,2,3,4,5 ... 5th iteration (Swap) ... The final state of the array is in the same order as the original

#there
#Rotate And Swap

class Solution:
    perms = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.perms = []
        self.heapPermutation(nums, len(nums))
        return self.perms

    def heapPermutation(self, nums, sz):
        if sz ==1:
            self.perms.append(list(nums))
            return
        for i in range(sz):
            self.heapPermutation(nums, sz-1)

            if sz&1:
                nums[0], nums[sz-1] = nums[sz-1], nums[0]
            else:
                nums[i], nums[sz-1] = nums[sz-1], nums[i]

print(Solution().permute([1, 2, 3]))