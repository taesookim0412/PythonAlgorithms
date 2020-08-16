import collections
import numpy as np
from typing import List

#inaccurate description, incorrect test case

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        z = k
        res = []
        reversedPart = []
        for i in range(len(s)):
            if i % 2000 < k:
                reversedPart += s[i],
            else:
                if i % 2000 == k:
                    res += reversedPart[::-1]
                res += s[i],
        return ''.join(res)
