import collections
import numpy as np
from typing import List


#Runtime: 44 ms, faster than 13.72% of Python3 online submissions for Guess Number Higher or Lower.
#Memory Usage: 13.8 MB, less than 70.69% of Python3 online submissions for Guess Number Higher or Lower.

class Solution:
    def guessNumber(self, n: int) -> int:
        num = 0
        lo = 0
        hi = n
        while lo <= hi:
            mid = lo + (hi-lo)//2
            num = mid
            res = guess(num)
            if res == 0: break
            elif res == -1:
                hi = mid - 1
            elif res == 1:
                lo = mid + 1
        return num


def guess(num):
    if num == 6:
        return 0
    elif num < 6:
        return 1
    return -1

s = Solution()
print(s.guessNumber(10))
print(s.guessNumber(1))