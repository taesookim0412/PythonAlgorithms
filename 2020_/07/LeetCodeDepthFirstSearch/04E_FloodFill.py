import collections
import numpy as np
from typing import List

#Runtime: 144 ms, faster than 7.45% of Python3 online submissions for Flood Fill.
#Memory Usage: 14.1 MB, less than 21.43% of Python3 online submissions for Flood Fill.

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(x, y, srcColor):
            if image[x][y] != srcColor or image[x][y] == newColor:
                return
            image[x][y] = newColor
            if x < len(image)-1:
                dfs(x+1, y, srcColor)
            if x > 0:
                dfs(x-1, y, srcColor)
            if y > 0:
                dfs(x, y-1, srcColor)
            if y < len(image[0])-1:
                dfs(x, y+1, srcColor)
        srcColor = image[sr][sc]
        dfs(sr, sc, srcColor)
        return image
s = Solution()
print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))