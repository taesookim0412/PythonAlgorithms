import collections
import heapq

import numpy as np
from typing import List

#Also other ways to manipulate memory:
#Add two rows for phi, i.e a null 0-index column for dp J, plus a len(dp) column for the end of each row,
#that removes the conditional requirements.
#However this is how I create algorithms so this is why I solved it this way (to help when I'm
#put to the test without resources :))

#Or you can use a heapq, get the 2 smallest, and if the prev row's same-col value is the same, then
#add the 2nd smallest.

#Runtime: 1128 ms, faster than 32.67% of Python3 online submissions for Minimum Falling Path Sum II.
#Memory Usage: 16.7 MB, less than 78.57% of Python3 online submissions for Minimum Falling Path Sum II.
class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        dp = [[99999 for _ in range(len(arr))] for _ in range(len(arr[0]))]
        dp[0] = arr[0]
        for i in range(1, len(arr)):
            for j in range(len(arr[0])):
                lCands = heapq.nsmallest(1, dp[i-1][:j])
                rCands = []
                if j < len(arr[0])-1:
                    rCands = heapq.nsmallest(1, dp[i-1][j+1:])
                smallestNonColVal = min(lCands or [999999], rCands or [9999999])[-1]
                dp[i][j] = smallestNonColVal + arr[i][j]
        return min(dp[-1])


#How is this falling path sum 2 if they removed the constraint of at most 1 column different.
#They should call it something else.
class Solution2:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        dp = [[9999999 for _ in range(len(arr))] for _ in range(len(arr[0]))]
        dp[0] = arr[0]
        print(np.asmatrix(arr))
        for i in range(1, len(arr)):
            for j in range(len(arr[0])):
                l = j - 1 if j > 0 else 1
                r = j + 1 if j < len(arr[0])-1 else l
                if l == j: l = r
                dp[i][j] = min(dp[i-1][l], dp[i-1][r]) + arr[i][j]
        print(np.asmatrix(dp))
        return min(dp[-1])

s = Solution()
print(s.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))
print(s.minFallingPathSum([[2,2,1,2,2],[2,2,1,2,2],[2,2,1,2,2],[2,2,1,2,2],[2,2,1,2,2]]))
#-192
print(s.minFallingPathSum([[-73,61,43,-48,-36],[3,30,27,57,10],[96,-76,84,59,-15],[5,-49,76,31,-7],[97,91,61,-46,67]] ))


