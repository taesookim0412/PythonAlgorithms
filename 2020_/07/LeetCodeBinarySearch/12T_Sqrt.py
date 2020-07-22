import collections
import numpy as np
from typing import List
#31.60%
#70%
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        while l <= r:
            mid = l + (r - l) // 2
            sqrd = mid * mid
            if sqrd == x:
                return mid
            if sqrd < x:
                l = mid + 1
            else:
                r = mid - 1
        return l - 1

s = Solution()
print(s.mySqrt(4))
print(s.mySqrt(8))