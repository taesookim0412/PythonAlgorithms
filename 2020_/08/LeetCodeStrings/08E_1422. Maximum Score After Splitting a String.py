import collections
import numpy as np
from typing import List

#Runtime: 36 ms, faster than 70.63% of Python3 online submissions for Maximum Score After Splitting a String.
#Memory Usage: 13.6 MB, less than 96.85% of Python3 online submissions for Maximum Score After Splitting a String.

class Solution:
    def maxScore(self, s: str) -> int:
        l = collections.defaultdict(int)
        r = collections.Counter(s)
        maxScore = 0
        for i in range(len(s)-1):
            c = s[i]
            l[c] += 1
            r[c] -= 1
            score = l['0'] + r['1']
            maxScore = max(score, maxScore)
        return maxScore