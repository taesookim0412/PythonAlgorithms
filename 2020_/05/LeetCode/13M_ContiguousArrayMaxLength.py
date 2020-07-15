from typing import List

#05-24-2020_
#Runtime: 896 ms, faster than 79.18% of Python3 online submissions for Contiguous Array.
#Memory Usage: 18.2 MB, less than 16.67% of Python3 online submissions for Contiguous Array.
#https://leetcode.com/problems/contiguous-array

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map = {0: -1}
        ct = 0
        maxlen = 0
        for i in range(0, len(nums)):
            ct += 1 if nums[i] == 1 else -1
            if ct in map:
                maxlen = max(maxlen, i - map[ct])
            else:
                map[ct] = i
        return maxlen
    def __init__(self):
        print(self.findMaxLength([0, 0, 1, 0, 0, 0, 1, 1]))

Solution()