import collections
import numpy as np
from typing import List

# Runtime: 40 ms, faster than 36.23% of Python3 online submissions for Binary String With Substrings Representing 1 To N.
# Memory Usage: 13.9 MB, less than 51.61% of Python3 online submissions for Binary String With Substrings Representing 1 To N.

class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for x in range(1, N + 1):
            bin_R = bin(x)[2:]
            if S.find(bin_R) == -1:
                return False
        return True

s = Solution()
print(s.queryString("0110", 3))
print(s.queryString("0110", 4))