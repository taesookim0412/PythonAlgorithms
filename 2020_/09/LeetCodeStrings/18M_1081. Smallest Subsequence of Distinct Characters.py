import collections
import numpy as np
from typing import List


class Solution:


    #smallest substring with varient length (redundant)(question also asked for subsequence)
    def smallestSubsequence(self, s) -> str:
        candidates = []
        distincts = set(s)
        for i in range(1, len(s) + 1):
            ctr = collections.Counter(s[:i])
            for j in range(len(s) - i + 1):
                # fiter: 0:0+1
                # window = s[j:j+i]
                if j != 0:
                    prev = s[j - 1]
                    curr = s[j + i - 1]
                    ctr[curr] += 1
                    if ctr[prev] == 1:
                        del ctr[prev]
                    else:
                        ctr[prev] -= 1
                if len(ctr) == len(distincts):
                    if sum(ctr.values()) == len(distincts):
                        candidates += s[j:j + i],
        print(candidates)
        return min(candidates)

s = Solution()
print(s.smallestSubsequence("cdadabcc"))