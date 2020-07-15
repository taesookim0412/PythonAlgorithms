import collections
import numpy as np
from typing import List

#a - i:
#1 - 9

#97 - 105
#49 - 57

#j - z:
#106 - 122

#10# - 26#:
# 106 - 96 + #
#Runtime: 52 ms, faster than 5.81% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.
#Memory Usage: 13.9 MB, less than 43.43% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.
#
class Solution:
    def freqAlphabets(self, s: str) -> str:
        #1 + 48 = a
        aiOffset = 48

        #10 + 96 = j
        jzoffset = 96

        res = []

        i = len(s)-1
        while i >= 0:
            a = s[i]
            if a == '#':
                num = int(''.join(s[i-2:i]))
                res.append(chr(num + 96))
                i-=3
                continue
            if '1' <= a <= '9':
                res.append(chr(ord(a) + 48))
            i-=1
        print(res)
        return ''.join(res[::-1])

print(Solution().freqAlphabets("10#11#12"))