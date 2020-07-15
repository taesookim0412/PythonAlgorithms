from typing import List
import numpy as np

#05-17-2020_
#https://leetcode.com/problems/minimum-path-sum/submissions/
#Runtime: 104 ms, faster than 67.03% of Python3 online submissions for Minimum Path Sum.
#Memory Usage: 15.1 MB, less than 26.32% of Python3 online submissions for Minimum Path Sum.
#dp solution definitely better


class Solution:
    cand = []
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        #print(np.matrix(grid))
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
            
    
    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     self.cand = []
    #     print(np.matrix(grid))
    #     self.traverseGrid(grid, 0, 0, 0)
    #     print(self.cand)
    #     print(np.matrix(grid))
    #     return min(self.cand)
        
    # def traverseGrid(self, grid:List[List[int]], sum: int, i:int, j:int):
    #     sum += grid[i][j]
    #     print(i, j)
    #     if i== len(grid)-1 and j== len(grid[len(grid)-1])-1: 
    #         return self.cand.ap~pend(sum)
    #     if i < (len(grid)-1): self.traverseGrid(grid, sum, i+1, j)
    #     if j < (len(grid[i]) -1): self.traverseGrid(grid, sum, i, j+1)
        
        
        
    def __init__(self):
        print(self.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
        print(self.minPathSum([[1]]))
        print(self.minPathSum([[1, 2, 5], [3, 2, 1]]))
        #print(self.minPathSum([[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]))
        
Solution()