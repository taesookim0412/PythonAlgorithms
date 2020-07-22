import collections
import numpy as np
from typing import List


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

#19
#61


class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = l+(r-l)//2
            res = guess(mid)
            if res == 0:
                return mid
            if res == 1:
                l = mid + 1
            elif res == -1:
                r = mid - 1
        return -1