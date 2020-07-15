import collections
import numpy as np
from typing import List


#Runtime: 612 ms, faster than 53.49% of Python3 online submissions for Island Perimeter.
#Memory Usage: 13.9 MB, less than 88.33% of Python3 online submissions for Island Perimeter.

#XD
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        grid.insert(0, [0 for _ in range(len(grid[0]))])
        grid.append([0 for _ in range(len(grid[0]))])
        for i in range(len(grid)):
            grid[i].insert(0, 0)
            grid[i].append(0)
        print(np.asmatrix(grid))
        res = 0
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if grid[i][j] == 1:
                    res += 4 - grid[i-1][j] - grid[i+1][j] - grid[i][j-1] - grid[i][j+1]
        return res


# class Solution:
#     def islandPerimeter(self, grid: List[List[int]]) -> int:
#         dp = [[0 for _ in range(len(grid[0])+2)] for _ in range(len(grid)+2)]
#         res = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 1:
#                     if i == 0:
#                         res += 4 - grid[i][j+1] - grid[i][j-1] - grid[i+1][j]
#                     elif i == len(grid):
#                         res += 4 - grid[i][j+1] - grid[i][j-1] - grid[i-1][j]
#                     elif j=
#         print(res)
#         return dp[-2][-2]

s = Solution()
print(s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))