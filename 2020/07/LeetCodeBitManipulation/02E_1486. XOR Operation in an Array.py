import collections
import numpy as np
from typing import List

#?
# class Solution:
#     def xorOperation(self, n, start):
#         nums = [start + (2*i) for i in range(n)]
#         for i in range(len(nums)):
#             if i == len(nums)-1: break
#             nums[i+1+((i+1)&1)] ^= nums[i+(i)&1]
#         return nums[-1]

#Runtime: 36 ms, faster than 44.96% of Python3 online submissions for XOR Operation in an Array.
#Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for XOR Operation in an Array.
class Solution2:
    def xorOperation(self, n, start):
        nums = [start + (2*i) for i in range(n)]
        for i in range(len(nums)):
            if i == len(nums)-1:
                break
            nums[i+1] ^= nums[i]
        return nums[-1]

s = Solution()
print(s.xorOperation(5, 0))
print(s.xorOperation(4,3))