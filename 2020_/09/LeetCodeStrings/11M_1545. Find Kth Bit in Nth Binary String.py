import collections
import numpy as np
from typing import List

# Runtime: 3208 ms, faster than 8.88% of Python3 online submissions for Find Kth Bit in Nth Binary String.
# Memory Usage: 56.1 MB, less than 5.01% of Python3 online submissions for Find Kth Bit in Nth Binary String.

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        for i in range(n-1):
            inverted_s = ''.join(list(map(lambda x: str(-(int(x)-1)), s)))
            s += "1" + inverted_s[::-1]
        return s[k-1]