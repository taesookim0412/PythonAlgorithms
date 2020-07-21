import collections
import math

import numpy as np
from typing import List

#Runtime: 764 ms, faster than 21.48% of Python3 online submissions for Koko Eating Bananas.
#Memory Usage: 15 MB, less than 82.68% of Python3 online submissions for Koko Eating Bananas.

class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        lo = 1
        hi = max(piles)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            total = 0
            for pile in piles:
                total += math.ceil(pile/mid)
            if total > H:
                lo = mid + 1
            else:
                hi = mid
        return lo
s = Solution()
#4
print(s.minEatingSpeed([3,6,7,11], 8))

#30
print(s.minEatingSpeed([30,11,23,4,20], 5))