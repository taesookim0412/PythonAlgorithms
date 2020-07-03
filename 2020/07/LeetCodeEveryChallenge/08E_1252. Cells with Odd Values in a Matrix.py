from typing import List
#Runtime: 72 ms, faster than 22.45% of Python3 online submissions for Cells with Odd Values in a Matrix.
#Memory Usage: 13.7 MB, less than 93.79% of Python3 online submissions for Cells with Odd Values in a Matrix.

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        odds = 0
        mtx = [[0 for _ in range(m)] for _ in range(n)]
        for x in indices:
            a = x[0]
            b = x[1]
            mtx[a] = [x+1 for x in mtx[a]]
            for i in range(len(mtx)):
                mtx[i][b] += 1
        for i, a in enumerate(mtx):
            for j, b in enumerate(a):
                if b % 2 != 0:
                    odds+=1
        return odds
s = Solution()
print(s.oddCells(2,3,[[0,1],[1,1]]))
