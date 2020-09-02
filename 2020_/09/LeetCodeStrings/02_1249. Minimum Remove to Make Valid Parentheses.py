import collections
import numpy as np
from typing import List

#Runtime: 120 ms, faster than 80.64% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
#Memory Usage: 17.8 MB, less than 5.04% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        balance = 0
        openers = []
        for i,c in enumerate(s):
            if balance <= 0 and c == ')':
                continue
            if c == '(':
                openers += len(res),
                res += c,
                balance += 1
            elif c == ')':
                res += c,
                balance -= 1
            else:
                res += c,
        for i in range(balance):
            del res[openers.pop()]
        return ''.join(res)