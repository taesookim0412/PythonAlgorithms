import collections
import numpy as np
from typing import List

#340
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        def backtrack(path, total, idx):
            if total == target:
                res.update([tuple(sorted(path))])
            elif total > target:
                return
            for i in range(idx, len(candidates)):
                backtrack([*path, candidates[i]], total + candidates[i], i+1)
        backtrack([], 0, 0)
        return list(res)

#396ms
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        def backtrack(path, total, idx):
            if total == target:
                res.update([tuple(sorted(path))])
            elif total > target:
                return
            for i in range(idx+1, len(candidates)):
                backtrack([*path, candidates[i]], total + candidates[i], i)
        backtrack([], 0, -1)
        return list(res)

#684ms
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()
        def backtrack(path, total, idx):
            if total == target:
                res.update([tuple(path)])
            elif total > target:
                return
            for i in range(idx+1, len(candidates)):
                backtrack([*path, candidates[i]], total + candidates[i], i)
        backtrack([], 0, -1)
        return list(res)

#704ms
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()
        def backtrack(path, total, idx):
            if total == target:
                res.update([tuple(path)])
            elif total > target:
                return
            for i in range(idx, len(candidates)):
                backtrack([*path, candidates[i]], total + candidates[i], i+1)
        backtrack([], 0, 0)
        return list(res)

#892ms
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()
        def backtrack(path, total, idx):
            if total == target:
                res.update([path])
            elif total > target:
                return
            for i in range(idx, len(candidates)):
                backtrack((*path, candidates[i]), total + candidates[i], i+1)
        backtrack((), 0, 0)
        return list(res)

#Runtime: 280 ms, faster than 18.14% of Python3 online submissions for Combination Sum II.
#Memory Usage: 13.9 MB, less than 51.65% of Python3 online submissions for Combination Sum II.

class Solution2:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        def backtrack(path, total, idx):
            if total == target:
                res.update([tuple(sorted(path))])
            elif total > target:
                return
            for i in range(idx+1, len(candidates)):
                backtrack([*path, candidates[i]], total + candidates[i], i)
        backtrack([], 0, -1)
        return list(res)

s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5],
8))