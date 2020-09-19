import collections
import numpy as np
from typing import List

# Runtime: 148 ms, faster than 13.59% of Python3 online submissions for Check If Word Is Valid After Substitutions.
# Memory Usage: 13.7 MB, less than 98.14% of Python3 online submissions for Check If Word Is Valid After Substitutions.

#delete every abc entry
class Solution:
    def isValid(self, s: str) -> bool:
        findVal = s.find('abc')
        while findVal != -1:
            s = s[:findVal] + s[findVal+3:]
            findVal = s.find('abc')
        return s==''


print(Solution().isValid("aabcbc"))
print(Solution().isValid("aabcbc"))