import collections
import heapq

import numpy as np
from typing import List

# Runtime: 148 ms, faster than 17.42% of Python3 online submissions for The K Weakest Rows in a Matrix.
# Memory Usage: 14.1 MB, less than 20.68% of Python3 online submissions for The K Weakest Rows in a Matrix.
# Binary search on a matrix then pushing into a dictionary with a nested priority queue!
# Then iterating the sorted version of the dictionary in order to heap pop lowest indices. Then deleting empty entries.
# Bet it's possible with 1 line through a counter and lambdas but yeah ok.

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = collections.defaultdict(list)
        for i in range(len(mat)):
            l = 0
            r = len(mat[i])-1
            while l <= r:
                mid = (l+r)>>1
                soldier = mat[i][mid]
                if soldier == 1 and (mid == len(mat[i])-1 or mat[i][mid+1] == 0):
                    heapq.heappush(soldiers[mid+1], i)
                    break
                elif soldier == 0 and mid==0:
                    heapq.heappush(soldiers[mid], i)
                if mat[i][mid] == 1:
                    l = mid + 1
                elif mat[i][mid] == 0:
                    r = mid - 1
        items = sorted(soldiers.items())
        res = []
        while k > 0:
            pair = items[0]
            arr = pair[1]
            res.append(heapq.heappop(arr))
            if len(arr)==0:
                del items[0]
            k-=1
        return res

s = Solution()
#2,0,3
print(s.kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]],3))
#1,0
print(s.kWeakestRows([[1,0],[0,0],[1,0]],2))






























def scanrow(row):
    l = 0
    r = len(row)-1
    lens = []
    while l <= r:
        mid = (l+r)>>1
        if row[mid] == 1 and (mid==len(row)-1 or row[mid+1]==0):
            lens.append(mid)
            break
        elif row[mid] ==1:
            l = mid+1
        else:
            r = mid-1
    return lens
#print(scanrow([1,1,0,0,0]))
#print(scanrow([1,1,1,1,1]))

