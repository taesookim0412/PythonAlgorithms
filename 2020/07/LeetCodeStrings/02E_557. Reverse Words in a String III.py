import collections
import numpy as np
from typing import List

#Runtime: 108 ms, faster than 7.84% of Python3 online submissions for Reverse Words in a String III.
#Memory Usage: 14.3 MB, less than 34.10% of Python3 online submissions for Reverse Words in a String III.
class Solution:
    def reverseWords(self, s: str) -> str:
        if s == "": return ""
        st = list(s)
        ls = -1
        for i, x in enumerate(st):
            if x == ' ':
                st[ls+1:i] = reversed(st[ls+1:i])
                ls = i
        if st[-1] != ' ':
            st[ls+1:len(st)] = reversed(st[ls+1:len(st)])
        return ''.join(st)

s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))
