import collections
import numpy as np
from typing import List

#Runtime: 92 ms, faster than 41.03% of Python3 online submissions for Minimum Time Difference.
#Memory Usage: 17.8 MB, less than 5.59% of Python3 online submissions for Minimum Time Difference.

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = list(sorted([list(map(int, timePoint.split(':'))) for timePoint in timePoints]))
        #print(timePoints)
        minDifference = 9999999
        for i in range(1, len(timePoints)):
            timeA = timePoints[i-1]
            timeB = timePoints[i]
            timeBtw = (timeB[0] * 60 + timeB[1]) - (timeA[0] * 60 + timeA[1])
            minDifference = min(minDifference, timeBtw)
        nocturnal_diff = ((timePoints[0][0]+24) * 60 + timePoints[0][1]) - (timePoints[-1][0] * 60 + timePoints[-1][1])
        minDifference = min(minDifference, nocturnal_diff)
        return minDifference

#["23:59","00:00"]
