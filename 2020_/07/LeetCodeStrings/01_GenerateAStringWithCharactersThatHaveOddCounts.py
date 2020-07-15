import collections
import numpy as np
from typing import List

# Runtime: 100 ms, faster than 5.50% of Python3 online submissions for Generate a String With Characters That Have Odd Counts.
# Memory Usage: 29 MB, less than 5.27% of Python3 online submissions for Generate a String With Characters That Have Odd Counts.

class Solution:
    def generateTheString(self, n: int) -> str:
        even = -((n%2)-1)
        res = []
        for i in range(n - even):
            res.append("s")
        if even:
            res.append("t")
        return ''.join(res)