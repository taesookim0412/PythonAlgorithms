import collections
import numpy as np
from typing import List

#Runtime: 44 ms, faster than 48.37% of Python3 online submissions for Permutations.
#Memory Usage: 14.1 MB, less than 28.23% of Python3 online submissions for Permutations.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def heapPermute(path, size):
            if size == 1:
                ans.append(path.copy())
                return
            for i in range(size):
                heapPermute(path, size-1)
                if size&1:
                    path[0], path[size-1] = path[size-1], path[0]
                else:
                    path[i], path[size-1] = path[size-1], path[i]
        heapPermute(nums, len(nums))
        return ans
s = Solution()
print(s.permute([1,2,3]))
