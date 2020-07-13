import collections
import numpy as np
from typing import List

# Given a non-negative integer num, return the number of steps to reduce it to zero.
# If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

#Runtime: 52 ms, faster than 9.19% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
#Memory Usage: 14 MB, less than 5.18% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.

class Solution:
    def numberOfSteps(self, num: int) -> int:
        ct = 0
        while num > 0:
            if num&1:
                num -= 1
                ct += 1
            elif not num&1:
                num >>= 1
                ct += 1
        return ct

s = Solution()
print(s.numberOfSteps(14))
print(s.numberOfSteps(123))