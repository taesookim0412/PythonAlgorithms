import collections
import numpy as np
from typing import List

#cant binary search it. it requires two-pointer.
#There is no correlation between the middle value and the left and right pointers.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            mid = l + (r-l)//2
            if numbers[mid] + numbers[mid+1] == target:
                return [mid+1, mid+2]
            if numbers[mid-1] + numbers[mid] == target:
                return [mid, mid+1]
            if numbers[l] + numbers[r]==target and l!=r:
                return [l+1,r+1]
            if numbers[r] > target:
                r-=1
            elif numbers[mid]+numbers[r] < target:
                l = mid + 1
            else:
                r = mid
            print(l,r,mid)
        print('s')
        return sorted([l+1,r+1])

s = Solution()
#2,3
print(s.twoSum([5, 25, 75], 100))
#1,2
print(s.twoSum([2,7,11,15], 9))
#2,3
print(s.twoSum([2,3,4], 6))
#1,2
print(s.twoSum([0,0,3,4], 0))
#3,6
print(s.twoSum([3,24,50,79,88,150,345],200))
