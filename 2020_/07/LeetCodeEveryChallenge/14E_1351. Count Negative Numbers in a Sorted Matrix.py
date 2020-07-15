import collections
import numpy as np
from typing import List
#Runtime: 132 ms, faster than 48.85% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
#Memory Usage: 14.8 MB, less than 28.69% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negatives = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])-1, -1, -1):
                elm = grid[i][j]
                if elm >= 0:
                    break
                negatives += 1
        return negatives
print(Solution().countNegatives([[5,1,0],[-5,-5,-5]]))