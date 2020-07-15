import collections
import numpy as np
from typing import List


#hold up this isnt binary search.. :(
# Runtime: 64 ms, faster than 28.94% of Python3 online submissions for Intersection of Two Arrays.
# Memory Usage: 13.7 MB, less than 95.63% of Python3 online submissions for Intersection of Two Arrays.
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #0 =
        nums = [nums1, nums2]
        nums.sort(key=len)
        smaller = nums[0]
        larger = nums[1]
        data = set()
        res = set()
        for i in range(len(smaller)):
            data.add(smaller[i])
        for i in range(len(larger)):
            if larger[i] in data:
                res.add(larger[i])
        return list(res)

#{smaller[i]}.union(data)


s = Solution()
print(s.intersection([2], [1,2]))
print(s.intersection([1,2,2,1], [2,2]))

