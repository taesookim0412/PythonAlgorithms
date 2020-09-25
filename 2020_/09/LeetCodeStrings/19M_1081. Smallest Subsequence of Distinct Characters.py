import collections
import numpy as np
from typing import List


# Runtime: 32 ms, faster than 74.37% of Python3 online submissions for Smallest Subsequence of Distinct Characters.
# Memory Usage: 13.9 MB, less than 49.75% of Python3 online submissions for Smallest Subsequence of Distinct Characters.

class Solution:
    def smallestSubsequence(self, s) -> str:
        last_occurences = {s: i for i, s in enumerate(s)}
        stack = []
        for i, c in enumerate(s):
            if c in stack: continue
            while stack and stack[-1] > c and i < last_occurences[stack[-1]]:
                stack.pop()
            stack.append(c)
        return ''.join(stack)

