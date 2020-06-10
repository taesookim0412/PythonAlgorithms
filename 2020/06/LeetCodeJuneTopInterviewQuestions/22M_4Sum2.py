from typing import List
#Runtime: 336 ms, faster than 46.84% of Python3 online submissions for 4Sum II.
#Memory Usage: 34.7 MB, less than 72.26% of Python3 online submissions for 4Sum II.
#Basically 2Sum just double it

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        nums = {}
        ct = 0
        for a in A:
            for b in B:
                nums[a+b] = nums.get(a+b, 0) + 1
        for c in C:
            for d in D:
                ct += nums.get(-(c+d), 0)
        return ct

sol = Solution()
print(sol.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))
