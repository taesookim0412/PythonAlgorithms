from typing import List

#05-29-2020_
#Runtime: 52 ms, faster than 21.90% of Python3 online submissions for Search in Rotated Sorted Array.
#Memory Usage: 14.2 MB, less than 6.29% of Python3 online submissions for Search in Rotated Sorted Array.
#https://leetcode.com/problems/search-in-rotated-sorted-array
#Divide And Conquer Solution

class Solution:
    idx = None
    target = 0
    def search(self, nums: List[int], target: int) -> int:
        self.target = target
        self.idx = None
        md = len(nums)//2
        L, R = nums[:md], nums[md:]
        self.dac(L, 0)
        self.dac(R, md)
        if self.idx is None: return -1
        return self.idx

    def dac(self, nums: List[int], idx: int):
        if len(nums) > 1:
            md = len(nums)//2
            L, R = nums[:md], nums[md:]
            self.dac(L, idx)
            self.dac(R, idx + md)
        if len(nums) == 1:
            if nums[0] == self.target:
                self.idx = idx




    def __init__(self):
        print(self.search([1, 2, 3, 4, 5, 6], 2))
        print(self.search([0], 0))
        print(self.search([4,5,6,7,0,1,2], 3))
Solution()