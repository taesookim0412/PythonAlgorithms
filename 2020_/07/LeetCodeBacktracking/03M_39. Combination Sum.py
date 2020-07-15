import collections
from time import perf_counter
from datetime import datetime

import numpy as np
from typing import List

#Runtime: 100 ms, faster than 44.68% of Python3 online submissions for Combination Sum.
#Memory Usage: 13.9 MB, less than 57.35% of Python3 online submissions for Combination Sum.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(path,total, idx):
            if total == target:
                res.append(path.copy())
                #print(path,total)
                return
            elif total > target:
                return
            for i in range(idx, len(candidates)):
                backtrack([*path, candidates[i]], total + candidates[i], i)
        backtrack([], 0, 0)
        return res

# Runtime: 108 ms, faster than 36.19% of Python3 online submissions for Combination Sum.
# Memory Usage: 13.9 MB, less than 44.41% of Python3 online submissions for Combination Sum.

class Solution1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(path,total, idx):
            if total == target:
                res.append(path.copy())
                #print(path,total)
                return
            elif total > target:
                return
            for i in range(idx, len(candidates)):
                path.append(candidates[i])
                backtrack(path, total + candidates[i], i)
                path.pop()
        backtrack([], 0, 0)
        return res

#Runtime: 132 ms, faster than 24.28% of Python3 online submissions for Combination Sum.
#Memory Usage: 14 MB, less than 26.63% of Python3 online submissions for Combination Sum.

class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        def backtrack(path,total,idx):
            if total == target:
                res.update([tuple(sorted(path))])
                print(path,total)
                return
            elif total > target:
                return
            for i in range(idx,len(candidates)):
                backtrack((*path, candidates[i]), total + candidates[i],i)
        backtrack([], 0,0)
        return list(res)

#WOW it's beautiful.
#Runtime: 1004 ms, faster than 5.04% of Python3 online submissions for Combination Sum.
#Memory Usage: 14.1 MB, less than 14.51% of Python3 online submissions for Combination Sum.
class Solution3:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        def backtrack(path,total):
            if total == target:
                res.update([tuple(sorted(path))])
                print(path,total)
                return
            elif total > target:
                return
            for i in range(len(candidates)):
                backtrack((*path, candidates[i]), total + candidates[i])
        backtrack((), 0)
        return list(res)


s = Solution()
print(s.combinationSum([2,3,6,7],7))