import collections
import numpy as np
from typing import List
#Runtime: 60 ms, faster than 32.05% of Python3 online submissions for Destination City.
#Memory Usage: 14.1 MB, less than 5.18% of Python3 online submissions for Destination City.

#not even lexicographical with multiple entries
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        pd = collections.defaultdict(dict)
        for i, a in enumerate(paths):
            frum = a[0]
            to = a[1]
            pd[frum] = to
        for key, val in pd.items():
            if not pd[val]:
                return val

print(Solution().destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))