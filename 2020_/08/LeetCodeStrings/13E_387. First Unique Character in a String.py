import collections
import numpy as np
from typing import List

# Runtime: 92 ms, faster than 89.26% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 14 MB, less than 40.24% of Python3 online submissions for First Unique Character in a String.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = collections.Counter(s)
        for i in range(len(s)):
            c = s[i]
            if chars[c] < 2:
                return i
        return -1