import collections
import numpy as np
from typing import List

#Runtime: 24 ms, faster than 94.33% of Python3 online submissions for Complex Number Multiplication.
#Memory Usage: 13.9 MB, less than 37.19% of Python3 online submissions for Complex Number Multiplication.
class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a, b = a[:-1], b[:-1]
        a = list(map(int, a.split('+')))
        b = list(map(int, b.split('+')))
        F = a[0] * b[0]
        O = a[0] * b[1]
        I = a[1] * b[0]
        L = -(a[1] * b[1])
        real = str(F + L)
        complex = str(O+I) + "i"
        return f"{real}+{complex}"

s = Solution()
print(s.complexNumberMultiply("1+1i", "1+1i"))