import collections
import numpy as np
from typing import List

#Runtime: 32 ms, faster than 78.99% of Python3 online submissions for Maximum Number of Balloons.
#Memory Usage: 13.8 MB, less than 61.40% of Python3 online submissions for Maximum Number of Balloons.

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = collections.Counter(text)
        res = min(letters['b'],
                  letters['a'],
                  letters['l']//2,
                  letters['o']//2,
                  letters['n'])
        return res

s = Solution()
print(s.maxNumberOfBalloons("loonbalxballpoon"))