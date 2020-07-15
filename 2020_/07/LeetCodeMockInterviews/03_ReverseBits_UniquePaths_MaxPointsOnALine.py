import collections
import numpy as np
from typing import List

# Random Set- On-Site Interview
# AttemptedJuly 14, 2020_ 7:28 PM
# Time Spent: 1 hour 25 minutes 26 seconds
# Time Allotted: 2 hours


#Hard
#38/41
#Messy
#Think I'm missing something

#Edge Case:
#[0,0] Returns 1
#[0,0][0,0]: Two points (Verts)

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)==0: return 0
        maxVerts = 0
        maxPts = 0
        for i in range(len(points)):
            slopes = collections.defaultdict(lambda:1)
            verts = collections.defaultdict(lambda:1)
            for j in range(len(points)):
                if i==j:continue
                coordsI = points[i]
                coordsJ = points[j]
                # Slope = y-y1/x-x1
                denominator = coordsJ[0] - coordsI[0]
                if denominator == 0:
                    verts[coordsI[0]] += 1
                else:
                    slope = (coordsJ[1] - coordsI[1]) / denominator
                    slopes[slope] += 1
            maxPts = max(max(slopes.values()), maxPts) if slopes.values() else maxPts
            maxVerts = max(max(verts.values()), maxVerts) if verts.values() else maxVerts
        cand = max(maxPts, maxVerts)
        return cand if cand != 0 else 1

s = Solution()
print(s.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
#1
print(s.maxPoints([[0,0]]))
#2
print(s.maxPoints([[0,0],[0,0]]))

#3
print(s.maxPoints([[0,0],[1,1],[0,0]]))


#Medium
#62/62 O(N) Every points on grid O(2) memory
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(m)] for _ in range(2)]
        empty = [1 for _ in range(m)]
        for i in range(n-1):
            dp[(i+1)&1] = empty
            for j in range(m-1):
                dp[(i+1)&1][j+1] = dp[i&1][j+1] + dp[(i+1)&1][j]
        return dp[(n+1)&1][-1]

#Easy
#Needed help
#600/600
class Solution:
    def reverseBits(self, n: int):
        res = 0
        power = 31
        while n > 0:
            res += (n & 1) << power
            power -= 1
            n >>= 1
        return res

    # def reverseBits(self, n: int) -> int:
    #     res = 1
    #     while n > 0:
    #         res = res << 1
    #         if n&1==1:
    #             res = res ^ 1
    #         n = n >> 1
    #     return res