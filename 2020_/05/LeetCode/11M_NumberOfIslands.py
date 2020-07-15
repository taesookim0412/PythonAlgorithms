from typing import List

#05-21-2020_
#Runtime: 156 ms, faster than 41.77% of Python3 online submissions for Number of Islands.
#Memory Usage: 15 MB, less than 9.40% of Python3 online submissions for Number of Islands.
#https://leetcode.com/problems/number-of-islands

#Interesting finds:
#The order for the recursive steps don't matter you could do UDLR, LDRU, RLUD, whichever,
#and it won't matter
#Also the "-1" was unused.

class Solution:
    grid = [[]]
    #O(n^2) runtime
    #Constant space
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        islands = 0
        print(grid)
        for i, a in enumerate(grid):
            for j, b in enumerate(grid[i]):
                if grid[i][j] == "1":
                    self.traverseIsland(i, j)
                    islands += 1

        return islands

    def traverseIsland(self, i: int, j: int):
        grid = self.grid
        #oob
        if i < 0 or i == len(grid): return
        if j < 0 or j == len(grid[i]): return
        if grid[i][j] != "1": return
        grid[i][j] = "-1"
        #uldr (ccw)
        self.traverseIsland(i-1, j)
        self.traverseIsland(i, j-1)
        self.traverseIsland(i+1, j)
        self.traverseIsland(i, j+1)

        #udlr
        # self.traverseIsland(i - 1, j)
        # self.traverseIsland(i + 1, j)
        # self.traverseIsland(i, j - 1)
        # self.traverseIsland(i, j + 1)






















    def strList(self, list: List[int]) -> List[str]:
        newList = []
        for i, a in enumerate(list):
            newList.append(str(a))
        return newList

    def __init__(self):
        print(self.numIslands([self.strList([1, 1, 0, 1]), self.strList([1, 1, 0, 0]), self.strList([1, 1, 0, 1])]))




Solution()