import collections
import numpy as np
from typing import List


#TLE
#[1,0,0,1,0,0,1,0]
#1000000000
#nice
#https://en.wikipedia.org/wiki/Pigeonhole_principle

#Hashmap
#Debugging
#8%
#76%

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        N = N % 14
        if (N == 0): N = 14
        for x in range(N):
            newCell = [0 for _ in range(len(cells))]
            for i in range(1, len(cells)-1):
                left = cells[i-1]
                right = cells[i+1]
                if left == right == 1 or left == right == 0:
                    newCell[i] = 1
            cells = newCell
        return cells

s = Solution()
print(s.prisonAfterNDays([1,0,0,1,0,0,0,1], 826))
print(s.prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000))