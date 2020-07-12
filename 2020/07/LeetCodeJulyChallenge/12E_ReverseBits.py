import collections
import numpy as np
from typing import List

#43%,11%
class Solution:
    def reverseBits(self, n: int) -> int:
        res, power = 0, 31
        while n:
            res += (n&1) << power
            n = n >> 1
            power -= 1
        return res