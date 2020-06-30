import collections
from typing import List

#Runtime: 40 ms, faster than 75.15% of Python3 online submissions for Running Sum of 1d Array.
#Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Running Sum of 1d Array.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if not nums: return []
        rs = []
        for i in range(0,len(nums)):
            if not rs:
                rs.append(nums[i])
                continue
            rs.append(rs[-1] + nums[i])
        return rs


#Runtime: 28 ms, faster than 99.44% of Python3 online submissions for Running Sum of 1d Array.
#Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Running Sum of 1d Array.


class Solution2:
    def runningSum(self, nums: List[int]) -> List[int]:
        if not nums: return []
        rs = [nums[0]]
        for i in range(1,len(nums)):
            rs.append(rs[-1] + nums[i])
        return rs


s = Solution()
print(s.runningSum([1,2,3,4]))