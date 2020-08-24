import collections
import numpy as np
from typing import List

#Runtime: 96 ms, faster than 5.32% of Python3 online submissions for Implement strStr().
#Memory Usage: 29.7 MB, less than 5.03% of Python3 online submissions for Implement strStr().
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        np_Haystack = np.asarray(haystack)
        return np.char.find(np_Haystack, needle)


#Runtime: 32 ms, faster than 74.88% of Python3 online submissions for Implement strStr().
#Memory Usage: 14.1 MB, less than 31.86% of Python3 online submissions for Implement strStr().

class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

s = Solution()
print(s.strStr('hello', 'l'))
print(s.strStr('hello', ''))
print(s.strStr('hello', 'p'))