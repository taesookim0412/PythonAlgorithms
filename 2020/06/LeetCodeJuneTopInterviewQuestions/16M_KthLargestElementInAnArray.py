#Runtime: 96 ms, faster than 30.39% of Python3 online submissions for Kth Largest Element in an Array.
#Memory Usage: 14.3 MB, less than 97.27% of Python3 online submissions for Kth Largest Element in an Array.

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        he = []
        for i in range(len(nums)):
            heapq.heappush(he, nums[i])
        return heapq.nlargest(k, he)[-1]