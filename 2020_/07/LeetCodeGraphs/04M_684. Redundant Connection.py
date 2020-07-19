import collections
import numpy as np
from typing import List

#Union Find:





# Runtime: 96 ms, faster than 19.51% of Python3 online submissions for Redundant Connection.
# Memory Usage: 14.9 MB, less than 5.06% of Python3 online submissions for Redundant Connection.
#dfs intuition:
class Solution2:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)

        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target:
                    return True
                #print('source',source)
                return any(dfs(nei, target) for nei in graph[source])

        for u, v in edges:
            seen = set()
            #if 2 in graph, 3 in graph
            #if dfs(2, 3) ->
            #-> graph[2]: [1]
            #-> 3 in [1,3]
            # Thus return cycle edge [2,3]
            if u in graph and v in graph and dfs(u, v):
                return [u, v]
            graph[u].add(v)
            graph[v].add(u)

s = Solution()
print(s.findRedundantConnection([[1,2], [1,3], [2,3]]))