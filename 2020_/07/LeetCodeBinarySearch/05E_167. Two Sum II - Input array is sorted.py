import collections
import numpy as np
from typing import List

#Runtime: 88 ms, faster than 28.35% of Python3 online submissions for Two Sum II - Input array is sorted.
#Memory Usage: 14.4 MB, less than 34.02% of Python3 online submissions for Two Sum II - Input array is sorted.

#Two-Pointer (The binary search one is terrible).
class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l <= r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            if s > target:
                r -= 1
            else:
                l += 1
        return []

#bored af
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = collections.defaultdict(dict)
        spot = 0
        def put(idx, num):
            res = nums[target-num]
            nums[num] = idx
            if res:
                nonlocal spot; spot = idx
                return [res,idx]
        return [put(i+1, a) for i,a in enumerate(numbers)][spot-1:spot][0]

#Hashmap version (just because)
class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = collections.defaultdict(dict)
        for i, a in enumerate(numbers):
            diff = target - a
            if nums[diff]:
                return [nums[diff]-1,i]
            nums[a] = i+1
        return []

s = Solution()
print(s.twoSum([2,7,11,15],9))