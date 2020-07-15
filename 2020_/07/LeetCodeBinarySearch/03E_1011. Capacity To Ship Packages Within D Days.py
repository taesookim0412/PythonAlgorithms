import collections
import numpy as np
from typing import List
#Runtime: 596 ms, faster than 54.15% of Python3 online submissions for Capacity To Ship Packages Within D Days.
#Memory Usage: 17.3 MB, less than 5.05% of Python3 online submissions for Capacity To Ship Packages Within D Days.

#https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)
        while left <= right:
            mid, curr, need = (left + right)//2 , 0, 1
            for w in weights:
                if curr + w > mid:
                    curr = 0
                    need += 1
                curr += w
            if need > D: left = mid + 1
            else: right = mid - 1
        return left






















class Solution2:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)
        while left<=right:
            mid,need,cur = (left + right)//2, 1, 0
            for w in weights:
                if cur + w > mid:
                    need +=1
                    cur = 0
                cur += w
            print(need, left)
            if need > D: left = mid + 1
            else: right = mid - 1
        return left

s=Solution()
print(s.shipWithinDays([1,2,3,4,5,6,7,8,9,10],5))