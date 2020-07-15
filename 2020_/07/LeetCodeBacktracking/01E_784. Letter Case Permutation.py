import collections
import numpy as np
from typing import List

#bfs backtrack
#Runtime: 100 ms, faster than 16.83% of Python3 online submissions for Letter Case Permutation.
#Memory Usage: 14.9 MB, less than 27.74% of Python3 online submissions for Letter Case Permutation.
class Solution:
    def letterCasePermutation(self, input) -> List[str]:
        res = []
        def backtrack(s,i):
            if i==len(s):
                res.append(''.join(s))
                return
            if s[i].isalpha():
                s[i] = s[i].upper()
                backtrack(s, i+1)
                s[i] = s[i].lower()
                backtrack(s, i+1)
            else:
                backtrack(s, i+1)
        string = list(input)
        backtrack(string, 0)
        return res

print(Solution().letterCasePermutation("a1b2"))
