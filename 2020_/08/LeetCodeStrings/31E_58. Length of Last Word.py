import collections
import numpy as np
from typing import List

#Runtime: 28 ms, faster than 82.54% of Python3 online submissions for Length of Last Word.
#Memory Usage: 13.7 MB, less than 92.72% of Python3 online submissions for Length of Last Word.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = list(filter(None, s.split(' ')))
        #print(words)
        return len(words[-1]) if words else 0

# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         space = s.rfind(' ')
#         if space != -1: return len(s) - space - 1
#         return 0

s = Solution()
print(s.lengthOfLastWord("Hello World"))
print(s.lengthOfLastWord(""))
print(s.lengthOfLastWord(" "))
print(s.lengthOfLastWord("a   "))