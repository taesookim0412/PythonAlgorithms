import collections
import numpy as np
from typing import List


#Runtime: 68 ms, faster than 89.45% of Python3 online submissions for Bulb Switcher IV.
#Memory Usage: 14.4 MB, less than 72.31% of Python3 online submissions for Bulb Switcher IV.
class Solution:
    def minFlips(self, target: str) -> int:
        ct = int(target[0])
        for a, b in zip(target, target[1:]):
            if a != b:
                ct += 1
        return ct


#Runtime: 92 ms, faster than 67.93% of Python3 online submissions for Bulb Switcher IV.
#Memory Usage: 14.5 MB, less than 26.37% of Python3 online submissions for Bulb Switcher IV.
class Solution2:
    def minFlips(self, target: str) -> int:
        ct = 0
        if target[0] == '1': ct += 1
        for i in range(1, len(target)):
            if target[i] != target[i-1]:
                ct += 1
        return ct

s = Solution()
print(s.minFlips("10111"))