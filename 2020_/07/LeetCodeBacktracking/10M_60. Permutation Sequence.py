import collections
import itertools

import numpy as np
from typing import List


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n+1)]
        perms = list(itertools.permutations(nums))
        return ''.join(perms[k-1])

class Solution2:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n+1)]
        fact = [1] * n
        for i in range(1, n):
            fact[i] = i* fact[i-1]
        k-=1
        res = []
        for i in range(n, 0, -1):
            id = k // fact[i-1]
            k %= fact[i-1]
            res.append(nums[id])
            nums.pop(id)
        return ''.join(res)

#wut the hek
# class Solution:
#     def getPermutation(self, n: int, k: int) -> str:
#         initial = [str(i) for i in range(1,n+1)]
#         res = []
#         def backtrack(path, iterationValue, j):
#             print(path)
#             if iterationValue == k and len(path) == len(initial):
#                 res.append(path)
#             if len(res) > 0 or len(path) > 3:
#                 return
#             for i in range(j, len(initial)):
#                 backtrack((path + initial[i:] + initial[i+1:]).copy(), iterationValue+1, i+1)
#         backtrack([], k, 0)
#         print(res)
#         return res[-1]

s = Solution()
print(s.getPermutation(3,3))
