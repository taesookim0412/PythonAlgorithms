import collections
import numpy as np
from typing import List


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        pass

#GIven two binary strings return a binary sum (as a string)

#Runtime: 24 ms, faster than 98.39% of Python3 online submissions for Add Binary.
#Memory Usage: 13.6 MB, less than 93.48% of Python3 online submissions for Add Binary.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        return str(bin(a+b))[2:]

s = Solution()
print(s.addBinary("11", "1"))
