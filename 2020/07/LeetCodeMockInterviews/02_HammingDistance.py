import collections
import numpy as np
from typing import List

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        mask, ct = 1, 0
        for i in range(32):
            if x&mask != y&mask:
                ct += 1
            mask <<= 1
        return ct