import collections
import numpy as np
from typing import List
#53.83%
#21%
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            mid = l+(r-l)//2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l