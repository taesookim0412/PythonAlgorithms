import collections
import numpy as np
from typing import List

#Runtime: 40 ms, faster than 82.89% of Python3 online submissions for Repeated Substring Pattern.
#Memory Usage: 14.1 MB, less than 12.65% of Python3 online submissions for Repeated Substring Pattern.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)//2, 0, -1):
            if len(s)%i == 0:
                ls = s[:i]
                if ls * (len(s)//i) == s:
                    return True


#Runtime: 872 ms, faster than 6.48% of Python3 online submissions for Repeated Substring Pattern.
#Memory Usage: 13.9 MB, less than 40.33% of Python3 online submissions for Repeated Substring Pattern.

class Solution2:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ls = ""
        rs = list(s)[::-1]
        for i in range(len(s)//2):
            ls += rs.pop()
            ls2 = ls
            while len(ls2) <= len(s) and (len(s)/len(ls)).is_integer():
                if len(ls2) == len(s):
                    if ls2 == s:
                        return True
                    break
                ls2 += ls
        return False

s = Solution()
print(s.repeatedSubstringPattern("abab"))
print(s.repeatedSubstringPattern("ababab"))