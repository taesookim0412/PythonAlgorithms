import collections
import numpy as np
from typing import List

#45.26% Runtime
#94.89% Memory

class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        i = len(s)
        last = len(s)
        while i > 0:
            i -= 1
            if s[i] == ' ':
                last = i
                continue
            if s[i - 1] == ' ':
                res += [s[i:last]]
                last = i-1
        res += [s[:last]] if last > 0 else ''
        return ' '.join(res)[:]

s = Solution()
print(s.reverseWords("  hello world!  "))