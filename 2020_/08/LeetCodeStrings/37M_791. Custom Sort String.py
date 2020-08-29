import collections
import numpy as np
from typing import List

#Runtime: 28 ms, faster than 86.67% of Python3 online submissions for Custom Sort String.
#Memory Usage: 13.8 MB, less than 65.79% of Python3 online submissions for Custom Sort String.

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        indices = {char: i for i, char in enumerate(S) }
        return ''.join(sorted(T, key=lambda x: indices.get(x, len(T))))

s = Solution()
print(s.customSortString("cba",
"abcds"))