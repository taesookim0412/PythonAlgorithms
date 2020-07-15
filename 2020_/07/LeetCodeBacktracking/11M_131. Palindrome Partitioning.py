import collections
import numpy as np
from typing import List


#original answer:
#Runtime: 172 ms, faster than 5.11% of Python3 online submissions for Palindrome Partitioning.
#Memory Usage: 14 MB, less than 78.81% of Python3 online submissions for Palindrome Partitioning.
class Solution:
    def partition(self, s):
        res = []
        def backtrack(path, j, idx):
            if idx == len(s):
                res.append(path)
            for i in range(j, len(s)):
                if s[j:i+1] == s[j:i+1][::-1]:
                    newlen = idx + i+1-j
                    backtrack(path + [s[j:i+1]], i+1, newlen)
        backtrack([], 0, 0)
        return res

class Solution1:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(path, partition):
            #print(path, partition)
            if not partition:
                res.append(path)
            for i in range(1, len(partition)+1):
                if partition[:i] == partition[i-1::-1]:
                    backtrack(path + [partition[:i]], partition[i:])
        backtrack([], s)
        return res

class Solution2:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(s, path, res):
            if not s:
                res.append(path[:])
                return
            for i in range(1, len(s)+1):
                if s[:i] == s[i-1::-1]:
                    path.append(s[:i])
                    dfs(s[i:], path, res)
                    path.pop()
        res = []
        dfs(s, [], res)
        return res


s = Solution()
print(s.partition("aab"))