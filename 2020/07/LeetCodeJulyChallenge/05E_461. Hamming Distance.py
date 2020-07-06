import collections
import numpy as np
from typing import List

#8.43%
#70%
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ct = 0
        mask = 1
        for i in range(32):
            if (x&mask) != (y&mask):
                ct += 1
            mask = mask << 1
        return ct
s = Solution()
print(s.hammingDistance(1, 4))
