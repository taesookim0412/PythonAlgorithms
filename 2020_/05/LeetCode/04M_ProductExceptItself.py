# -*- coding: utf-8 -*-
#05-12-2020_
#O(n) Constant space


#Runtime: 120 ms, faster than 82.98% of Python3 online submissions for Product of Array Except Self.
#Memory Usage: 19.9 MB, less than 94.00% of Python3 online submissions for Product of Array Except Self.
#https://leetcode.com/problems/product-of-array-except-self
#Two-Pass In Place

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]
        for i in range(0, len(nums)-1):
            output.append(nums[i] * output[i])
        print(output)
        mult = 1
        idx = 1
        prevNum = 1
        for i in range(len(nums) -1, -1, -1):
            prevNum = nums[i]
            nums[i] = output[i] * mult
            mult *= prevNum
            idx += 1
        
        
        return nums
        
    def __init__(self):
        #Output:
        #[1, 2, 8, 56]
        #Intermediate
        #[1, 11, 77, 308]
        #Solution
        #[308, 154, 88, 56]
        print(self.productExceptSelf([2, 4, 7, 11]))
        print(self.productExceptSelf([1, 2,3,4]))
    
Solution()