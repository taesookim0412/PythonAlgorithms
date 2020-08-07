import collections
import numpy as np
from typing import List

#Runtime: 28 ms, faster than 85.65% of Python3 online submissions for Path Crossing.
#Memory Usage: 13.7 MB, less than 88.33% of Python3 online submissions for Path Crossing.

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        v = 0
        h = 0
        verticals = {'N': 1, 'S':-1}
        horizontals = {'E': 1, 'W': -1}
        visited = set([(0,0)])
        for c in path:
            if c in verticals:
                v+=verticals[c]
            elif c in horizontals:
                h+= horizontals[c]
            if (h,v) in visited:
                return True
            visited = visited | {(h,v)}
        return False


s = Solution()
print(s.isPathCrossing("NESW"))