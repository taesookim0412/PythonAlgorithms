from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res)

    def dfs(self, data, param):
        pass