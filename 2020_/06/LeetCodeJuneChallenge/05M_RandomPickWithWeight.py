from random import random
from typing import List


#Runtime: 5256 ms, faster than 9.45% of Python3 online submissions for Random Pick with Weight.
#Memory Usage: 18.4 MB, less than 17.41% of Python3 online submissions for Random Pick with Weight.

class Solution:
    def __init__(self, w: List[int]):
        self.w = w
    def pickIndex(self):
        return random.choices(range(len(self.w)), self.w)[0]

#Sample 244ms submission TODO: Read this
# class Solution:
#
#     def __init__(self, w: List[int]):
#         self.pre_sum = []
#         pre_sum = 0
#         for weight in w:
#             pre_sum += weight
#             self.pre_sum.append(pre_sum)
#         self.total_sum = pre_sum
#
#     def pickIndex(self) -> int:
#         target = self.total_sum * random.random()
#         lo, hi = 0, len(self.pre_sum)
#         while lo < hi:
#             mid = lo + (hi - lo) // 2
#             if self.pre_sum[mid] < target:
#                 lo = mid + 1
#             else:
#                 hi = mid
#         return lo

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()