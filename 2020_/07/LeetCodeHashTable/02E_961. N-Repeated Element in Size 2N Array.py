import collections
import numpy as np
from typing import List

# Runtime: 296 ms, faster than 26.04% of Python3 online submissions for N-Repeated Element in Size 2N Array.
# Memory Usage: 15.2 MB, less than 23.62% of Python3 online submissions for N-Repeated Element in Size 2N Array.

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        n = len(A)//2
        cts = collections.Counter(A)
        return [x for x, val in cts.items() if val==n][-1]