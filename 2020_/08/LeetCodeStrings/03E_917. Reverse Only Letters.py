import collections
import numpy as np
from typing import List
#Runtime: 28 ms, faster than 82.28% of Python3 online submissions for Reverse Only Letters.
#Memory Usage: 13.9 MB, less than 18.18% of Python3 online submissions for Reverse Only Letters.

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        res = []
        for i in range(len(S)):
            if S[i].isalpha():
                res += S[i],
        res = res[::-1]
        for i in range(len(S)):
            if not S[i].isalpha():
                res.insert(i, S[i])
        return ''.join(res)

s = Solution()
print(s.reverseOnlyLetters("a-bC-dEf-ghIj"))