import collections
import numpy as np
from typing import List
#Runtime: 84 ms, faster than 71.76% of Python3 online submissions for Sort Array By Parity.
#Memory Usage: 14.5 MB, less than 10.57% of Python3 online submissions for Sort Array By Parity.

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        evens = []
        odds = []
        for i in range(len(A)):
            if A[i] & 1:
                odds += i,
            else:
                evens += i,
        res = []
        res += [A[x] for x in evens]
        res += [A[x] for x in odds]
        return res
