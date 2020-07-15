import collections
import numpy as np
from typing import List
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.



#2, 3, 5
#2, 4, 8, 16
#3, 9, 27
#5, 25, 125

#
# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         twoPrimes = [2]
#         threePrimes = [3]
#         fivePrimes = [5]
#         while len(twoPrimes) + len(threePrimes) + len(fivePrimes) < n:
#             if twoPrimes[-1] < threePrimes[-1]:
#                 twoPrimes += twoPrimes[-1] * 2,
#             elif threePrimes[-1] < fivePrimes[-1]:
#                 threePrimes += threePrimes[-1]*3,
#             else:
#                 fivePrimes += fivePrimes[-1] * 5,
#         print(twoPrimes,threePrimes,fivePrimes)
#sol:
# class Solution:
#     def nthUglyNumber(self, n):
#         ugly = [1]
#         i2 = i3 = i5 = 0
#         while len(ugly) < n:
#             while ugly[i2] * 2 <= ugly[-1]: i2 += 1
#             while ugly[i3] * 3 <= ugly[-1]: i3 += 1
#             while ugly[i5] * 5 <= ugly[-1]: i5 += 1
#             ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
#         return ugly[-1]


s = Solution()
s.nthUglyNumber(10)
