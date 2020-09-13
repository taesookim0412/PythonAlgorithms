import collections
import numpy as np
from typing import List

# Runtime: 376 ms, faster than 35.28% of Python3 online submissions for Number of Substrings Containing All Three Characters.
# Memory Usage: 14.3 MB, less than 9.11% of Python3 online submissions for Number of Substrings Containing All Three Characters.

#abca
#abc -> + abca
#cabca
#aaabc
#3
#aababc

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ctr = collections.defaultdict(int)
        res = 0
        j = 0
        for i in range(len(s)):
            ctr[s[i]] += 1
            while len(ctr) == 3:
                res += len(s) - i
                ctr[s[j]] -= 1
                if not ctr[s[j]]:
                    del ctr[s[j]]
                j += 1
        return res
s = Solution()
print(s.numberOfSubstrings("abc"))
print(s.numberOfSubstrings("abca"))
print(s.numberOfSubstrings("abcabc"))