import collections
import numpy as np
from typing import List

#abBA
#abB
#stack = [a,b]
#aA

#Runtime: 36 ms, faster than 91.40% of Python3 online submissions for Make The String Great.
#Memory Usage: 13.8 MB, less than 60.17% of Python3 online submissions for Make The String Great.

class Solution:
    def makeGood(self, s: str) -> str:
        res = []
        stack = []
        for i in range(len(s)):
            char = s[i]
            if stack and stack[-1] == char.swapcase():
                res.pop()
                stack.pop()
            else:
                res += char,
                stack += char,
        return ''.join(res)
s = Solution()
print(s.makeGood("abBA"))
