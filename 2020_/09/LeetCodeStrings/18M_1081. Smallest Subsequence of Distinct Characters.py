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