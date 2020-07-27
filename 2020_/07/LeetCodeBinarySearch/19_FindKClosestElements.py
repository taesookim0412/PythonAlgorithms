import collections
import numpy as np
from typing import List
#89.26%
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k
        while l < r:
            mid = l + ( r - l) // 2
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid
        return arr[l:l+k]


#Positionally closest elements
class Solution2:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == x:
                l = mid
                break
            if arr[mid] < x:
                l = mid + 1
            elif arr[mid] > x:
                r = mid - 1
            print(l, r, mid)
        return arr[l-k:l] if l -k >= 0 else arr[0:k]

s = Solution()
print(s.findClosestElements([1, 2, 3, 4, 5], 4,3))
print(s.findClosestElements([1, 2, 3, 4, 5], 4, -1))
print(s.findClosestElements([1, 2, 3, 4, 5], 4, 5))
print(s.findClosestElements([1,2], 1, 1))