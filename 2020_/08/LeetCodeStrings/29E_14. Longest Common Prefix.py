import collections
import numpy as np
from typing import List


#Runtime: 28 ms, faster than 94.89% of Python3 online submissions for Longest Common Prefix.
#Memory Usage: 13.9 MB, less than 59.52% of Python3 online submissions for Longest Common Prefix.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        shortest_Len =  len(min(strs, key=len))
        running_Ct = 0
        while running_Ct<shortest_Len:
            ch = strs[0][running_Ct]
            for i, c in enumerate(strs):
                if c[running_Ct] != ch:
                    return strs[0][:running_Ct]
            running_Ct += 1
        return strs[0][:running_Ct]


s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["aa","aa","aa"]))
print(s.longestCommonPrefix(["aa","ab"]))
print(s.longestCommonPrefix(["aa","a"]))