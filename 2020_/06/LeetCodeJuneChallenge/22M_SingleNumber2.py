from typing import List
#65% faster runtime
#90% less mem

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for i, a in enumerate(nums):
            ones = (ones ^ a) & ~twos
            twos = (twos ^ a) & ~ones
        return ones

s = Solution()
print(s.singleNumber([2,2,3,2]))