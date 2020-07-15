from typing import List

#05-22-2020_
#Runtime: 132 ms, faster than 24.06% of Python3 online submissions for Subarray Sum Equals K.
#Memory Usage: 16.1 MB, less than 20.00% of Python3 online submissions for Subarray Sum Equals K.
#https://leetcode.com/problems/subarray-sum-equals-k


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = {0: 1}
        totSum = 0
        ct = 0
        for i, a in enumerate(nums):
            totSum += a

            # check diff
            diff = totSum - k
            if diff in sums:
                ct += sums[diff]

            # push to hmap
            if totSum not in sums:
                sums[totSum] = 1
            else:
                sums[totSum] += 1
            print(sums)
        return ct

    def __init__(self):
        print(self.subarraySum([1, 2, 1, 2, 1, 2], 3))
        print(self.subarraySum([1, 1, 1], 2))

        # 2
        print(self.subarraySum([1, 2, 3], 3))
        print(self.subarraySum([1], 0))

        print(self.subarraySum([-1, -1 ,1], 0))
        print(self.subarraySum([0,0,0,0,0,0,0,0,0,0], 0))

Solution()
