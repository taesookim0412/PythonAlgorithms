import collections
import numpy as np
from typing import List

#Runtime: 60 ms, faster than 6.67% of Python3 online submissions for Find N Unique Integers Sum up to Zero.
#Memory Usage: 14 MB, less than 40.03% of Python3 online submissions for Find N Unique Integers Sum up to Zero.
class Solution:
    def sumZero(self, n: int) -> List[int]:
        diff = 0
        res = []

        for i in range(n-1):
            res += i,
            diff += i
        res += -diff,
        return res