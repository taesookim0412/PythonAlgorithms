import collections
from typing import List
#Runtime: 80 ms, faster than 54.40% of Python3 online submissions for Max Increase to Keep City Skyline.
#Memory Usage: 14.1 MB, less than 14.83% of Python3 online submissions for Max Increase to Keep City Skyline.

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        maxI = collections.defaultdict(list)
        maxJ = collections.defaultdict(list)
        for i in range(len(grid)):
            maxI[i] = max(grid[i])
            for j in range(len(grid[0])):
                if not maxJ[j]:
                    maxJ[j] = grid[i][j]
                    continue
                maxJ[j] = max(maxJ[j], grid[i][j])
        sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                diff = min(maxI[i], maxJ[j]) - grid[i][j]
                if diff >0:
                    sum+= diff
                grid[i][j] = min(maxI[i], maxJ[j])
        return sum

s = Solution()
print(s.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))
