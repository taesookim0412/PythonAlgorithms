import collections
import numpy as np
from typing import List

#Runtime: 32 ms, faster than 97.56% of Python3 online submissions for Consecutive Characters.
#Memory Usage: 13.8 MB, less than 47.90% of Python3 online submissions for Consecutive Characters.

class Solution:
    def maxPower(self, s: str) -> int:
        maxPwr = 1
        ct = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                ct += 1
            else:
                ct = 1
            maxPwr = max(ct, maxPwr)
        return maxPwr

#Runtime: 68 ms, faster than 20.37% of Python3 online submissions for Consecutive Characters.
#Memory Usage: 13.8 MB, less than 71.43% of Python3 online submissions for Consecutive Characters.

class Solution:
    def maxPower(self, s: str) -> int:
        pwr = 1
        for i in range(len(s) - 1):
            j = i
            iPwr = 1
            while j + 1 < len(s) and s[j + 1] == s[j]:
                iPwr += 1
                j += 1
            pwr = max(iPwr, pwr)
        return pwr
