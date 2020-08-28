import collections
import numpy as np
from typing import List

#Runtime: 136 ms, faster than 88.08% of Python3 online submissions for Check If a String Can Break Another String.
#Memory Usage: 16.3 MB, less than 37.20% of Python3 online submissions for Check If a String Can Break Another String.

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        def canBreak(s1, s2):
            for i in range(len(s2)):
                if s1[i] > s2[i]:
                    return False
            return True
        return canBreak(s1, s2) or canBreak(s2, s1)