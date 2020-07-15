import collections
import heapq

import numpy as np
from typing import List
#Input: A = [1, 4, 3, 2, 5]
#Candidates: [1,4,3,2] / [4, 3, 2, 5]
#Output: [4,3,2,5]



#Optimized solution
class Solution:
    def largestSubarray(self, arr, k):
        heap = []
        for i in range(0,len(arr)+1-k):
            heapq.heappush(heap, arr[i:i+k])
        return heapq.nlargest(1, heap)[-1]

#Time complexity: O(n) Possible to optimize further
#Space complexity: O(n) Every possible subarray
class Solution2:
    def largestSubarray(self, arr, k):
        heap = []
        for i in range(len(arr)):
            if i+i+k <= len(arr) + 1:
                heapq.heappush(heap, arr[i:i+k])
        return heapq.nlargest(1, heap)[-1]

class Solution3:
    def largestSubarray(self, arr, k):
        subArrays = []
        for i in range(len(arr)):
            if i+i+k <= len(arr) + 1:
                subArrays += [arr[i:i+k]]
        subArrays.sort()
        print(subArrays)
        return subArrays[-1]

s = Solution()
print(s.largestSubarray([1,4,3,2,5],4))