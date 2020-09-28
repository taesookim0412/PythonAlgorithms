import collections
import numpy as np
from typing import List

#40ms, 29.26% faster

class Solution:
    def numSteps(self, s: str) -> int:
        n = int(s, 2)
        steps = 0
        while n != 1:
            steps += 1
            if n % 2:
                n += 1
            else:
                n = n // 2
        return steps

s = Solution()
print(s.numSteps("1101"))