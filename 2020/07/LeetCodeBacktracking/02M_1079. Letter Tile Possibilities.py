import collections
import numpy as np
from typing import List


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        def dfs(path, str):
            if path:
                res.add(path)
            for i in range(len(str)):
                dfs(path + str[i], str[:i] + str[i+1:])
        dfs('', tiles)
        return len(res)

class Solution2:
    def __init__(self):
        self.res = set()

    def numTilePossibilities(self, tiles: str):
        def dfs(path, t):
            if path:
                self.res.add(path)
            for i in range(len(t)):
                dfs(path +t[i], t[:i] + t[i+1:])
        dfs('', tiles)
        return len(self.res)

s = Solution()
print(s.numTilePossibilities("asd"))