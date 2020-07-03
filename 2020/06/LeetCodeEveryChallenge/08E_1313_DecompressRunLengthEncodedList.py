import collections
from typing import List

#Runtime: 124 ms, faster than 5.88% of Python3 online submissions for Decompress Run-Length Encoded List.
#Memory Usage: 14 MB, less than 53.90% of Python3 online submissions for Decompress Run-Length Encoded List.

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        list= []
        for i in range(0, len(nums),2):
            for j in range(nums[i]):
                list += nums[i+1],
        return list

s = Solution()
print(s.decompressRLElist([1,2,3,4]))