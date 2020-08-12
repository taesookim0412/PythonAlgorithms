import collections
import numpy as np
from typing import List

#str1: "ABCABC"
#str2: "ABC"
#X: "ABC"

#"ABABAB"
#"ABAB"
#X: "AB"

# ABABAB ABAB
# AB ABAB
# AB AB
# AB

#Runtime: 28 ms, faster than 86.62% of Python3 online submissions for Greatest Common Divisor of Strings.
#Memory Usage: 13.9 MB, less than 29.23% of Python3 online submissions for Greatest Common Divisor of Strings.

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        while str1 != "":
            print(str1, str2)
            if len(str1) == len(str2):
                return str1 if str1 == str2 else ""
            if len(str1) < len(str2):
                str1, str2 = str2, str1
            str1 = str1[len(str2):]
        return ""

s = Solution()
print(s.gcdOfStrings("ABCABC", 'ABC'))
#6 % 4 == 2
print(s.gcdOfStrings("ABABAB", 'ABAB'))
print(s.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX",
"TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))

print(s.gcdOfStrings("LEET", 'CODE'))