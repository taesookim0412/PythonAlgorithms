import collections
import numpy as np
from typing import List

#88%
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1 : return True
        l, r = 0, num
        while l < r:
            mid = l + (r-l)//2
            number = mid * mid
            if number == num:
                return True
            elif number < num:
                l = mid + 1
            else:
                r = mid
        return False