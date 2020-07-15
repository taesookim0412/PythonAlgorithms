import collections
import numpy as np
from typing import List

#ajdhgf
#

#Runtime: 428 ms, faster than 14.45% of Python3 online submissions for Minimum Number of Steps to Make Two Strings Anagram.
#Memory Usage: 14.4 MB, less than 11.72% of Python3 online submissions for Minimum Number of Steps to Make Two Strings Anagram.
#https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/discuss/721763/Python-Hashmap-Solution

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        chrs = collections.defaultdict(dict)
        for i, a in enumerate(s):
            if not chrs[a]:
                chrs[a] = 1
                continue
            chrs[a]+=1
        criticalChars = 0
        for i, a in enumerate(t):
            if chrs[a]:
                criticalChars += 1
                chrs[a]-=1
        return len(t) - criticalChars

s = Solution()
#1
print(s.minSteps("bab", "aba"))
#5
print(s.minSteps("leetcode", "practice"))
#18
print(s.minSteps("gctcxyuluxjuxnsvmomavutrrfb",
"qijrjrhqqjxjtprybrzpyfyqtzf"))