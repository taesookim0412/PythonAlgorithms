import collections
import numpy as np
from typing import List
#Runtime: 36 ms, faster than 82.38% of Python3 online submissions for String Matching in an Array.
#Memory Usage: 14 MB, less than 15.15% of Python3 online submissions for String Matching in an Array.

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        res = []
        for i, a in enumerate(words):
            for j in range(i+1, len(words)):
                if a in words[j]:
                    res += a,
        return set(res)